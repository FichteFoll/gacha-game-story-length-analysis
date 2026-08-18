# Honkai: Star Rail Trailblaze Missions: How Long Each Mission Takes

Duration estimates for every Trailblaze Mission of the main storyline,
from the Herta Space Station to Planarcadia,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: 118 h 11 min** (24 entries counting missions, measured against 244 accepted uploads out of 652 candidates).
That figure is the sum of the per-act medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Herta Space Station | Herta Space Station | 1.0 | 1 | 2 h 19 min | [00-herta-space-station.md](00-herta-space-station.md) |
| Jarilo-VI | Jarilo-VI: Belobog and the Underworld | 1.0 | 2 | 6 h 32 min | [01-jarilo-vi.md](01-jarilo-vi.md) |
| The Xianzhou Luofu | The Xianzhou Luofu | 1.0 - 1.3 | 3 | 6 h 37 min | [02-xianzhou-luofu.md](02-xianzhou-luofu.md) |
| Penacony | Penacony, the Land of Dreams | 2.0 - 2.7 | 5 | 22 h 46 min | [03-penacony.md](03-penacony.md) |
| Amphoreus | Amphoreus, the Eternal Land | 3.0 - 3.7 | 8 | 52 h 14 min | [04-amphoreus.md](04-amphoreus.md) |
| Planarcadia | Planarcadia | 4.0 - 4.4 | 5 | 27 h 43 min | [05-planarcadia.md](05-planarcadia.md) |

## Longest and shortest missions

| | Mission | Estimate |
| --- | --- | --- |
| longest | Amphoreus, Mission 1: Heroic Saga of Flame-Chase | 8 h 20 min |
| longest | Planarcadia, Mission 1: Welcome to Arcadia | 8 h 01 min |
| longest | Penacony, Mission 3: In Our Time | 7 h 46 min |
| longest | Amphoreus, Mission 3: Through the Petals in the Land of Repose | 7 h 40 min |
| longest | Amphoreus, Mission 4: The Fall at Dawn's Rise | 7 h 20 min |
| shortest | The Xianzhou Luofu, Mission 3: Karmic Clouds Faded, War Banners Folded | 1 h 16 min |
| shortest | The Xianzhou Luofu, Mission 2: Topclouded Towerthrust | 2 h 00 min |
| shortest | Herta Space Station, Mission 1: Today Is Yesterday's Tomorrow | 2 h 19 min |

## Method

1. **Structure from the wiki.**
The chapter and act list, the act titles, the quest parts
and the Level gates come from the
[Trailblaze Mission page](https://honkai-star-rail.fandom.com/wiki/Trailblaze_Mission)
and the individual chapter and act pages of the Honkai: Star Rail Wiki.
Fandom serves a Cloudflare challenge to plain HTTP clients,
so the pages were read through the MediaWiki API
(`/api.php?action=query&prop=revisions&rvprop=content`) instead.

2. **Durations from playthrough uploads.**
For every mission, YouTube was searched four ways:
by world plus mission title, by mission title alone,
and twice by the patch branding recent uploads use instead of mission titles
("Honkai: Star Rail 4.4 Planarcadia Trailblaze Mission Walkthrough").
Acts released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
Each result was collected with its runtime, title, uploader,
view count and URL.

3. **A second pass over the candidates worth measuring.**
The search listing gives rounded view counts and no upload date,
so every candidate that was not discarded outright
is fetched again in full.
That yields exact view counts and upload dates,
and the uploader's own chapter markers.
YouTube rate-limits these requests,
so the pass covers as many as it manages
and the rest keep their figures from the search listing.

4. **Locating the act inside the upload.**
Where an uploader marked out their video with chapter markers,
the markers are matched against the act's quest parts,
its title and its number,
and the act is measured from those markers rather than from
the video's total runtime.
That drops the uploader's pre-roll and detours from the measurement,
turns an upload covering two acts into evidence for each of them,
and, where enough uploads marked the same quest part,
gives that part its own median.
A marker set that covers less than 60 percent
of a single-act upload is ignored:
those markers were something other than the quest parts,
and trusting them would under-measure the act.

5. **Screening.**
A candidate is discarded when its title marks it as something other than
a hands-on playthrough of exactly that act:
cutscene reels, cinematic edits, lore explainers, guides and reaction videos;
livestreams and let's-plays, whose idle chatter inflates runtime;
multi-act compilations such as "Full Amphoreus Trailblaze Quest" or "100% all missions",
unless their chapter markers located this act inside them;
uploads covering part of a mission rather than all of it,
which in this game means both the numbered kind ("Part 3")
and the kind titled after a single quest part of the mission,
unless their runtime says they cover the mission after all;
and uploads whose title does not name the act
either by name or by chapter plus act number.
Of the survivors, anything below half or above 1.8 times the median
is dropped as a truncated or padded upload.

6. **Estimate.**
The published figure is the **median** of the accepted uploads.
From eight uploads on, the published range is the **middle half**
(the interquartile range), with the full spread given alongside it:
one padded upload widens a min-max range that is otherwise tight,
and says more about that uploader than about the act.
Below eight uploads there is no distribution to speak of
and the range is the minimum and maximum.
Nothing is rated above *low* on fewer than eight uploads.
From there, confidence is *high*
when the middle half spans a factor under 1.25
and *medium* under 1.5.
Everything else is *low*,
as is any act whose median moved by 10 percent or more
against the earlier, independent set of queries
(`analyze.py --compare`):
a figure that moves when the queries change was never settled,
whatever its sample size says.

## What these numbers do and do not mean

- They measure **video runtime of someone playing the act**,
which is the closest available proxy for how long the act takes.
They are not official figures;
HoYoverse does not publish act lengths.
- Runtime includes the traversal, dialogue and combat
that a player cannot skip,
but it also includes whatever detours the uploader took,
and it excludes the time a first-time player spends
re-reading dialogue or dying to a boss.
Treat the median as a middle estimate and the range as the real spread.
- Uploaders play at different speeds,
skip cutscenes to different degrees,
and record on different game versions.
Acts that were rebalanced or shortened after release
may be measured against older, longer uploads.
- The 1.0 missions are the hardest of all to measure.
The uploads that exist are the oldest on YouTube,
and the convention then was to cut a mission into scene-length videos,
so *In the Withering Wintry Night* in particular
rests on a small pool of genuinely complete runs.
- Planarcadia is the newest content sampled.
Walkthrough channels covered it thoroughly,
so the pools are not thin,
but they have had the least time to settle,
and the accepted uploads of its opening mission
still disagree by a factor of two.
- Astropolis and its mission *To Roll the Stars in Astropolis*
are still upcoming content at the time of writing (Version 4.5),
so there is nothing to measure yet.
- *Memories are the Prelude to Dreams* is a Finality Mission:
supplemental Penacony story released long after the world was finished.
The Trial of Equilibrium missions are level-cap trials
rather than story.
Neither is part of the main progression,
so both are outside this report's scope.

## Files

- One markdown file per chapter, listed in the table above.
Each act section carries a collapsed evidence table
with runtime, video title, uploader, view count, upload date and URL
for every accepted upload.
A view count prefixed with `~` came from the search listing
and is rounded; the rest are exact.
- `data/analysis.json` holds the same evidence in machine-readable form,
including the rejected candidates and the reason each was rejected.
- `data/acts.tsv` is the act list extracted from the wiki.
- `data/evidence/` holds the raw harvest, one file per act,
before any screening was applied.
- `data/versions.json` maps each act to its release version,
as categorized on the wiki,
and `data/version_index.json` gives each version
its patch number and release date.
Both are fetched by `fetch_versions.py` before the harvest,
because the harvest searches for version-branded upload titles.
- `data/quest_parts.json` lists the quest parts of each act,
in the order the wiki gives them.
- `data/wiki.json`, `data/game.txt`, `data/chapter_keys.json`,
`data/query_templates.txt`, `data/compilations.txt`
and `data/partials.txt`
are the inputs the pipeline is steered with, described under Method.
- The scripts themselves live in the `questline-length-research` skill
(`.claude/skills/questline-length-research/scripts/`),
shared by every report in this repository:
`harvest.sh` collects the candidates,
`topup.sh` widens a thin act's pool,
`analyze.py` screens them and computes the statistics,
`enrich.sh` fetches exact metadata and chapter markers for the survivors,
and `gen_docs.py` renders these markdown files from `analysis.json`.
Re-running
`analyze.py data --compare data/baseline.json`
over the harvested evidence reproduces `data/analysis.json` exactly.
- `data/baseline.json` holds the per-act medians
from the first, independent set of queries,
which is what the stability figure is measured against.
- Every figure in the prose is interpolated from `analysis.json`
rather than written by hand,
and the claims the prose makes in words
are asserted in `claims.py` before any file is written.
A claim that no longer holds fails the build.

Data collected 2026-08-18.
