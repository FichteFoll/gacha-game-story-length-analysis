#!/bin/bash
# Second pass over the candidates worth measuring, one full extraction each.
#
# Usage: enrich.sh <workdir> [parallelism] [--only <slug>,<slug>,...]
#   Reads  <workdir>/analysis.json   (run analyze.sh once first, to know which
#                                     candidates are worth the extra request)
#   Writes <workdir>/enriched.tsv    url, duration, upload date, view count and
#                                    the uploader's chapter markers as JSON
#
# The harvest runs with --flat-playlist, which is fast but gives approximate view
# counts, no upload date and no chapter markers. This pass drops the flag for the
# few hundred candidates that survived title screening, or that were rejected
# only for covering several acts at once: those are exactly the uploads whose
# chapter markers let analyze.py measure one act inside a longer video.
#
# Already-fetched URLs are skipped, so an interrupted run can just be re-run.
# --only restricts the pass to the candidates of the named acts (the evidence
# files' basenames, as for harvest.sh), which is how a newly added act gets
# enriched without spending the bot-check budget on older acts' leftovers.
#
# A failed extraction adds no row, so the next run retries it; this one says how
# many URLs it attempted, enriched and failed, and exits non-zero if any failed.
# Once YouTube answers "Sign in to confirm you're not a bot", the URLs still
# queued are not attempted at all: the block is on the client, so they would
# fail the same way, and every further request only prolongs it.
#
# Set YTDLP_COOKIES or YTDLP_COOKIES_FROM_BROWSER (see yt_auth.sh) to make the
# requests as a signed-in client, which is what gets past the bot check.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/yt_auth.sh"

WORKDIR="${1:?usage: enrich.sh <workdir> [parallelism] [--only slug,...]}"
JOBS="${2:-5}"
ONLY=""
[[ "${3:-}" == "--only" ]] && ONLY="${4:?--only needs a comma-separated slug list}"
OUT="$WORKDIR/enriched.tsv"
TAB=$'\t'
# One line per attempted URL ("enriched", "failed" or "bot-check"),
# and the flag the first bot-check answer raises to stop the jobs still queued.
STATUS="$OUT.status"
BLOCKED="$OUT.blocked"
export OUT TAB STATUS BLOCKED

touch "$OUT"
rm -f "$BLOCKED"
: > "$STATUS"

if [[ -n "$ONLY" ]]; then
  jq -r --arg only "$ONLY" '($only | split(",")) - [.[].slug] | .[]
         | "no act with slug \(.) in analysis.json"' "$WORKDIR/analysis.json" >&2
fi
# Everything except the uploads rejected as not being a playthrough at all:
# those are cutscene reels and streams, and no marker makes them measurable.
jq -r --arg only "$ONLY" '.[]
       | select($only == "" or (.slug | IN($only | split(",")[])))
       | .candidates[]
       | select((.rejected | index("not-a-playthrough")) | not)
       | .url' "$WORKDIR/analysis.json" | sort -u > "$OUT.wanted"
cut -f1 "$OUT" | sort -u > "$OUT.have"
comm -23 "$OUT.wanted" "$OUT.have" > "$OUT.todo"
printf 'enriching %s of %s candidates\n' \
  "$(wc -l < "$OUT.todo")" "$(wc -l < "$OUT.wanted")"

# A marker list can run past the pipe-atomic write size, so the row is staged and
# appended under a lock rather than written straight into the shared file.
fetch_one() {
  local tmp outcome=enriched
  [[ -e "$BLOCKED" ]] && return
  tmp=$(mktemp)
  yt_auth "$tmp.cookies"
  timeout 120 yt-dlp "${YT_AUTH[@]+"${YT_AUTH[@]}"}" --no-warnings --skip-download \
    --print "%(webpage_url)s${TAB}%(duration)j${TAB}%(upload_date)j${TAB}%(view_count)j${TAB}%(chapters)j" \
    "$1" 2> "$tmp.err" > "$tmp"
  if [[ -s "$tmp" ]]; then
    flock "$OUT" bash -c "cat '$tmp' >> '$OUT'"
  elif grep -q "confirm you.re not a bot" "$tmp.err"; then
    outcome=bot-check
    touch "$BLOCKED"
  else
    outcome=failed
  fi
  flock "$STATUS" bash -c "echo $outcome >> '$STATUS'"
  rm -f "$tmp" "$tmp.err" "$tmp.cookies"
}
export -f fetch_one

xargs -d '\n' -P "$JOBS" -I{} bash -c 'fetch_one "{}"' < "$OUT.todo"

attempted=$(wc -l < "$STATUS")
enriched=$(grep -cx enriched "$STATUS")
bot_checks=$(grep -cx bot-check "$STATUS")
failed=$((attempted - enriched))
cut -f1 "$OUT" | sort -u > "$OUT.have"
printf 'attempted %s, enriched %s, failed %s; %s of %s candidates still unenriched\n' \
  "$attempted" "$enriched" "$failed" \
  "$(comm -23 "$OUT.wanted" "$OUT.have" | wc -l)" "$(wc -l < "$OUT.wanted")"
if [[ -e "$BLOCKED" ]]; then
  printf '%s\n' \
    "BOT CHECK: $bot_checks of the failures were \"Sign in to confirm you're not a bot\"," \
    "and the URLs still queued were not attempted. Solve the captcha in a browser" \
    "or set cookies (see yt_auth.sh), then re-run: it resumes from enriched.tsv."
else
  echo "bot check: not seen"
fi
rm -f "$OUT.wanted" "$OUT.have" "$OUT.todo" "$STATUS" "$BLOCKED"

rc=0
((failed > 0)) && rc=1
echo "EXIT:$rc"
exit "$rc"
