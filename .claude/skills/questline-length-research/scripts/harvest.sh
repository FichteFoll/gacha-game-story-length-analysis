#!/bin/bash
# Harvest playthrough-video evidence (duration, title, uploader, views, URL) per act.
#
# Usage: harvest.sh <workdir> [parallelism] [--only <slug>,<slug>,...]
#   <workdir> must contain acts.tsv with one act per line:
#     chapter_id <TAB> chapter_title <TAB> act_label <TAB> act_title
#   plus versions.json and version_index.json, from fetch_versions.py.
#   Writes <workdir>/evidence/<chapter_id>_<act_label>.tsv, one row per candidate.
#
# The searches themselves, and how deep each one runs, come from queries.py:
# recent acts are searched deeper and by patch branding as well as by act title.
#
# Re-running is cheap: acts whose evidence file already exists are skipped, so a
# run interrupted by a tool timeout can simply be started again. --only overrides
# that for the named acts and appends to what they already have, which is how a
# thin act gets re-searched after the query templates change.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/yt_auth.sh"

WORKDIR="${1:?usage: harvest.sh <workdir> [parallelism] [--only slug,...]}"
JOBS="${2:-5}"
ONLY=""
[[ "${3:-}" == "--only" ]] && ONLY=",${4:?--only needs a comma-separated slug list},"
OUT="$WORKDIR/evidence"
mkdir -p "$OUT"

# A real tab, because yt-dlp's --print template does not interpret \t.
TAB=$'\t'
export TAB OUT

# Appends are staged and locked: several queries feed the same act's file.
search() {
  local slug="$1" depth="$2" query="$3" tmp
  tmp=$(mktemp)
  yt_auth "$tmp.cookies"
  timeout 240 yt-dlp "${YT_AUTH[@]+"${YT_AUTH[@]}"}" \
    --no-warnings --skip-download --flat-playlist \
    --print "%(duration)s${TAB}%(title)s${TAB}%(uploader)s${TAB}%(webpage_url)s${TAB}%(view_count)s" \
    "ytsearch${depth}:${query}" 2>/dev/null > "$tmp"
  [[ -s "$tmp" ]] && flock "$OUT" bash -c "cat '$tmp' >> '$OUT/$slug.tsv.part'"
  rm -f "$tmp" "$tmp.cookies"
}
export -f search

TODO=$(mktemp)
python3 "$HERE/queries.py" "$WORKDIR" \
  | while IFS=$'\t' read -r slug depth query; do
      if [[ -n "$ONLY" ]]; then
        [[ "$ONLY" == *",$slug,"* ]] || continue
        # Keep what is already there: dedupe runs over the seeded part file.
        [[ -s "$OUT/$slug.tsv" && ! -e "$OUT/$slug.tsv.part" ]] \
          && cp "$OUT/$slug.tsv" "$OUT/$slug.tsv.part"
      elif [[ -s "$OUT/$slug.tsv" ]]; then
        continue
      fi
      printf '%s\t%s\t%s\n' "$slug" "$depth" "$query"
    done > "$TODO"
printf 'running %s searches\n' "$(wc -l < "$TODO")"

xargs -d '\n' -P "$JOBS" -I{} bash -c \
  'IFS=$'"'"'\t'"'"' read -r s d q <<< "{}"; search "$s" "$d" "$q"' < "$TODO"

for part in "$OUT"/*.tsv.part; do
  [[ -e "$part" ]] || continue
  awk -F'\t' '!seen[$4]++' "$part" > "${part%.part}"   # dedupe by URL, keep order
  rm -f "$part"
  printf 'done %s (%s candidates)\n' \
    "$(basename "${part%.tsv.part}")" "$(wc -l < "${part%.part}")"
done
rm -f "$TODO"

echo "EXIT:0"
