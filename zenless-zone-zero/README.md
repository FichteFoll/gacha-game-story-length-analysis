# Zenless Zone Zero, Phaethon's Story: How Long Each Chapter Takes

Duration estimates for every chapter of the main story,
from the prologue on Sixth Street to the newest season in Roscaelifer,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: 71 h 02 min** (21 entries counting chapters, interludes and epilogues, measured against 271 accepted uploads out of 589 candidates).
That figure is the sum of the per-chapter medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Season 1 | New Eridu: Sixth Street, Lumina Square and the Outer Ring | 1.0 - 1.7 | 10 | 24 h 08 min | [01-season-1.md](01-season-1.md) |
| Season 2 | Waifei Peninsula: Yunkui Summit and Suibian Temple | 2.0 - 2.8 | 9 | 37 h 51 min | [02-season-2.md](02-season-2.md) |
| Season 3 | Roscaelifer | 3.0 - 3.1 | 2 | 9 h 03 min | [03-season-3.md](03-season-3.md) |

## Longest and shortest chapters

| | Chapter | Estimate |
| --- | --- | --- |
| longest | Season 2, Chapter 6: To Be Fuel for the Night | 6 h 49 min |
| longest | Season 2, Interlude: Encore for an Old Dream | 5 h 03 min |
| longest | Season 3, Chapter 1: A Sleepwalker's Confession | 4 h 34 min |
| longest | Season 2, Chapter 1: Where Clouds Embrace the Dawn | 4 h 31 min |
| longest | Season 3, Chapter 2: The Long Goodbye | 4 h 29 min |
| shortest | Season 1, Chapter 1 Intermission: The Zero Zone | 1 h 25 min |
| shortest | Season 1, Chapter 3: The Midnight Pursuit | 1 h 40 min |
| shortest | Season 1, Chapter 0: Business x Strangeness x Justness | 1 h 57 min |

## Method

1. **Structure from the wiki.**
The chapter and chapter list, the chapter titles, the quest parts come from the
[Phaethon's Story page](https://zenless-zone-zero.fandom.com/wiki/Phaethon's_Story)
and the individual chapter and chapter pages of the Zenless Zone Zero Wiki.
Fandom serves a Cloudflare challenge to plain HTTP clients,
so the pages were read through the MediaWiki API
(`/api.php?action=query&prop=revisions&rvprop=content`) instead.

2. **Durations from playthrough uploads.**
For every chapter, YouTube was searched four ways:
by season plus chapter number plus chapter title,
by chapter title alone,
and twice by the patch branding recent uploads use
instead of chapter titles
("Zenless Zone Zero 3.1 Season 3 Chapter 2 full quest gameplay").
Chapters released within the last four versions are searched twice as deep,
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

4. **Locating the chapter inside the upload.**
Where an uploader marked out their video with chapter markers,
the markers are matched against the chapter's quest parts,
its title and its number,
and the chapter is measured from those markers rather than from
the video's total runtime.
That drops the uploader's pre-roll and detours from the measurement,
turns an upload covering two chapters into evidence for each of them,
and, where enough uploads marked the same quest part,
gives that part its own median.
A marker set that covers less than 60 percent
of a single-chapter upload is ignored:
those markers were something other than the quest parts,
and trusting them would under-measure the chapter.

5. **Screening.**
A candidate is discarded when its title marks it as something other than
a hands-on playthrough of exactly that chapter:
cutscene reels, cinematic edits, lore explainers, guides and reaction videos;
livestreams and let's-plays, whose idle chatter inflates runtime;
multi-chapter compilations such as "Full Season 1 Story" or "all main stories",
unless their chapter markers located this chapter inside them;
uploads covering part of a chapter rather than all of it,
which in this game means the numbered kind
("Part 3", "Episode 4", "1/2"),
unless their runtime says they cover the chapter after all;
and uploads whose title does not name the chapter
either by name or by chapter plus chapter number.
Of the survivors, anything below half or above 1.8 times the median
is dropped as a truncated or padded upload.

6. **Estimate.**
The published figure is the **median** of the accepted uploads.
From eight uploads on, the published range is the **middle half**
(the interquartile range), with the full spread given alongside it:
one padded upload widens a min-max range that is otherwise tight,
and says more about that uploader than about the chapter.
Below eight uploads there is no distribution to speak of
and the range is the minimum and maximum.
Nothing is rated above *low* on fewer than eight uploads.
From there, confidence is *high*
when the middle half spans a factor under 1.25
and *medium* under 1.5.
Everything else is *low*,
as is any chapter whose median moved by 10 percent or more
against the earlier, independent set of queries
(`analyze.py --compare`):
a figure that moves when the queries change was never settled,
whatever its sample size says.

## What these numbers do and do not mean

- They measure **video runtime of someone playing the chapter**,
which is the closest available proxy for how long the chapter takes.
They are not official figures;
HoYoverse does not publish chapter lengths.
- Runtime includes the traversal, dialogue and combat
that a player cannot skip,
but it also includes whatever detours the uploader took,
and it excludes the time a first-time player spends
re-reading dialogue or dying to a boss.
Treat the median as a middle estimate and the range as the real spread.
- Uploaders play at different speeds,
skip cutscenes to different degrees,
and record on different game versions.
Chapters that were rebalanced or shortened after release
may be measured against older, longer uploads.
- Season 1 ships each chapter in two halves, (A) and (B),
released together and played back to back.
Almost nobody titles an upload after one half,
so a Season 1 figure here covers the whole chapter, both halves.
The two epilogues are the exception:
their halves shipped a version apart,
their uploads say which half they are,
and they are counted as two entries.
- Season 1 is the softest part of this report,
and its figures should be read as a range rather than as an estimate.
Dialogue is skippable in this game and a great deal of Season 1 is dialogue,
so the same chapter takes one uploader an hour and another three;
the pools are also the oldest and the thinnest,
and *A Call From the Hollow's Heart* in particular
rests on a handful of complete runs.
Where a median moved once the queries were widened,
the confidence rating says so.
- The game gates chapters behind Inter-Knot Level
and the Rank-Up commissions that raise Inter-Knot Reputation Rank,
but the wiki documents no level requirement per chapter,
so this report has no gate column.
What it does document is the other direction:
the Senior Proxy rank-up requires the Chapter 2 Interlude commission
*Invisible Assistant*.
- The prologue and Chapter 1 are categorized on the wiki
under version 0.13, the 2022 Tuning Test closed beta
in which they were first shown.
Players met them at the 1.0 release on 2024-07-04,
which is what the season's version range says instead.
- Chapter markers are rarer here than in any other game in this repository,
and where they exist they usually mark single steps
rather than the episodes a chapter is divided into.
Almost every figure in this report is therefore whole-video runtime,
not a span located inside a longer upload.
- Season 3 is still being released.
*The Long Goodbye* (3.1) is the newest chapter at the time of writing,
and there is nothing to measure beyond it yet.

## Files

- One markdown file per chapter, listed in the table above.
Each chapter section carries a collapsed evidence table
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
