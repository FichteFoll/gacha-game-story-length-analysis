---
name: questline-length-research
description: Estimate how long the chapters and acts of a game's storyline take, by taking the questline structure from a community wiki (Fandom or wiki.gg) and measuring durations from YouTube playthrough uploads, then writing per-chapter markdown reports with a full evidence vault. Use for questions like "how long does each act of X take", "how long is chapter Y", or any request to time story content that has no official playtime figures.
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
  plus a `README.md` index carrying the chapter table, what this game's harvest
  does differently, and the caveats that apply to this report only.
  The shared procedure lives in the repository README, one level up.
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
<report>/README.md                the authored index, with its placeholders
<report>/00-<chapter-slug>.md     the authored chapter files, one per chapter
<report>/data/wiki.json           which wiki, and how it records versions
<report>/data/game.txt            the game's name, as uploaders spell it
<report>/data/acts.tsv            the questline structure (step 1)
<report>/data/chapter_keys.json   words that identify each chapter in a title
<report>/data/act_keys.json       marks that tell two same-named acts apart
<report>/data/query_templates.txt the YouTube searches to run per act
<report>/data/not_playthrough.txt phrasings for footage that is not the questline
<report>/data/compilations.txt    extra multi-act phrasings this game's uploads use
<report>/data/partials.txt       phrasings for less than one act, if the game has any
<report>/data/min_minutes.txt    runtime floor, if the game's entries are all long
<report>/report.py                the game's configuration and structure
<report>/claims.py                what the prose asserts about the data
```

Every game names its story hierarchy differently.
Map it onto chapter and act:
Wuthering Waves already divides Main Quests into chapters and acts,
Honkai: Star Rail groups Trailblaze Missions by world,
Zenless Zone Zero cuts Phaethon's Story into chapters.
Whatever the game calls the smaller unit,
put that word in the act label (`Act 3`, `Episode 2`),
because the screening reads the unit off the label.

Pick the unit the *uploads* are titled after, not the one the wiki files under.
Zenless Zone Zero releases each Season 1 chapter in an (A) and a (B) half,
and the wiki writes one page per half,
but no upload covers a half or says which half it is,
so the report's act is the whole chapter.
Where the halves shipped a version apart, uploaders do say,
and those halves are separate acts.
An act list that measures a unit nobody uploads
is a pool of half-length videos counted as whole ones.

`data/wiki.json` carries the host and the wiki's own name,
plus how it records release versions where that differs from the default
(`released_in`, `version_page`, `version_fields`; see `scripts/fetch_versions.py`).
Set `released_in` to `null` for a wiki that does not categorize by version at all.

`report.py` carries no prose.
It records the wiki page that documents the questline (`overview_page`),
which no script reads any more and the authored markdown links by hand,
the level gate's name (`gate_label`, `None` for a game without one)
and the gates themselves, the collection date,
and the three nouns the renderer writes with: what one entry is (`unit`),
what a file's worth of them is (`container`, "Chapter" by default)
and what their second column holds (`region_label`, "Region" by default,
"Part" for a game that groups its story by narrative rather than by place),
and the chapter list with each chapter's id, slug, region, versions and title,
plus the chapter's own wiki page, which the markdown likewise links by hand
(an act's page reaches the filler through `analysis.json` instead).
The report's title, its intro, its method wording and its caveats
are written in `<report>/README.md`,
and a chapter's blurb, pacing paragraph and act notes
in that chapter's own markdown file.

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
chapter_id <TAB> chapter_title <TAB> act_label <TAB> act_title [<TAB> wiki page]
```

The fifth column is optional and defaults to the act title.
Name a page there whenever the two differ:
where an act is documented under one of its halves,
or under a page title the display title is only part of.
It is what the version lookup queries and what the report links.

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

A wiki that records nothing per act, and states on each version's own page
which acts that version shipped, is the one case where `versions.json` is
written by hand: set `released_in` to null, write the mapping out from those
sentences, and this script keeps it and indexes the versions it names.

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
so do not fight it: retrying straight away buys a trickle and then stops again.
Say that the run hit the bot check,
say how many URLs are still unenriched,
and let the user decide between the two ways out.

- **A captcha, solved in a browser.** Only a person can do it, and it lifts the
block for a while rather than for good: the lift has been worth anywhere
between a handful of URLs and a couple of hundred, and it has also come back
on its own after an hour of doing nothing. Re-run `enrich.sh` when told it is
solved; it resumes from `enriched.tsv`.
- **Cookies**, which is the durable fix, because the block is on the client and
a signed-in client is not subject to it. Set one of the two variables in
`scripts/yt_auth.sh` — `YTDLP_COOKIES=<cookies.txt>` or
`YTDLP_COOKIES_FROM_BROWSER=<browser>` — and all three network scripts pass
it to `yt-dlp`. The browser form needs the browser's own cookie store, so it
only works where the browser is: from a sandbox, ask the user to export a
`cookies.txt` once and bind it in, or to run the script themselves.
Say plainly that it means signing the requests in as somebody, and that the
account is the one that wears the consequences, so it should be a throwaway.

Either way, finish with `analyze.py` and `gen_docs.py`
to fold the new markers in.

## Step 5: screen and compute

```bash
scripts/analyze.py <workdir> [--compare <baseline>]
```

Screening is the part that determines whether the numbers mean anything.
Discard, by title:

- **not a playthrough**: cutscene reels, cinematic edits, lore explainers,
  guides, reactions, soundtrack rips.
  A cutscene compilation of a four-hour act runs 40 minutes and would wreck the median.
  The shared list covers what every pool carries;
  a phrasing peculiar to this game ("exploration only", "VOD")
  goes in `<workdir>/not_playthrough.txt`.
  A highlight clip has no phrasing to catch: it names the chapter, says
  nothing about its scope and runs three minutes. Where every entry of a game
  is twenty minutes or more, put a runtime floor in
  `<workdir>/min_minutes.txt` (one number) and they are counted out as not
  being playthroughs, which spares the second pass fetching them too.
- **streams and let's-plays**: idle chatter inflates runtime far past the act.
- **multi-act compilations**: "Acts 9 & 10", "Full Sumeru Archon Quest", "all acts".
  The unit ("act", "episode") comes from the act labels,
  the container ("chapter", "episode", "arc") is fixed
  minus whatever this game numbers its acts with
  (a game whose act *is* a chapter would otherwise read
  every "Full Chapter 3" as a compilation of chapters),
  and anything else this game's uploaders say
  goes in `<workdir>/compilations.txt`.
  Careful: "Full Archon Quest" on its own is the normal phrasing
  for one complete act, not a compilation. Do not filter it.
  A title that pins exactly one act by the unit and a numeral
  ("FULL Chapter 2 - Process 3") is that act however it words its scope,
  so the scope words are overruled rather than the other way round.
  A compilation whose chapter markers locate the act is readmitted, measured.
- **part of an act**: "Part 3", "Walkthrough II", or a title naming
  a single quest part of the act.
  Where an act runs for hours, uploaders split it,
  and a split's runtime measures the split.
  This one is off unless `<workdir>/partials.txt` says otherwise,
  because what a split is called differs per game;
  the line `<quest part>` in that file additionally reads
  a title naming one of the act's quest parts as a split.
  An upload whose runtime matches what the unambiguous uploads measured
  is readmitted whatever it calls itself,
  unless the pattern that caught it is prefixed `!`,
  which marks a wording that admits of no second reading:
  where an act *is* a chapter and the game divides a chapter into acts of its
  own, "Act 3" is a third of the entry however long the video runs,
  where "Part 3" might be the third instalment of a complete playthrough.
  Leaving these to the outlier trim does not work:
  enough of them drag the median they are trimmed against down with them,
  until the complete uploads are the ones that look like outliers.
- **wrong act**: the title must name the act,
  either by title words or by act number *and* chapter identifier
  (supply the identifiers in `<workdir>/chapter_keys.json`;
  the version names and patch numbers are added per chapter automatically).
  Requiring both halves is what stops "Snezhnaya Act 1"
  from being counted as evidence for a different chapter's Act I.
  A title that pins a *different* number of the same unit is out even where
  the act's title words are all in it: an uploader who repeats one act's name
  across a whole chapter ("Chapter 1 Process 4 - The Broken Lands")
  is evidence for the number, not for the name.
- **the wrong one of two same-named acts**: where the title match cannot tell
  two acts apart, give the pair their distinguishing marks in
  `<workdir>/act_keys.json`, keyed `"<chapter_id>|<act_label>"`:
  a title then has to carry one of them to count as evidence for that act.
  Zenless Zone Zero's epilogue halves differ only by a "(A)" or "(B)"
  that the word matching never sees,
  and an upload that names neither half is evidence for neither.
  The same file is the place for a negative mark,
  written as a lookahead (`^(?!.*interlude)`),
  where a title matching "Chapter 2" would otherwise
  count for "Chapter 2 Interlude" as well,
  or where an act's own title is degenerate:
  the words of "The Zero Zone" are in every Zenless Zone Zero upload's title.

- **one uploader, one title, several videos**: a channel that publishes an act
  in instalments often reuses the title verbatim and lets the upload order
  carry the sequence, so nothing in the wording says "part 2".
  Those are read as splits automatically, without a pattern.
- **the same uploader twice**: an uploader who posts a single-act upload
  *and* a compilation that contains it
  offers one playthrough under two URLs,
  and readmitting compilations by their chapter markers
  makes that the common case rather than the rare one.
  Only one row per uploader survives per act:
  the marker-measured one, which is bounded by the act
  rather than by where the upload starts and stops,
  and between two of a kind the shorter one.

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
Fix the patterns, re-run, and only then write the report.

## Step 8: write the report

You write the markdown; the pipeline fills in the derived parts:

```bash
scripts/gen_docs.py <report> [--no-verify] [--scaffold]
```

Per chapter: header line with region, versions, entry count and chapter total;
a short story blurb; an at-a-glance act table; a pacing paragraph
explaining *why* the chapter times out the way it does;
then one section per act with the metadata, the quest parts and the evidence table.
The blurb, the pacing paragraph, the act notes, the headings and the sources
are hand-written in the chapter file itself,
and so are the report `README.md`'s intro, method wording and caveats.
Everything derived sits in a placeholder in that same file,
which `gen_docs.py` rewrites in place, leaving the prose around it as written
(it does right-strip every line and end the file in one newline,
so a two-space hard line break does not survive a run).
The filler is generic; the structure it needs
(chapter ids, slugs, wiki pages, regions, versions, gates and the nouns)
comes from the report's `report.py`, and the claims from its `claims.py`.

The placeholders are HTML comments, in two forms:

- an inline value, `<!--f:NAME-->2 h 10 min<!--/f-->`,
  both markers on the same line and never nested inside another `f:` marker,
  `NAME` naming a fact computed from `analysis.json`;
- a generated block,
  `<!--gen:KIND[ attr="value" ...]-->` ... `<!--/gen-->`,
  each marker on a line of its own,
  for a table or a bullet list:
  `chapters`, `extremes` and `thresholds` in the report `README.md`,
  `heading`, `glance`, `act-heading act="Act I"`, `stats act="Act I"`
  and `evidence act="Act I"` in a chapter file.

Keep a `gen:` block out of any paragraph, with a blank line on either side:
a line holding only an HTML comment starts an HTML block in CommonMark
and splits the paragraph in two.
The one exception the reports make is `gen:stats`,
whose opener follows the act note's last line directly
because the region starts at the derived superlative sentence;
that costs a paragraph break in the rendered page,
and is accepted rather than changing the published source.
A value inside a sentence is therefore always the inline `f:` form,
and it never spans a line break.
An unknown name or kind, or an unterminated marker, fails the build.

An act that `analysis.json` has and the markdown does not also fails the build,
naming the act;
`--scaffold` writes the stub sections for it instead,
which is what to run after a re-harvest has turned up a new act.
The scaffolded prose, and a new chapter's `## Sources` section,
still have to be written by hand.

See `reference/report-format.md` for the exact layout that worked.

**Do not write a number into the prose.** Prose written against a mental model
of the data is wrong roughly as often as it is checked, and it goes stale the
moment a re-harvest moves a median.
Nothing stops you from typing a figure into a sentence any more,
now that the sentences are markdown rather than Python format strings,
so this is a rule you keep rather than one the filler enforces.
Instead:

- put every figure in an `f:` marker, filled from the analysis on every run
  ("<!--f:n_above_2h-->four<!--/f--> of its <!--f:n_entries-->six<!--/f--> acts
  sit above two hours", the counts spelled out as `facts.py` renders them);
  a marker naming a fact that does not exist fails the build,
  which is the guarantee a hand-typed number does not get;
- generate superlatives from a ranking computed over all acts,
  so "the longest act in the game" can only appear where it is true,
  and a tie is stated as a tie;
- write down whatever claim the words still make
  ("marathon acts", "the chapter centrepiece", "by far the largest chapter")
  as an assertion over the analysis, evaluated before any file is written,
  failing the build with the sentence it guards.
  These claims are what is left guarding a figure that was typed in by hand,
  so write them for the numbers the words depend on as well.

The vocabulary for those assertions is in `scripts/assertions.py`;
the assertions themselves belong in the report's own `claims.py`.
Verification is the default and `--no-verify` is the escape hatch.
The test is: delete a video from an evidence file, re-run,
and the build should either fail or correct itself.

## Pitfalls that have already cost time

- Several jobs appending to one evidence file need a lock, as harvest.sh and
  topup.sh both do now. Without one the loss is silent: the file is still
  there, only shorter, and the medians it feeds move for no visible reason.
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
- A wiki writes its release dates in more than one format
  (`2024-07-04 10:00` next to `September 4th, 2025`),
  and the dates are sorted against each other to decide which acts are recent.
  `fetch_versions.py` normalises what it recognises;
  print the index and look at it before harvesting,
  because an unparsed date sorts after every real one
  and makes the wrong acts look new.
- A wiki may categorise the launch content under a beta version
  (Zenless Zone Zero's prologue is `Released in Version 0.13`, a 2022 closed test).
  That is what the wiki says, so publish it, and explain it in the caveats.
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
