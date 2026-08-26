# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A data pipeline plus its published output:
duration estimates for the story questlines of gacha games,
measured from YouTube playthrough uploads
because the publishers document no playtimes.
There is no application here and no test suite;
the deliverable is markdown, and the pipeline is what makes it reproducible.

One top-level directory per game report
(`genshin-impact/`, `honkai-star-rail/`, `zenless-zone-zero/`,
`arknights-endfield/` and `wuthering-waves/`),
each holding what is specific to that game and nothing else:
`README.md` plus one file per chapter, a `data/` vault,
`report.py` and `claims.py`.

The markdown files in a report directory are hand-written.
They carry the authored prose,
and HTML-comment placeholders where a derived figure or a derived block belongs;
`gen_docs.py` rewrites the contents of those placeholders in place
and leaves the rest of the file as it found it,
save for one normalisation it applies to the whole text:
every line is right-stripped and the file ends in exactly one newline,
so a two-space markdown hard line break does not survive a run.
`report.py` therefore holds configuration and structure only
(the wiki pages, the unit noun, the chapter metadata and the gates),
with no prose in it,
and `claims.py` holds the assertions guarding what the prose says in words.

The root `README.md` is hand-written and holds what the reports share:
the purpose, the links to them, the pipeline as prose,
the limits of the measurement and the vault layout.
It states no threshold, so that no number is maintained by hand;
a report's own `README.md` carries only what its game does differently,
plus the thresholds, which are filled into its `gen:thresholds` block
from the constants.
Anything that becomes true of every report belongs in the root README,
not copied into each of them.

Every script lives once, in the skill
`.claude/skills/questline-length-research/`,
whose `SKILL.md` is the authoritative procedure (steps 0 to 8) and pitfall list,
and whose `reference/games.md` holds the wiki host, questline page and level gate
of the games looked at so far.
Read `SKILL.md` before touching the pipeline:
it explains *why* each screening rule and confidence threshold exists.
Nothing in `scripts/` may become game-specific;
what a game differs in belongs in its `data/` or its `report.py`.

## Commands

All commands are run from a report directory
(`genshin-impact/`, `honkai-star-rail/`, `zenless-zone-zero/`,
`arknights-endfield/`, `wuthering-waves/`);
`<workdir>` is `data`.

```bash
SKILL=../.claude/skills/questline-length-research/scripts
python3 $SKILL/fetch_versions.py data                 # step 2, before harvesting
$SKILL/harvest.sh data [jobs] [--only <slug>,...]     # step 3, yt-dlp searches
$SKILL/enrich.sh data [jobs]                          # step 4, full extraction
python3 $SKILL/analyze.py data --compare data/baseline.json   # step 5, writes analysis.json
printf '<slug>|<query>\n' | $SKILL/topup.sh data [n]          # step 6, thin acts
python3 $SKILL/gen_docs.py .                          # step 8, fills the markdown
```

`analyze.py data --compare data/baseline.json` followed by `gen_docs.py .`
refills every marked region of every tracked markdown file
and reproduces its current contents byte for byte;
that round trip is the closest thing to a test suite here, so run it
after any pipeline change and check `git status` comes back clean.

`harvest.sh`, `enrich.sh` and `topup.sh` hit the network through `yt-dlp`
and take tens of minutes: background them.
All three are resumable (harvest skips acts that already have an evidence file,
enrich skips URLs already in `enriched.tsv`),
so an interrupted run is simply re-run.
YouTube starts answering "Sign in to confirm you're not a bot"
after a few hundred full extractions;
`analyze.py` falls back to the harvested figures, so do not fight it.
**Say so, and stop.** Tell the user the run hit the bot check
and how many URLs are still unenriched, and wait rather than retrying into it:
a retry that is merely slower still returns almost nothing.
There are two ways out and the choice is the user's.
A captcha solved in a browser lifts the block for a while, unpredictably —
it has been worth anything from six URLs to a couple of hundred,
and it has also lifted on its own after an hour.
Cookies are the durable fix, because the block is on the client:
set `YTDLP_COOKIES=<cookies.txt>` or `YTDLP_COOKIES_FROM_BROWSER=<browser>`
(see `scripts/yt_auth.sh`) and `harvest.sh`, `enrich.sh` and `topup.sh`
sign their requests in. Reading a browser's store only works where the browser
is, so from a sandbox that means an exported `cookies.txt` bound in,
or the user running the script themselves.
Either way, finish with `analyze.py` and `gen_docs.py`
to fold the new markers in.

`gen_docs.py --no-verify` fills the files despite failing claims,
for inspection only.
`gen_docs.py --scaffold` adds the stub sections
for a chapter of `report.CHAPTERS` that has no markdown file,
and for an act of `analysis.json` that its chapter's file does not cover;
without it, such a gap fails the build and names the chapter or the act.

## Architecture

Data flows in one direction, each stage writing a file the next one reads:

```
wiki (MediaWiki API, per data/wiki.json)
    -> acts.tsv, quest_parts.json, versions.json, version_index.json
queries.py (templates x act) -> harvest.sh -> data/evidence/<chapter>_<act>.tsv
analyze.py (screening) -> analysis.json -> enrich.sh -> enriched.tsv -> analyze.py again
analysis.json -> facts.py / assertions.py + the report's report.py and claims.py
    -> gen_docs.py -> the marked regions of the authored *.md
```

`analyze.py` runs twice by design: the first pass decides which candidates
are worth a full extraction, the second folds `enriched.tsv` back in
so acts can be measured from the uploader's chapter markers
rather than from whole-video runtime.

Generic, in the skill's `scripts/`, parameterised by `<workdir>` or `<report>`:
`fetch_versions.py`, `queries.py`, `harvest.sh`, `enrich.sh`, `topup.sh`,
`yt_auth.sh` (the cookie flags those three share),
`analyze.py`, `facts.py` (quantities derived from `analysis.json`),
`assertions.py` (the vocabulary claims are written in)
and `gen_docs.py` (the filler for the marked regions).

Report-specific: the authored `README.md` and chapter files,
`data/` (`wiki.json`, `game.txt`, `acts.tsv`,
`chapter_keys.json`, `act_keys.json`, `not_playthrough.txt`,
`compilations.txt`, `partials.txt`, `min_minutes.txt`,
`query_templates.txt`),
`report.py` (the game's configuration and structure)
and `claims.py` (the assertions guarding the prose).

A second game is therefore a new report directory,
never a change to a script.
What games disagree about is already parameterised:
the wiki and its version infobox (`data/wiki.json`),
the word acts are numbered with (read off the labels in `acts.tsv`),
what an upload titled as less than one act looks like (`data/partials.txt`),
what tells two same-named acts apart (`data/act_keys.json`),
the level gate's name, and the three nouns the renderer writes with:
the unit an entry is (`unit`), the group of entries one file covers
(`container`) and what the group's second column holds (`region_label`),
which is a region for four of the games and the part of the narrative
for Honkai Impact 3rd, whose entry is itself a chapter
(`report.py`, which also records the questline page
that the authored markdown links by hand).

### The prose must not contain hand-written numbers

This is the invariant the whole reporting half exists to protect,
and since the prose moved into the markdown
it is no longer enforced by `gen_docs.py` alone.
What `gen_docs.py` still guarantees is narrow:
a figure that sits inside an `f:` marker cannot go stale,
because it is rewritten from `analysis.json` on every run,
and a marker naming something `facts.py` does not compute
fails the build with the file and the marker name
rather than leaving a stale figure standing.
A figure typed straight into a sentence, outside any marker,
is now possible, and is caught only by the claims in `claims.py`.
So the invariant holds by convention plus `claims.py`:
put every number in a marker, and guard in words what words assert.

Superlatives come from a ranking computed over all acts, so
"the longest act in the game" can only appear where it is true.
Claims the prose makes in *words* ("marathon acts", "the chapter centrepiece")
are written down in the report's `claims.py` next to the sentence they guard,
and `gen_docs.py` evaluates all of them before writing a single file:
a claim that no longer holds fails the build and names the sentence to fix.
When editing prose, add or adjust the guarding claim in the same change.

### The marker grammar

Two forms, both HTML comments, so they are invisible in a rendered page:

- an inline value, `<!--f:NAME-->2 h 10 min<!--/f-->`,
  with both markers on the same line, never nested inside another `f:` marker,
  and the value between them replaced on every run.
  `NAME` is a key of the fact mapping for the file's scope:
  `report_facts()` for a report `README.md`,
  that merged with `chapter_facts()` for a chapter file.
- a generated block,
  `<!--gen:KIND[ attr="value" ...]-->` ... `<!--/gen-->`,
  each marker on a line of its own,
  with everything between them replaced on every run.
  The kinds are `chapters`, `extremes` and `thresholds` in a report `README.md`,
  and `heading`, `glance`, `act-heading`, `stats` and `evidence`
  in a chapter file;
  the three per-act kinds take an `act="<label>"` attribute.
  The label alone identifies the act,
  because the chapter id follows from which file the region sits in
  (`report.CHAPTERS` maps `slug` to `id`).

A `gen:` block belongs outside any paragraph,
with a blank line before its opening and after its closing marker:
a line holding only an HTML comment starts an HTML block in CommonMark
and would split the paragraph in two,
changing the rendered result even though the source text survives.
The reports break that rule in one place, knowingly:
a `gen:stats` opener follows the act note's last line directly,
because the region starts at the derived superlative sentence,
which belongs to the note's paragraph.
Giving it its own blank line would change the published source,
so the paragraph break in the rendered page is accepted instead.
A value inside a sentence therefore uses the inline `f:` form only,
and an `f:` marker never spans a line break.
An unknown `NAME` or `KIND`, or an unterminated marker,
is an error naming the file and the marker, not a silent pass.

### Statistics conventions

The published estimate is always the **median**, never a single runtime.
From eight uploads on the published range is the interquartile range,
with the full spread alongside; below eight it is min to max.
Nothing rates above *low* confidence on fewer than eight uploads;
then *high* under a 1.25 interquartile factor and *medium* under 1.5.
An act whose median moved 10 percent or more against `data/baseline.json`
is *low* by definition, whatever its sample size.
The sample floor and the drift limit are `IQR_SAMPLES` and `UNSTABLE_DRIFT`
in `analyze.py`, which `gen_docs.py` imports rather than restates;
only the two interquartile factors (`SPREAD_HIGH`, `SPREAD_MEDIUM`)
live in `gen_docs.py`, because nothing else grades on them.
The published method section quotes all four from the constants themselves,
so a changed threshold rewrites its own description.

## Conventions

- The authored markdown and the generated blocks use semantic line breaks
  (one clause per line, breaking after periods and commas and before conjunctions).
  `gen_docs.py` rewrites only the marked regions,
  so the breaks in the authored markdown survive as written.
- Python 3.14, standard library only. `yt-dlp` is the sole external tool.
- Say plainly what the numbers are: video runtime of someone else playing,
  as a proxy for act length. Not official, includes the uploader's detours,
  excludes a first-timer's re-reading and deaths.
