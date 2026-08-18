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
(`genshin-impact/`, `honkai-star-rail/` and `zenless-zone-zero/`),
each holding what is specific to that game and nothing else:
`README.md` plus one file per chapter, a `data/` vault,
`report.py` (configuration and authored prose) and `claims.py`.

The root `README.md` is hand-written and holds what the reports share:
the purpose, the links to them, the pipeline as prose,
the limits of the measurement and the vault layout.
It states no threshold, so that no number is maintained by hand;
a report's own `README.md` carries only what its game does differently,
plus the thresholds, which are interpolated from the constants.
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
(`genshin-impact/`, `honkai-star-rail/`, `zenless-zone-zero/`);
`<workdir>` is `data`.

```bash
SKILL=../.claude/skills/questline-length-research/scripts
python3 $SKILL/fetch_versions.py data                 # step 2, before harvesting
$SKILL/harvest.sh data [jobs] [--only <slug>,...]     # step 3, yt-dlp searches
$SKILL/enrich.sh data [jobs]                          # step 4, full extraction
python3 $SKILL/analyze.py data --compare data/baseline.json   # step 5, writes analysis.json
printf '<slug>|<query>\n' | $SKILL/topup.sh data [n]          # step 6, thin acts
python3 $SKILL/gen_docs.py .                          # step 8, renders the markdown
```

`analyze.py data --compare data/baseline.json` followed by `gen_docs.py .`
reproduces every tracked file byte for byte;
that round trip is the closest thing to a test suite here, so run it
after any pipeline change and check `git status` comes back clean.

`harvest.sh`, `enrich.sh` and `topup.sh` hit the network through `yt-dlp`
and take tens of minutes: background them.
All three are resumable (harvest skips acts that already have an evidence file,
enrich skips URLs already in `enriched.tsv`),
so an interrupted run is simply re-run.
YouTube starts answering "Sign in to confirm you're not a bot"
after a few hundred full extractions;
`analyze.py` falls back to the harvested figures, so retry later rather than fighting it.

`gen_docs.py --no-verify` renders despite failing claims, for inspection only.

## Architecture

Data flows in one direction, each stage writing a file the next one reads:

```
wiki (MediaWiki API, per data/wiki.json)
    -> acts.tsv, quest_parts.json, versions.json, version_index.json
queries.py (templates x act) -> harvest.sh -> data/evidence/<chapter>_<act>.tsv
analyze.py (screening) -> analysis.json -> enrich.sh -> enriched.tsv -> analyze.py again
analysis.json -> facts.py / assertions.py + the report's report.py and claims.py
    -> gen_docs.py -> *.md
```

`analyze.py` runs twice by design: the first pass decides which candidates
are worth a full extraction, the second folds `enriched.tsv` back in
so acts can be measured from the uploader's chapter markers
rather than from whole-video runtime.

Generic, in the skill's `scripts/`, parameterised by `<workdir>` or `<report>`:
`fetch_versions.py`, `queries.py`, `harvest.sh`, `enrich.sh`, `topup.sh`,
`analyze.py`, `facts.py` (quantities derived from `analysis.json`),
`assertions.py` (the vocabulary claims are written in)
and `gen_docs.py` (layout).

Report-specific: `data/` (`wiki.json`, `game.txt`, `acts.tsv`,
`chapter_keys.json`, `act_keys.json`, `compilations.txt`, `partials.txt`,
`query_templates.txt`),
`report.py` (the game's configuration and the authored prose)
and `claims.py` (the assertions guarding that prose).

A second game is therefore a new report directory,
never a change to a script.
What games disagree about is already parameterised:
the wiki and its version infobox (`data/wiki.json`),
the word acts are numbered with (read off the labels in `acts.tsv`),
what an upload titled as less than one act looks like (`data/partials.txt`),
what tells two same-named acts apart (`data/act_keys.json`),
the level gate's name, the questline page and the renderer's nouns
(`report.py`).

### The prose must not contain hand-written numbers

This is the invariant the whole reporting half exists to protect.
The prose in `report.py` carries placeholders (`{len_Act_II}`, `{n_entries}`),
filled from `facts.py` at render time; an unknown placeholder raises `KeyError`
rather than rendering a stale figure.
Superlatives come from a ranking computed over all acts, so
"the longest act in the game" can only appear where it is true.
Claims the prose makes in *words* ("marathon acts", "the chapter centrepiece")
are written down in the report's `claims.py` next to the sentence they guard,
and `gen_docs.py` evaluates all of them before writing a single file:
a claim that no longer holds fails the build and names the sentence to fix.
When editing prose, add or adjust the guarding claim in the same change.

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

- Markdown and generated prose use semantic line breaks
  (one clause per line, breaking after periods and commas and before conjunctions).
  `gen_docs.py` preserves the authored breaks, so keep them in `report.py`.
- Python 3.14, standard library only. `yt-dlp` is the sole external tool.
- Say plainly what the numbers are: video runtime of someone else playing,
  as a proxy for act length. Not official, includes the uploader's detours,
  excludes a first-timer's re-reading and deaths.
