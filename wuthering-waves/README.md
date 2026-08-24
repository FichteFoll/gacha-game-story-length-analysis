# <!--f:game-->Wuthering Waves<!--/f--> Main Questline: How Long Each Act Takes

Duration estimates for every entry of the Main Quest storyline,
from the Huanglong prologue to Mengzhou,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->86 h 05 min<!--/f-->** (<!--f:n_report_entries-->47<!--/f--> entries counting acts, prologues, interludes and segues, measured against <!--f:n_videos-->626<!--/f--> accepted uploads out of <!--f:n_candidates-->1203<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->act<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Prologue: Utterance of Marvels | Huanglong | 1.0 | 2 | 51 min | [00-prologue.md](00-prologue.md) |
| Chapter I: Jinzhou Rising | Huanglong, later the Black Shores | 1.0 - 1.3 | 9 | 11 h 38 min | [01-chapter-i-jinzhou.md](01-chapter-i-jinzhou.md) |
| Chapter II: Even When Divinity Remains Silent | Rinascita | 2.0 - 2.8 | 17 | 36 h 27 min | [02-chapter-ii-rinascita.md](02-chapter-ii-rinascita.md) |
| Chapter III: To the Stars Yet to Shine | Roya Frostlands, Lahai-Roi | 3.0 - 3.4 | 14 | 26 h 31 min | [03-chapter-iii-roya-frostlands.md](03-chapter-iii-roya-frostlands.md) |
| Chapter IV: Rebirth From the Depths | Mengzhou | 3.5 - 3.6 | 5 | 10 h 38 min | [04-chapter-iv-mengzhou.md](04-chapter-iv-mengzhou.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->acts<!--/f-->

<!--gen:extremes-->
| | Act | Estimate |
| --- | --- | --- |
| longest | Chapter IV, Act III: Song of the Heart Sword | 4 h 38 min |
| longest | Chapter II, Act XI: Dawn Breaks on Dark Tides | 4 h 23 min |
| longest | Chapter III, Act III: The Star That Voyages Far | 3 h 59 min |
| longest | Chapter II, Act VIII: By Sun's Burning Hand | 3 h 28 min |
| longest | Chapter III, Act IV: Gold Suspended in Shadows | 3 h 24 min |
| shortest | Chapter III, Segue - III: The Flaming Red from Tomorrow | 7 min |
| shortest | Chapter III, Segue - V: Wishes in the Bell: Epilogue | 14 min |
| shortest | Prologue, Prologue II: Utterance of Marvels: II | 15 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Wuthering Waves<!--/f-->:

- **Structure:** the chapter and act list, the act titles, the quest parts
and the Union Level gates come from the
[Main Quest page](https://wutheringwaves.fandom.com/wiki/Main_Quest)
and the individual chapter and act pages of the Wuthering Waves Wiki.
- **Searches:** for every entry, YouTube was searched five ways:
by chapter plus act label plus act title, by act title alone,
by act title with the game name,
and twice by the patch branding recent uploads use instead of act titles
("Wuthering Waves 3.5 Chapter IV Act 1 ...").
- **Compilations:** multi-act uploads such as
"Act 1 & 2", "Act 3 & Segue" or "Full Rinascita Main Story Quest",
which count only where their chapter markers
located this entry inside them.
- **Fragments:** two channels publish one upload per quest objective
("*Utterance of Marvels: II*: Activate Resonance Beacon"),
which run a couple of minutes each
and would otherwise sink the median of the shortest entries.
They are screened out as covering less than one entry,
and readmitted where the runtime says otherwise.

Beyond the acts, a chapter here holds a prologue, an interlude
and any number of **segues**: short afterstories that close out a version.
The wiki lists them in story order without numbering them,
so this report numbers them within their chapter
(*Segue - I*, *Segue - II*) to have something to call them.

The figures it screens and grades on:

<!--gen:thresholds-->
- Acts released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
- A marker set covering less than 60 percent
of a single-act upload is ignored,
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
and *low* for any act whose median moved by 10 percent or more
against the earlier, independent set of queries (`analyze.py --compare`),
whatever its sample size says.
<!--/gen-->

## Limits of this report

Beyond the limits every report in this repository shares,
listed in the [repository README](../README.md):

- Chapter IV closes on content published days before this report.
A version that has just shipped is the one everyone uploads,
so its acts are well covered;
what is thin is the segue behind them, which is rated *low* accordingly.
- Every act is gated behind a Union Level in game,
but the wiki fills the requirement field on two quest pages only,
so the gate reads "-" almost everywhere.
That is the wiki being silent, not the game being ungated.
- The Chapter II interlude is an event chapter,
and the wiki categorises each of its five quest parts by release version
but not the page the interlude itself lives on,
so its release version reads "unknown" here.
- Because a segue carries no number of its own,
an upload titled "Act 12 & Segue" pins exactly one act label
and is read as being about that act.
Those uploads are kept, and they stretch the upper end of the range
for the acts a segue follows;
the estimate is a median, so they do not move it far.
- *At Dream's Edge* is a collaboration side story
that the wiki lists inside Chapter III's act list,
so it is measured here alongside the acts.
- The prologue ships as two quests whose titles differ only in a numeral
that the title matching never sees,
so an upload naming neither half counts as evidence for neither,
and both halves rest on small pools.

Data collected <!--f:date-->2026-08-24<!--/f-->.
