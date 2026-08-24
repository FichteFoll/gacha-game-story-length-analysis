# <!--f:game-->Arknights: Endfield<!--/f--> Main Missions: How Long Each Process Takes

Duration estimates for every process of the main mission storyline,
from the prologue on the surface of Talos-II
to the Wuling Very Large Rift,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->23 h 38 min<!--/f-->** (<!--f:n_report_entries-->12<!--/f--> entries counting the prologue, measured against <!--f:n_videos-->158<!--/f--> accepted uploads out of <!--f:n_candidates-->512<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->process<!--/f--> medians,
so treat it as an order of magnitude
rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Chapter I | Valley IV: The Hub, Valley Pass, Aburrey Quarry, Originium Science Park, Origin Lodespring and Power Plateau | 1.0 | 5 | 8 h 28 min | [01-chapter-i.md](01-chapter-i.md) |
| Chapter II | Wuling: Jingyu Valley, Qingbo Stockade, Wuling City and the North Wuling Exclusion Zone | 1.0 - 1.4 | 7 | 15 h 10 min | [02-chapter-ii.md](02-chapter-ii.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->processes<!--/f-->

<!--gen:extremes-->
| | Process | Estimate |
| --- | --- | --- |
| longest | Chapter II, Process VII: Ruins in the Miasma | 4 h 34 min |
| longest | Chapter II, Process III: The Long Feud | 3 h 02 min |
| longest | Chapter I, Process I: The Broken Lands | 2 h 38 min |
| longest | Chapter I, Process III: Path of Ascension | 2 h 37 min |
| longest | Chapter II, Process II: The Way of Water | 1 h 50 min |
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
and the individual mission pages of the Endfield Talos Wiki.
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
and the **Released in** lines here are read off those five sentences.
Version 1.3 added no main story,
which is why no process is attributed to it.
- The whole game is younger than any other report in this repository.
Its oldest uploads are from January 2026
and its newest process shipped in July,
so every pool here is thinner than the equivalent elsewhere,
and the figures should be expected to move more on a re-harvest.
- Chapter I *The Turbid Heavens* contains the AIC factory tutorial,
which some uploaders play out in full and others hurry past.
Its uploads disagree accordingly,
and its confidence rating says so.
- Chapter II is still being released.
*Ruins in the Miasma* (1.4) is the newest process at the time of writing,
and there is nothing to measure beyond it yet.

Data collected <!--f:date-->2026-08-24<!--/f-->.
