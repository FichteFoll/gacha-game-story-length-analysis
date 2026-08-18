#!/bin/bash
# Second pass over the candidates worth measuring, one full extraction each.
#
# Usage: enrich.sh <workdir> [parallelism]
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
set -uo pipefail

WORKDIR="${1:?usage: enrich.sh <workdir> [parallelism]}"
JOBS="${2:-5}"
OUT="$WORKDIR/enriched.tsv"
TAB=$'\t'
export OUT TAB

touch "$OUT"

# Everything except the uploads rejected as not being a playthrough at all:
# those are cutscene reels and streams, and no marker makes them measurable.
jq -r '.[] | .candidates[]
       | select((.rejected | index("not-a-playthrough")) | not)
       | .url' "$WORKDIR/analysis.json" | sort -u > "$OUT.wanted"
cut -f1 "$OUT" | sort -u > "$OUT.have"
comm -23 "$OUT.wanted" "$OUT.have" > "$OUT.todo"
printf 'enriching %s of %s candidates\n' \
  "$(wc -l < "$OUT.todo")" "$(wc -l < "$OUT.wanted")"

# A marker list can run past the pipe-atomic write size, so the row is staged and
# appended under a lock rather than written straight into the shared file.
fetch_one() {
  local tmp
  tmp=$(mktemp)
  timeout 120 yt-dlp --no-warnings --skip-download \
    --print "%(webpage_url)s${TAB}%(duration)j${TAB}%(upload_date)j${TAB}%(view_count)j${TAB}%(chapters)j" \
    "$1" 2>/dev/null > "$tmp"
  [[ -s "$tmp" ]] && flock "$OUT" bash -c "cat '$tmp' >> '$OUT'"
  rm -f "$tmp"
}
export -f fetch_one

xargs -d '\n' -P "$JOBS" -I{} bash -c 'fetch_one "{}"' < "$OUT.todo"
rm -f "$OUT.wanted" "$OUT.have" "$OUT.todo"

printf 'enriched %s videos\n' "$(wc -l < "$OUT")"
echo "EXIT:0"
