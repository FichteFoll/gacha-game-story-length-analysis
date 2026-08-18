#!/bin/bash
# Add candidates to acts whose evidence pool came out too thin, using extra
# hand-written queries (usually region- or version-specific phrasings).
#
# Usage: topup.sh <workdir> [results-per-query] < queries.txt
#   queries.txt holds one "<slug>|<query>" per line, where <slug> is the evidence
#   file's basename, e.g.
#     sotwm_Act_V|Genshin Impact Nod-Krai Archon Quest Act 5 full playthrough
#
# Rows are appended and re-deduplicated by URL, so running it twice is harmless.
set -uo pipefail

WORKDIR="${1:?usage: topup.sh <workdir> [results-per-query] < queries.txt}"
PER_QUERY="${2:-8}"
OUT="$WORKDIR/evidence"
TAB=$'\t'
export OUT PER_QUERY TAB

topup() {
  local slug="$1" query="$2" f="$OUT/$1.tsv"
  timeout 240 yt-dlp --no-warnings --skip-download --flat-playlist \
    --print "%(duration)s${TAB}%(title)s${TAB}%(uploader)s${TAB}%(webpage_url)s${TAB}%(view_count)s" \
    "ytsearch${PER_QUERY}:$query" 2>/dev/null >> "$f"
  awk -F'\t' '!seen[$4]++' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
  printf 'topped up %s (%s candidates)\n' "$slug" "$(wc -l < "$f")"
}
export -f topup

xargs -d '\n' -P 5 -I{} bash -c 'IFS="|" read -r s q <<< "{}"; topup "$s" "$q"'

echo "EXIT:0"
