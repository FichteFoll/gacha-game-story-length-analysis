---
name: questline-length-research
description: Estimate how long the chapters and acts of a game's storyline take, by taking the questline structure from a Fandom wiki and measuring durations from YouTube playthrough uploads, then writing per-chapter markdown reports with a full evidence vault. Use for questions like "how long does each act of X take", "how long is chapter Y", or any request to time story content that has no official playtime figures.
---

# Questline length research from wiki structure plus video evidence

Produces defensible playtime estimates for story content that no publisher documents:
the questline skeleton comes from a wiki,
the numbers come from the runtime of uploads of people playing it,
and every number keeps the evidence that produced it.

Nothing in `scripts/` is specific to one game.
A new game is a new report directory holding its data and its prose,
never a copy of a script;
see `reference/games.md` for the wiki, the questline page and the level gate
of the games already looked at.

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

## Step 0: lay out the report directory

One directory per game, named after the game, holding only what is game-specific:

```
<report>/data/wiki.json           which wiki, and how it records versions
<report>/data/game.txt            the game's name, as uploaders spell it
<report>/data/acts.tsv            the questline structure (step 1)
<report>/data/chapter_keys.json   words that identify each chapter in a title
<report>/data/query_templates.txt the YouTube searches to run per act
<report>/data/compilations.txt    extra multi-act phrasings this game's uploads use
<report>/report.py                the game's configuration and the authored prose
<report>/claims.py                what that prose asserts about the data
```

Every game names its story hierarchy differently.
Map it onto chapter and act:
Wuthering Waves already divides Main Quests into chapters and acts,
Honkai: Star Rail groups Trailblaze Missions by world,
Zenless Zone Zero cuts Phaethon's Story into chapters.
Whatever the game calls the smaller unit,
put that word in the act label (`Act 3`, `Episode 2`),
because the screening reads the unit off the label.

`data/wiki.json` carries the host and the wiki's own name,
plus how it records release versions where that differs from the default
(`released_in`, `version_page`, `version_fields`; see `scripts/fetch_versions.py`).
Set `released_in` to `null` for a wiki that does not categorize by version at all.

`report.py` carries the report's title and intro, the wiki page that documents
the questline, the level gate's name (`gate_label`, `None` for a game without one),
the publisher, the per-game wording the method section quotes,
the caveats that apply to this report only, and the authored prose.

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
scripts/fetch_versions.py <workdir>
```

This writes `versions.json` (act title -> version name)
and `version_index.json` (version -> patch number and release date),
using the conventions in `<workdir>/wiki.json`.
Do it first, not afterwards as a reporting detail:
recent uploads are titled by patch branding rather than by act title
("Genshin Impact 6.6 Act 10 Full Walkthrough"),
so the harvest needs the branding to search for them,
and the release date is what tells it which acts are recent.

Check the printed count before moving on.
The version infobox is not the same on every wiki
(Genshin has `|number` and `|date`, Honkai: Star Rail `|version` and `|release_date`),
and a wrong field name yields an index with no dates,
which silently makes every act look old and every search shallow.

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

The last two are worth writing in the game's own vocabulary
("trailblaze mission", "main quest"), because that is how its uploads are titled.
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
  The unit ("act", "episode") comes from the act labels,
  the container ("chapter", "episode", "arc") is fixed,
  and anything else this game's uploaders say
  goes in `<workdir>/compilations.txt`.
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

```bash
scripts/gen_docs.py <report> [--no-verify]
```

Per chapter: header line with region, versions, entry count and chapter total;
a short story blurb; an at-a-glance act table; a pacing paragraph
explaining *why* the chapter times out the way it does;
then one section per act with the metadata, the quest parts and the evidence table.
The renderer is generic; what it renders comes from the report's
`report.py` (configuration and prose) and `claims.py`.

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

The vocabulary for those assertions is in `scripts/assertions.py`;
the assertions themselves belong in the report's own `claims.py`.
Verification is the default and `--no-verify` is the escape hatch.
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
- Do not assert a wiki host, an overview page or an infobox field from memory
  either. One `action=query&meta=siteinfo` call settles the host,
  and one `titles=` call settles whether a page exists.
- View counts from the search listing are approximate,
  and the full extraction pass only reaches some of the videos.
  Label the two apart rather than calling them all approximate.
- Chapter markers are worth more than any query tuning.
  Check for them before spending a session widening searches.
- Keep the screening patterns word-bounded.
  `arc` without one matches "Archon", and every "Full Archon Quest"
  (one complete act) is thrown away as a compilation.
- Say plainly what the numbers are:
  video runtime of someone else playing, as a proxy for act length.
  They are not official, they include the uploader's detours,
  and they exclude a first-timer's re-reading and deaths.
