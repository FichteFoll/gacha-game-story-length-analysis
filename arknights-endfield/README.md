# <!--f:game-->Arknights: Endfield<!--/f--> Main Missions: How Long Each Process Takes

Duration estimates for every process of the main mission storyline,
from the prologue on the surface of Talos-II
to Si's Painting,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->26 h 52 min<!--/f-->** (<!--f:n_report_entries-->13<!--/f--> entries counting the prologue, measured against <!--f:n_videos-->190<!--/f--> accepted uploads out of <!--f:n_candidates-->706<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->process<!--/f--> medians,
so treat it as an order of magnitude
rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Chapter I | Valley IV: The Hub, Valley Pass, Aburrey Quarry, Originium Science Park, Origin Lodespring and Power Plateau | 1.0 | 5 | 8 h 28 min | [01-chapter-i.md](01-chapter-i.md) |
| Chapter II | Wuling: Jingyu Valley, Qingbo Stockade, Wuling City, the North Wuling Exclusion Zone and Si's Painting | 1.0 - 1.6 | 8 | 18 h 24 min | [02-chapter-ii.md](02-chapter-ii.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->processes<!--/f-->

<!--gen:extremes-->
| | Process | Estimate |
| --- | --- | --- |
| longest | Chapter II, Process VII: Ruins in the Miasma | 4 h 34 min |
| longest | Chapter II, Process VIII: Sanctuary from the Rift | 3 h 14 min |
| longest | Chapter II, Process III: The Long Feud | 3 h 02 min |
| longest | Chapter I, Process I: The Broken Lands | 2 h 38 min |
| longest | Chapter I, Process III: Path of Ascension | 2 h 37 min |
| shortest | Chapter I, Prologue: Prologue | 28 min |
| shortest | Chapter I, Process II: The Turbid Heavens | 59 min |
| shortest | Chapter II, Process V: Wrothful Tide | 1 h 03 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Arknights: Endfield<!--/f-->:

- **Structure:** the chapters, the processes and the missions in each of them
come from the
[Mission/Main page](https://endfield.wiki.gg/wiki/Mission/Main)
and the individual mission pages of the Endfield Talos Wiki,
save for the newest process, which that page does not list yet
(see the limits below).
This is the one report here that does not read a Fandom wiki:
`endfield.fandom.com` exists, but its questline pages are empty placeholders.
- **Searches:** for every process, YouTube was searched four ways:
by chapter plus process number plus process name,
by process name alone,
and twice by the patch number recent uploads brand themselves with
instead of naming the process
("Arknights: Endfield 1.4 main story quest full walkthrough").
A second, independently worded set of queries was then run over every process
and the medians compared against the first
(the **Stability** line under each process below).
- **Compilations:** multi-process uploads,
which in this game means "Full Game", "all main missions",
and the many uploads covering a whole version's worth of story at once,
and which count only where their chapter markers
located this process inside them.
- **Partial uploads:** uploads covering part of a process rather than all of it,
which here means the numbered kind ("Part 3", "Ep 12", "1/2")
and the kind titled after one of the process's own missions,
unless their runtime says they cover the process after all.
- **Not a playthrough:** on top of the shared list,
this game's pool carries uploads marked "exploration only"
and VTuber VODs, both of which measure something other than the story.

The figures it screens and grades on:

<!--gen:thresholds-->
- Processes released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
- A marker set covering less than 60 percent
of a single-process upload is ignored,
as marking something other than the quest parts.
- Of the uploads that survive screening,
anything below half or above 1.8 times the median
is dropped as truncated or padded.
- From eight uploads on, the published range is the **middle half**
(the interquartile range), with the full spread alongside it;
below that it is the minimum and maximum.
- Confidence is *high* when the middle half spans a factor under 1.25
and *medium* under 1.5.
It is *low* on fewer than eight uploads,
and *low* for any process whose median moved by 10 percent or more
against the earlier, independent set of queries (`analyze.py --compare`),
whatever its sample size says.
- Processes resting on fewer than three uploads are published with their figures
but take no part in any ranking,
so none of them is called the longest or the shortest of anything.
<!--/gen-->

## Limits of this report

Beyond the limits every report in this repository shares,
listed in the [repository README](../README.md):

- The unit measured here is the **process**,
the level the game labels on screen
("Chapter II Process III: The Long Feud")
and the level its uploaders title their videos after.
A process is not a fixed size:
they run from three missions to ten,
and the estimates run accordingly.
- The two missions before Chapter I Process I
are a prologue in the game's own words
but carry no name on the wiki's mission table,
so they are one entry here, titled *Prologue*.
- No main mission on the wiki records a level requirement,
and the game gates story progress by story progress,
so this report has no gate column at all.
- Which processes a version shipped is not recorded per mission anywhere.
It is stated once per version, in prose, on that version's own page
("New Main Story up to Chapter II Process VI"),
and the **Released in** lines here are read off those sentences.
Versions 1.3 and 1.5 added no main story,
which is why no process is attributed to them.
- The whole game is younger than any other report in this repository.
Its oldest uploads are from January 2026
and its newest process shipped in October,
so every pool here is thinner than the equivalent elsewhere,
and the figures should be expected to move more on a re-harvest.
- Chapter I *The Turbid Heavens* contains the AIC factory tutorial,
which some uploaders play out in full and others hurry past.
Its uploads disagree accordingly,
and its confidence rating says so.
- Chapter II is still being released.
*Sanctuary from the Rift* (1.6) is the newest process at the time of writing,
and it shipped only days before collection,
so its pool is the youngest in the report,
made of first-week uploads,
and its figures are the most likely to move on a re-harvest.
It has no stability figure,
because it was added to the report
after the medians it would be compared against were taken.
- The wiki's mission table does not list *Sanctuary from the Rift* yet.
Its version page names the process only by its last mission,
"Chapter II Process VIII: Paint with Fresh Ink",
so the process title is the one the game shows and its uploads carry,
all but one of its missions are named on the wiki's event and pass pages,
and *Witness the Game Unfold* by uploads alone,
in the order the uploaders' chapter markers give.

Data collected <!--f:date-->2026-10-17<!--/f-->.
