---
name: questline-length-research
description: Estimate how long the chapters and acts of a game's storyline take, by taking the questline structure from a Fandom wiki and measuring durations from YouTube playthrough uploads, then writing per-chapter markdown reports with a full evidence vault. Use for questions like "how long does each act of X take", "how long is chapter Y", or any request to time story content that has no official playtime figures.
---

# Questline length research from wiki structure plus video evidence

Produces defensible playtime estimates for story content that no publisher documents:
the questline skeleton comes from a wiki,
the numbers come from the runtime of uploads of people playing it,
and every number keeps the evidence that produced it.

## What good output looks like

- One markdown file per chapter,
  plus a `README.md` index carrying the chapter table, the method and the caveats.
- Every act has: an estimate, the sampled range, the number of uploads behind it,
  a confidence rating, and a collapsed evidence table listing
  runtime, video title, uploader, view count and URL for each accepted upload.
- Every factual claim about the questline itself
  (act titles, quest parts, gates, release versions)
  is traceable to a wiki page that is linked.
- The estimate is a **median**, never a single video's runtime.
  One upload is an anecdote.

## Step 1: get the structure from the wiki

Fandom serves a Cloudflare challenge to plain HTTP clients,
so both `WebFetch` and `curl` on `/wiki/<Page>` return 402 or 403.
Use the MediaWiki API instead, which is not challenged:

```bash
curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64)' \
  'https://<wiki>.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json'
```

Batch the per-act pages rather than fetching them one at a time,
up to 50 titles per request:

```bash
curl -sS -A 'Mozilla/5.0' -G 'https://<wiki>.fandom.com/api.php' \
  --data-urlencode action=query --data-urlencode prop=revisions \
  --data-urlencode rvprop=content --data-urlencode rvslots=main \
  --data-urlencode format=json --data-urlencode 'titles=Act One|Act Two|...'
```

Useful properties beyond the wikitext:

- `prop=categories&cllimit=max` returns rendered categories,
  which is how you get facts that templates add rather than the wikitext,
  such as `Released in Version 3.2`.
  Wikitext greps for a `|version=` field find nothing.
- Not every recent page is categorized yet.
  Fall back to the version named in the sampled upload titles,
  and say in the report that this is where it came from.

Write the structure to `<workdir>/acts.tsv`,
one act per line, tab separated:

```
chapter_id <TAB> chapter_title <TAB> act_label <TAB> act_title
```

Then confirm the extracted list against the wiki's own overview page before measuring anything.
An act list that silently misses an interlude produces a report that is wrong everywhere.

## Step 2: harvest video evidence

`yt-dlp` searches YouTube and reports duration, title, uploader and URL in one call,
so no separate search tool is needed:

```bash
scripts/harvest.sh <workdir> [results-per-query]
```

It runs two queries per act
(chapter plus act label plus act title, then act title alone),
dedupes by URL and writes `<workdir>/evidence/<slug>.tsv`.
Already-harvested acts are skipped, so an interrupted run can just be re-run.

## Step 3: screen and compute

```bash
scripts/analyze.py <workdir>
```

Screening is the part that determines whether the numbers mean anything.
Discard, by title:

- **not a playthrough**: cutscene reels, cinematic edits, lore explainers,
  guides, reactions, soundtrack rips.
  A cutscene compilation of a four-hour act runs 40 minutes and would wreck the median.
- **streams and let's-plays**: idle chatter inflates runtime far past the act.
- **multi-act compilations**: "Acts 9 & 10", "Full Sumeru Archon Quest", "all acts".
  Add franchise-specific phrasings via `<workdir>/compilations.txt`.
  Careful: "Full Archon Quest" on its own is the normal phrasing
  for one complete act, not a compilation. Do not filter it.
- **wrong act**: the title must name the act,
  either by title words or by act number *and* chapter identifier
  (supply the identifiers in `<workdir>/chapter_keys.json`).
  Requiring both halves is what stops "Snezhnaya Act 1"
  from being counted as evidence for a different chapter's Act I.

Then drop anything below half or above 1.8 times the median as truncated or padded.

Publish the median as the estimate, the min and max as the range,
and a confidence rating from the sample size and the spread
(high: 8+ uploads within a factor of 1.6; medium: 6+ within 2.2; low: otherwise).

## Step 4: top up the thin acts

`analyze.py` flags acts with fewer than six accepted uploads.
The newest chapters are always thinnest.
Feed extra hand-written queries in:

```bash
printf 'sotwm_Act_V|<region> Archon Quest Act 5 <act title> full playthrough\n' \
  | scripts/topup.sh <workdir>
```

Re-run `analyze.py` and check whether the median moved.
If a top-up shifts a median by more than about 20 percent,
that act's figure is soft; rate it low confidence and say so.

## Step 5: audit before writing

Print the accepted and rejected candidates for the widest-spread acts and read them.
Every pass so far has found the filters both over- and under-rejecting on the first try.
Fix the patterns, re-run, and only then generate the report.

## Step 6: write the report

Per chapter: header line with region, versions, entry count and chapter total;
a short story blurb; an at-a-glance act table; a pacing paragraph
explaining *why* the chapter times out the way it does;
then one section per act with the metadata, the quest parts and the evidence table.

See `reference/report-format.md` for the exact layout that worked.

## Pitfalls that have already cost time

- `yt-dlp --print "%(duration)s\t..."` does **not** interpret `\t`.
  Pass a real tab (`TAB=$'\t'` and `${TAB}` in the template),
  or every downstream field split silently collapses.
- Label the count of chapter entries "entries", not "acts",
  when a chapter also contains a prelude, prologue or interlude.
- Quest part titles can contain commas
  ("Into the Wind, Into the Frigid North" is one quest).
  Join part lists with semicolons or the count contradicts the list.
- A chapter's wiki page name is often not its display title:
  the page is `Chapter VII`, not `Chapter VII: Everwinter Without Mercy`.
  Link the page name, and verify it resolves through the API before publishing.
- Do not assert release versions from memory. Query them.
- View counts come from the search listing and are approximate. Label them as such.
- Say plainly what the numbers are:
  video runtime of someone else playing, as a proxy for act length.
  They are not official, they include the uploader's detours,
  and they exclude a first-timer's re-reading and deaths.
