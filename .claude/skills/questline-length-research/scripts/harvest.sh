#!/bin/bash
# Harvest playthrough-video evidence (duration, title, uploader, views, URL) per act.
#
# Usage: harvest.sh <workdir> [results-per-query]
#   <workdir> must contain acts.tsv with one act per line:
#     chapter_id <TAB> chapter_title <TAB> act_label <TAB> act_title
#   Writes <workdir>/evidence/<chapter_id>_<act_label>.tsv, one row per candidate.
#
# Re-running is cheap: acts whose evidence file already exists are skipped, so a
# run interrupted by a tool timeout can simply be started again.
set -uo pipefail

WORKDIR="${1:?usage: harvest.sh <workdir> [results-per-query]}"
PER_QUERY="${2:-6}"
OUT="$WORKDIR/evidence"
mkdir -p "$OUT"

# A real tab, because yt-dlp's --print template does not interpret \t.
TAB=$'\t'
export TAB OUT PER_QUERY

search() {
  timeout 240 yt-dlp --no-warnings --skip-download --flat-playlist \
    --print "%(duration)s${TAB}%(title)s${TAB}%(uploader)s${TAB}%(webpage_url)s${TAB}%(view_count)s" \
    "ytsearch${PER_QUERY}:$1" 2>/dev/null
}
export -f search

harvest_one() {
  local chap_id="$1" act_label="$2" act_title="$3" chap_title="$4"
  local slug
  slug=$(printf '%s_%s' "$chap_id" "$act_label" | tr -c 'A-Za-z0-9_-' '_')
  local f="$OUT/$slug.tsv"
  [[ -s "$f" ]] && { echo "skip $slug (already harvested)"; return 0; }

  {
    search "${chap_title%%:*} ${act_label} ${act_title} full walkthrough no commentary"
    search "${act_title} full quest gameplay"
  } > "$f.part"

  awk -F'\t' '!seen[$4]++' "$f.part" > "$f"   # dedupe by URL, keep search order
  rm -f "$f.part"
  printf 'done %s (%s candidates)\n' "$slug" "$(wc -l < "$f")"
}
export -f harvest_one

# Five concurrent searches keeps well clear of YouTube throttling.
awk -F'\t' 'NF>=4 {print $1"\t"$3"\t"$4"\t"$2}' "$WORKDIR/acts.tsv" \
  | xargs -d '\n' -P 5 -I{} bash -c \
      'IFS=$'"'"'\t'"'"' read -r a b c d <<< "{}"; harvest_one "$a" "$b" "$c" "$d"'

echo "EXIT:0"
