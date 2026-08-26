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
#
# Several queries for one act run at the same time, so, as in harvest.sh, each
# one stages its rows in a file of its own and appends them under a lock. Two
# jobs rewriting an act's evidence file at once loses whatever the other one had
# just written, and the loss is silent: the file is still there, only shorter.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/yt_auth.sh"

WORKDIR="${1:?usage: topup.sh <workdir> [results-per-query] < queries.txt}"
PER_QUERY="${2:-8}"
OUT="$WORKDIR/evidence"
TAB=$'\t'
export OUT PER_QUERY TAB
mkdir -p "$OUT"

topup() {
  local slug="$1" query="$2" tmp
  tmp=$(mktemp)
  yt_auth "$tmp.cookies"
  timeout 240 yt-dlp "${YT_AUTH[@]+"${YT_AUTH[@]}"}" \
    --no-warnings --skip-download --flat-playlist \
    --print "%(duration)s${TAB}%(title)s${TAB}%(uploader)s${TAB}%(webpage_url)s${TAB}%(view_count)s" \
    "ytsearch${PER_QUERY}:$query" 2>/dev/null > "$tmp"
  [[ -s "$tmp" ]] && flock "$OUT" bash -c "cat '$tmp' >> '$OUT/$slug.tsv.part'"
  rm -f "$tmp" "$tmp.cookies"
}
export -f topup

xargs -d '\n' -P 5 -I{} bash -c 'IFS="|" read -r s q <<< "{}"; topup "$s" "$q"'

for part in "$OUT"/*.tsv.part; do
  [[ -e "$part" ]] || continue
  f="${part%.part}"
  cat "$part" >> "$f"
  awk -F'\t' '!seen[$4]++' "$f" > "$f.tmp" && mv "$f.tmp" "$f"   # keep order
  rm -f "$part"
  printf 'topped up %s (%s candidates)\n' \
    "$(basename "${f%.tsv}")" "$(wc -l < "$f")"
done

echo "EXIT:0"
