# <!--f:game-->Reverse: 1999<!--/f--> Main Story: How Long Each Chapter Takes

Duration estimates for every chapter of the *Reverse: 1999* main story,
from the prologue aboard the APPLe to the current chapter,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main story: <!--f:grand_total-->65 h 13 min<!--/f-->** (<!--f:n_report_entries-->16<!--/f--> chapters counting the prologue and the two inter chapters, measured against <!--f:n_videos-->157<!--/f--> accepted uploads out of <!--f:n_candidates-->661<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians,
so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Arcs

<!--gen:chapters-->
| Arc | Chapters | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Arc 1: The Living and the Rest | Prologue - 7 | up to 1.9 | 10 | 30 h 56 min | [01-the-living-and-the-rest.md](01-the-living-and-the-rest.md) |
| Arc 2: The Journey Back | 8 - 10 | 2.2 - 2.8 | 3 | 15 h 06 min | [02-the-journey-back.md](02-the-journey-back.md) |
| Arc 3: The Roots of the Tale | 11 - 13 | 3.0 onwards | 3 | 19 h 11 min | [03-the-roots-of-the-tale.md](03-the-roots-of-the-tale.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Arc 1, Chapter 7: Vereinsamt | 8 h 05 min |
| longest | Arc 3, Chapter 12: The Campaign's Tale | 7 h 20 min |
| longest | Arc 2, Chapter 10: Paradise Regained | 6 h 18 min |
| longest | Arc 3, Chapter 13: On Another's Sorrow | 6 h 01 min |
| longest | Arc 3, Chapter 11: A Long Long Way | 5 h 50 min |
| shortest | Arc 1, Inter Chapter - II: To the New World | 36 min |
| shortest | Arc 1, Prologue: This is Tomorrow | 38 min |
| shortest | Arc 1, Inter Chapter - I: The Star | 1 h 22 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Reverse: 1999<!--/f-->:

- **Structure:** the chapter list, the arc grouping and the chapter titles come
from the [Main Story page](https://reverse1999.fandom.com/wiki/Main_Story)
of the Reverse: 1999 Wiki,
which carries the whole run as the three tabs of one table,
and the per-chapter stage lists come from the individual chapter pages.
- **The unit is the chapter, and the arcs are the wiki's own.**
The game numbers its main story chapters straight through
and groups them under three named arcs,
which is what the three files below are.
Between the numbered chapters sit a prologue
and two inter chapters, filed under the main story by the game
and counted as entries here.
- **The stage list stands in for quest parts.** A chapter is a run of
15 to 30 named story stages, and the wiki tabulates them in order,
so those are what an uploader's chapter markers are matched against
and what an upload titled after a single stage is recognised by.
One stage of Chapter 6 carries the chapter's own name,
and is left out of that chapter's list:
a title naming it cannot be told from a title naming the whole chapter.
- **Searches:** for every chapter, YouTube was searched by chapter number
and title, by "main story" and "full story" phrasings,
by title plus patch number where the wiki records one,
and by hand-written queries for the chapters
the templates left with a thin pool.
- **"Full story" is not a compilation here.** It is this game's ordinary
phrasing for one complete chapter, so it is deliberately not screened out;
what is screened out is "all chapters", a numbered chapter range,
and a title that names a chapter *and* an inter chapter.
- **Splits are the norm, not the exception.** A chapter runs for hours,
and most uploaders publish it in halves, in thirds or one stage at a time.
The game's own stage codes ("7TH-12", "1-16"), a "Stage 13-18" range
and a "(1/3)" mark a split with no second reading;
a "Part 2" or a "pt. 36" may still be readmitted on its runtime,
since it is as likely to be the third instalment of a complete playthrough.
- **The inter chapters need naming twice.** *The Star* and
*To the New World* are ordinary enough phrases that matching an upload on
the words alone would sweep in half the game;
an upload counts as evidence for one of them only if it also says
"inter chapter", "special", or the stage prefix the game files it under
(`data/act_keys.json`).
- **Combat that is not the story:** the pool carries Hard Mode clears,
all-stage and all-hard-stage runs, survey stages, boss guides
and the event stages that share a chapter's name,
none of which is the chapter's story
(`data/not_playthrough.txt`).
- **Clips:** the same chapters produce a great many highlight clips
that name the chapter and run a couple of minutes.
No wording catches them, so this report sets a runtime floor
(`data/min_minutes.txt`) below the length of the shortest entry.

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

- **The wiki records a release version for half the entries and no release
date for any of them.** A version page announces "the new main story
chapter" from 1.4 onwards, and that is where the Versions column comes from;
nothing on the wiki says which version shipped the launch chapters,
either inter chapter, or the newest chapter, whose version page does not
exist yet. Because no version carries a machine-readable date either,
no chapter counted as recent and none was searched any deeper for it;
the thin pools were topped up by hand instead.
- **Most uploaders split a chapter, so the pool of whole-chapter uploads is
small.** A handful of channels publish a chapter as one video and everybody
else publishes it in instalments, which are screened out as fragments.
That is why several chapters here rest on fewer uploads
than their view counts would suggest,
and are rated *low* on sample size alone.
- **The spread within a chapter is wide because the dialogue is skippable.**
This is a text-heavy game whose story stages can be read or clicked past,
and two uploaders playing the same chapter can differ by a factor of two.
That, rather than any measurement error, is what the ranges below show.
- **Uploads titled as a "movie" are screened out** as cutscene edits,
which is what the phrasing means in every other report here.
For this game some of them are complete playthroughs,
so a little good evidence is lost to the shared rule.
- The second pass that fetches exact view counts, upload dates and
chapter markers reached about two thirds of the candidates
before YouTube's bot check cut it off.
The rest keep the search listing's rounded view counts,
marked with a `~`, and read "n/a" for their upload date.
The estimates themselves are unaffected:
they come from the runtimes, which the harvest already had.
- The arcs are the wiki's grouping of the story and mean nothing mechanically:
nothing in the game gates on an arc boundary,
and the report files chapters by arc only because the wiki does.
- The wiki records no level requirement for entering a story chapter,
so this report publishes no gate.

Data collected <!--f:date-->2026-08-27<!--/f-->.
