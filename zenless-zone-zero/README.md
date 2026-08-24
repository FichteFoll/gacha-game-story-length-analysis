# Zenless Zone Zero, Phaethon's Story: How Long Each Chapter Takes

Duration estimates for every chapter of the main story,
from the prologue on Sixth Street to the newest season in Roscaelifer,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->70 h 49 min<!--/f-->** (<!--f:n_report_entries-->21<!--/f--> entries counting chapters, interludes and epilogues, measured against <!--f:n_videos-->268<!--/f--> accepted uploads out of <!--f:n_candidates-->589<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Season 1 | New Eridu: Sixth Street, Lumina Square and the Outer Ring | 1.0 - 1.7 | 10 | 23 h 57 min | [01-season-1.md](01-season-1.md) |
| Season 2 | Waifei Peninsula: Yunkui Summit and Suibian Temple | 2.0 - 2.8 | 9 | 37 h 51 min | [02-season-2.md](02-season-2.md) |
| Season 3 | Roscaelifer | 3.0 - 3.1 | 2 | 9 h 01 min | [03-season-3.md](03-season-3.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Season 2, Chapter 6: To Be Fuel for the Night | 6 h 49 min |
| longest | Season 2, Interlude: Encore for an Old Dream | 5 h 03 min |
| longest | Season 3, Chapter 1: A Sleepwalker's Confession | 4 h 32 min |
| longest | Season 2, Chapter 1: Where Clouds Embrace the Dawn | 4 h 31 min |
| longest | Season 3, Chapter 2: The Long Goodbye | 4 h 29 min |
| shortest | Season 1, Chapter 1 Intermission: The Zero Zone | 1 h 18 min |
| shortest | Season 1, Chapter 3: The Midnight Pursuit | 1 h 40 min |
| shortest | Season 1, Chapter 0: Business x Strangeness x Justness | 1 h 57 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Zenless Zone Zero<!--/f-->:

- **Structure:** the chapter and chapter list, the chapter titles, the quest parts come from the
[Phaethon's Story page](https://zenless-zone-zero.fandom.com/wiki/Phaethon's_Story)
and the individual chapter and chapter pages of the Zenless Zone Zero Wiki.
- **Searches:** For every chapter, YouTube was searched four ways:
by season plus chapter number plus chapter title,
by chapter title alone,
and twice by the patch branding recent uploads use
instead of chapter titles
("Zenless Zone Zero 3.1 Season 3 Chapter 2 full quest gameplay").
- **Compilations:** multi-chapter uploads such as
"Full Season 1 Story" or "all main stories",
which count only where their chapter markers
located this chapter inside them.
- **Partial uploads:** uploads covering part of a chapter rather than all of it,
which in this game means the numbered kind
("Part 3", "Episode 4", "1/2"),
unless their runtime says they cover the chapter after all.

The figures it screens and grades on:

<!--gen:thresholds-->
- Chapters released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
- A marker set covering less than 60 percent
of a single-chapter upload is ignored,
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
and *low* for any chapter whose median moved by 10 percent or more
against the earlier, independent set of queries (`analyze.py --compare`),
whatever its sample size says.
<!--/gen-->

## Limits of this report

Beyond the limits every report in this repository shares,
listed in the [repository README](../README.md):

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

Data collected <!--f:date-->2026-08-18<!--/f-->.
