# Genshin Impact Archon Questline: How Long Each Act Takes

Duration estimates for every main act of the Archon Quest storyline,
from the Mondstadt Prologue to Chapter VII,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: 112 h 37 min** (45 entries counting acts, preludes and interludes, measured against 449 accepted uploads out of 672 candidates).
That figure is the sum of the per-act medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Prologue: The Outlander Who Caught the Wind | Mondstadt | 1.0 | 3 | 3 h 07 min | [00-prologue-mondstadt.md](00-prologue-mondstadt.md) |
| Chapter I: Farewell, Archaic Lord | Liyue | 1.0 - 1.4 | 5 | 6 h 46 min | [01-chapter-i-liyue.md](01-chapter-i-liyue.md) |
| Chapter II: Omnipresence Over Mortals | Inazuma | 1.6 - 2.6 | 5 | 8 h 11 min | [02-chapter-ii-inazuma.md](02-chapter-ii-inazuma.md) |
| Chapter III: Truth Amongst the Pages of Purana | Sumeru | 3.0 - 3.5 | 6 | 16 h 02 min | [03-chapter-iii-sumeru.md](03-chapter-iii-sumeru.md) |
| Chapter IV: Masquerade of the Guilty | Fontaine | 4.0 - 4.7 | 6 | 17 h 15 min | [04-chapter-iv-fontaine.md](04-chapter-iv-fontaine.md) |
| Chapter V: Incandescent Ode of Resurrection | Natlan | 5.0 - 5.7 | 7 | 17 h 26 min | [05-chapter-v-natlan.md](05-chapter-v-natlan.md) |
| Song of the Welkin Moon (unofficially Chapter VI) | Nod-Krai, later Sumeru | 5.8 - Luna VII (6.x) | 11 | 35 h 23 min | [06-song-of-the-welkin-moon-nod-krai.md](06-song-of-the-welkin-moon-nod-krai.md) |
| Chapter VII: Everwinter Without Mercy | Snezhnaya | 7.0 | 2 | 8 h 27 min | [07-chapter-vii-snezhnaya.md](07-chapter-vii-snezhnaya.md) |

## Longest and shortest acts

| | Act | Estimate |
| --- | --- | --- |
| longest | Chapter IV, Act V: Masquerade of the Guilty | 4 h 50 min |
| longest | Song of the Welkin Moon, Act I: A Dance of Snowy Tides and Hoarfrost Groves | 4 h 43 min |
| longest | Chapter III, Act V: Akasha Pulses, the Kalpa Flame Rises | 4 h 31 min |
| longest | Chapter VII, Act II: Wraith's Nocturne | 4 h 25 min |
| longest | Song of the Welkin Moon, Act IV: An Elegy for Faded Moonlight | 4 h 03 min |
| shortest | Chapter I, Act IV - Prelude: Bough Keeper: Dainsleif | 37 min |
| shortest | Chapter II, Act II: Stillness, the Sublimation of Shadow | 50 min |
| shortest | Chapter V, Interlude: All Fires Fuel the Flame | 50 min |

## Method

1. **Structure from the wiki.**
The chapter and act list, the act titles, the quest parts
and the Adventure Rank gates come from the
[Archon Quest page](https://genshin-impact.fandom.com/wiki/Archon_Quest)
and the individual chapter and act pages of the Genshin Impact Wiki.
Fandom serves a Cloudflare challenge to plain HTTP clients,
so the pages were read through the MediaWiki API
(`/api.php?action=query&prop=revisions&rvprop=content`) instead.

2. **Durations from playthrough uploads.**
For every act, YouTube was searched twice
(once by chapter plus act label plus act title, once by act title alone)
and the top results were collected with their runtime, title, uploader,
view count and URL.
Acts with a thin result pool got a third, region-specific query.

3. **Screening.**
A candidate is discarded when its title marks it as something other than
a hands-on playthrough of exactly that act:
cutscene reels, cinematic edits, lore explainers, guides and reaction videos;
livestreams and let's-plays, whose idle chatter inflates runtime;
multi-act compilations such as "Acts 9 & 10" or "Full Sumeru Archon Quest";
and uploads whose title does not name the act
either by name or by chapter plus act number.
Of the survivors, anything below half or above 1.8 times the median
is dropped as a truncated or padded upload.

4. **Estimate.**
The published figure is the **median** of the accepted uploads,
and the range is their minimum and maximum.
Confidence is *high* at eight or more uploads spanning a factor under 1.6,
*medium* at six or more spanning a factor under 2.2,
and *low* otherwise.

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
- The newest acts (Nod-Krai's later acts, Chapter VII)
have the fewest uploads to draw on,
so their figures are the softest.
They are marked *low* or *medium* confidence accordingly.
- Interlude Chapter acts
(*The Crane Returns on the Wind*, *Perilous Trail*,
*Inversion of Genesis*, *Paralogism*)
are Archon Quests but not part of the main chapter progression,
so they are outside this report's scope.

## Files

- One markdown file per chapter, listed in the table above.
Each act section carries a collapsed evidence table
with runtime, video title, uploader, view count and URL
for every accepted upload.
- `data/analysis.json` holds the same evidence in machine-readable form,
including the rejected candidates and the reason each was rejected.
- `data/acts.tsv` is the act list extracted from the wiki.
- `data/evidence/` holds the raw harvest, one file per act,
before any screening was applied.
- `data/versions.json` maps each act to its release version,
as categorized on the wiki,
and `data/version_index.json` gives each version
its patch number and release date.
Both are fetched by `pipeline/fetch_versions.py` before the harvest,
because the harvest searches for version-branded upload titles.
- `data/quest_parts.json` lists the quest parts of each act,
in the order the wiki gives them.
- `data/chapter_keys.json` and `data/compilations.txt`
are the screening inputs described under Method.
- `pipeline/` holds the scripts that produced all of this:
`harvest.sh` collects the candidates,
`topup.sh` widens a thin act's pool,
`analyze.py` screens them and computes the statistics,
and `gen_docs.py` renders these markdown files from `analysis.json`.
Re-running `analyze.py` over the harvested evidence
reproduces `data/analysis.json` exactly.
- Every figure in the prose is interpolated from `analysis.json`
by `pipeline/facts.py` rather than written by hand,
and the claims the prose makes in words
are asserted in `pipeline/claims.py` before any file is written.
A claim that no longer holds fails the build.

Data collected 2026-08-18.
