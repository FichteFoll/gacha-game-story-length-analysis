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
- A batch of 50 pages runs past the API's 500-entry response limit,
  and the pages that get cut off come back looking uncategorized.
  Follow `continue` or you will silently lose the acts at the end of the batch.
- Write the quest parts of each act to `<workdir>/quest_parts.json`,
  keyed `"<chapter_id>|<act_label>"`.
  They are what chapter markers get matched against in step 4.


Write the structure to `<workdir>/acts.tsv`,
one act per line, tab separated:

```
chapter_id <TAB> chapter_title <TAB> act_label <TAB> act_title
```

Then confirm the extracted list against the wiki's own overview page before measuring anything.
An act list that silently misses an interlude produces a report that is wrong everywhere.

## Step 2: fetch the release versions, before harvesting anything

```bash
scripts/fetch_versions.py <workdir> <wiki-host>
```

This writes `versions.json` (act title -> version name)
and `version_index.json` (version -> patch number and release date).
Do it first, not afterwards as a reporting detail:
recent uploads are titled by patch branding rather than by act title
("Genshin Impact 6.6 Act 10 Full Walkthrough"),
so the harvest needs the branding to search for them,
and the release date is what tells it which acts are recent.

## Step 3: harvest video evidence

`yt-dlp` searches YouTube and reports duration, title, uploader and URL in one call,
so no separate search tool is needed:

```bash
scripts/harvest.sh <workdir> [parallelism] [--only <slug>,...]
```

The searches come from `queries.py`, which formats
`<workdir>/query_templates.txt` per act and emits a depth for each:

```
{chapter} {act_label} {act_title} full walkthrough no commentary
{act_title} full quest gameplay
{game} {number} Act {act_number} {act_title}
{game} {version} archon quest act {act_number} walkthrough
```

A template naming a field the act has no value for is skipped,
so an uncategorized act is never searched for as "None Act 3".
Acts released within the last four versions are searched twice as deep:
`ytsearch6` is fine for content with hundreds of uploads
and far too shallow for anything a month old.

Already-harvested acts are skipped, so an interrupted run can just be re-run.
`--only` overrides that for the named acts and appends,
which is how a thin act gets re-searched after the templates change.

## Step 4: fetch exact metadata and chapter markers

```bash
scripts/enrich.sh <workdir> [parallelism]
```

The harvest runs with `--flat-playlist`: fast, but it rounds view counts,
reports no upload date, and carries no chapter markers.
This second pass drops the flag
for every candidate not already discarded as a non-playthrough.

The chapter markers are the single biggest precision upgrade available.
Walkthrough uploads very often name their markers after the quest parts,
so matching markers against `quest_parts.json`
locates one act inside a longer upload. That means:

- a "Acts 9 & 10" compilation becomes evidence for each act separately,
  instead of being thrown away;
- the uploader's pre-roll and detours drop out of the measurement;
- a quest part marked out by several uploads gets its own median.

Ignore a marker set covering less than 60 percent of a single-act upload:
those markers were something else, and trusting them under-measures the act.

YouTube starts answering "Sign in to confirm you're not a bot"
after a few hundred full extractions.
The script is resumable and `analyze.py` falls back to the harvested figures,
so re-run it later rather than fighting it.

## Step 5: screen and compute

```bash
scripts/analyze.py <workdir> [--compare <baseline>]
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
  A compilation whose chapter markers locate the act is readmitted, measured.
- **wrong act**: the title must name the act,
  either by title words or by act number *and* chapter identifier
  (supply the identifiers in `<workdir>/chapter_keys.json`;
  the version names and patch numbers are added per chapter automatically).
  Requiring both halves is what stops "Snezhnaya Act 1"
  from being counted as evidence for a different chapter's Act I.

Then drop anything below half or above 1.8 times the median as truncated or padded.

Publish the median as the estimate.
For the range, publish the interquartile range from eight uploads on,
with the full spread alongside it:
one padded upload distorts a min-max range that is otherwise tight.

Rate nothing above low confidence on fewer than eight uploads,
then *high* when the middle half spans a factor under 1.25 and *medium* under 1.5.
Hold the interquartile range to a tighter factor than a full spread,
or switching metric alone promotes everything.

Two checks that replace reviewer judgement, both free:

- `--compare <earlier analysis.json>` records how far each median moved.
  An act whose median moves by 10 percent or more
  when the query set changes was never settled: rate it low, by definition.
- `analyze.py` compares each bundled upload's runtime
  against the sum of the medians of the acts it bundles.
  Those uploads were harvested anyway and are sitting in the rejected pile,
  and agreement within a few percent is corroboration
  that no amount of re-searching the same queries can give you.

## Step 6: top up the thin acts

`analyze.py` flags acts with fewer than six accepted uploads,
and the eight-upload floor on confidence flags the rest.
The newest chapters are always thinnest.
First re-run the templates deeper for those acts:

```bash
scripts/harvest.sh <workdir> 6 --only <slug>,<slug>
```

Then, for what that does not reach, hand-written queries:

```bash
printf 'sotwm_Act_V|<region> Archon Quest Act 5 <act title> full playthrough\n' \
  | scripts/topup.sh <workdir>
```

Keep the analysis from before the top-up and pass it to `--compare`:
a median that moves by more than 10 percent was never settled,
and that is a measurement rather than a judgement call.

## Step 7: audit before writing

Print the accepted and rejected candidates for the widest-spread acts and read them.
Every pass so far has found the filters both over- and under-rejecting on the first try.
Fix the patterns, re-run, and only then generate the report.

## Step 8: write the report

Per chapter: header line with region, versions, entry count and chapter total;
a short story blurb; an at-a-glance act table; a pacing paragraph
explaining *why* the chapter times out the way it does;
then one section per act with the metadata, the quest parts and the evidence table.

See `reference/report-format.md` for the exact layout that worked.

**Do not write a number into the prose.** Prose written against a mental model
of the data is wrong roughly as often as it is checked, and it goes stale the
moment a re-harvest moves a median. Instead:

- give the prose placeholders and fill them from the analysis at render time
  ("{n_above_2h} of its {n_entries} acts sit above two hours");
- generate superlatives from a ranking computed over all acts,
  so "the longest act in the game" can only appear where it is true,
  and a tie is stated as a tie;
- write down whatever claim the words still make
  ("marathon acts", "the chapter centrepiece", "by far the largest chapter")
  as an assertion over the analysis, evaluated before any file is written,
  failing the build with the sentence it guards.

Make that verification the default and put the escape hatch behind a flag.
The test is: delete a video from an evidence file, re-run,
and the build should either fail or correct itself.

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
- Do not assert release versions from memory. Query them, before harvesting.
- View counts from the search listing are approximate,
  and the full extraction pass only reaches some of the videos.
  Label the two apart rather than calling them all approximate.
- Chapter markers are worth more than any query tuning.
  Check for them before spending a session widening searches.
- Say plainly what the numbers are:
  video runtime of someone else playing, as a proxy for act length.
  They are not official, they include the uploader's detours,
  and they exclude a first-timer's re-reading and deaths.
