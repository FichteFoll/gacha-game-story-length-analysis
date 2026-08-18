# Genshin Impact Archon Questline: How Long Each Act Takes

Duration estimates for every main act of the Archon Quest storyline,
from the Mondstadt Prologue to Chapter VII,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: 112 h 26 min** (45 entries counting acts, preludes and interludes, measured against 489 accepted uploads out of 698 candidates).
That figure is the sum of the per-act medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Prologue: The Outlander Who Caught the Wind | Mondstadt | 1.0 | 3 | 2 h 53 min | [00-prologue-mondstadt.md](00-prologue-mondstadt.md) |
| Chapter I: Farewell, Archaic Lord | Liyue | 1.0 - 1.4 | 5 | 6 h 42 min | [01-chapter-i-liyue.md](01-chapter-i-liyue.md) |
| Chapter II: Omnipresence Over Mortals | Inazuma | 1.6 - 2.6 | 5 | 8 h 12 min | [02-chapter-ii-inazuma.md](02-chapter-ii-inazuma.md) |
| Chapter III: Truth Amongst the Pages of Purana | Sumeru | 3.0 - 3.5 | 6 | 16 h 04 min | [03-chapter-iii-sumeru.md](03-chapter-iii-sumeru.md) |
| Chapter IV: Masquerade of the Guilty | Fontaine | 4.0 - 4.7 | 6 | 17 h 16 min | [04-chapter-iv-fontaine.md](04-chapter-iv-fontaine.md) |
| Chapter V: Incandescent Ode of Resurrection | Natlan | 5.0 - 5.7 | 7 | 17 h 28 min | [05-chapter-v-natlan.md](05-chapter-v-natlan.md) |
| Song of the Welkin Moon (unofficially Chapter VI) | Nod-Krai, later Sumeru | 5.8 - Luna VII (6.x) | 11 | 35 h 22 min | [06-song-of-the-welkin-moon-nod-krai.md](06-song-of-the-welkin-moon-nod-krai.md) |
| Chapter VII: Everwinter Without Mercy | Snezhnaya | 7.0 | 2 | 8 h 29 min | [07-chapter-vii-snezhnaya.md](07-chapter-vii-snezhnaya.md) |

## Longest and shortest acts

| | Act | Estimate |
| --- | --- | --- |
| longest | Chapter IV, Act V: Masquerade of the Guilty | 4 h 50 min |
| longest | Song of the Welkin Moon, Act I: A Dance of Snowy Tides and Hoarfrost Groves | 4 h 43 min |
| longest | Chapter VII, Act II: Wraith's Nocturne | 4 h 27 min |
| longest | Chapter III, Act V: Akasha Pulses, the Kalpa Flame Rises | 4 h 27 min |
| longest | Chapter VII, Act I: Everwinter Without Mercy | 4 h 02 min |
| shortest | Chapter I, Act IV - Prelude: Bough Keeper: Dainsleif | 36 min |
| shortest | Chapter II, Act II: Stillness, the Sublimation of Shadow | 50 min |
| shortest | Prologue, Act I: The Outlander Who Caught the Wind | 52 min |

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
For every act, YouTube was searched four ways:
by chapter plus act label plus act title, by act title alone,
and twice by the patch branding recent uploads use instead of act titles
("Genshin Impact 6.6 Act 10 ...").
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
multi-act compilations such as "Acts 9 & 10" or "Full Sumeru Archon Quest",
unless their chapter markers located this act inside them;
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
`data/query_templates.txt` and `data/compilations.txt`
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
