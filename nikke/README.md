# <!--f:game-->NIKKE<!--/f--> Campaign: How Long Each Chapter Takes

Duration estimates for every story chapter of the *Goddess of Victory: NIKKE* campaign,
from the tutorial descent onto the surface to the current chapter,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole campaign story: <!--f:grand_total-->62 h 18 min<!--/f-->** (<!--f:n_report_entries-->47<!--/f--> chapters counting the prologue, measured against <!--f:n_videos-->475<!--/f--> accepted uploads out of <!--f:n_candidates-->1035<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Volumes

<!--gen:chapters-->
| Volume | Chapters | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Volume 1: Fall to Secret | 00 - 09 | not recorded | 10 | 5 h 06 min | [01-fall-to-secret.md](01-fall-to-secret.md) |
| Volume 2: Comrade to Eden | 10 - 19 | not recorded | 10 | 8 h 34 min | [02-comrade-to-eden.md](02-comrade-to-eden.md) |
| Volume 3: Flame Dragon to Rescue | 20 - 29 | not recorded | 10 | 15 h 22 min | [03-flame-dragon-to-rescue.md](03-flame-dragon-to-rescue.md) |
| Volume 4: Treasure to Gene | 30 - 39 | not recorded | 10 | 15 h 43 min | [04-treasure-to-gene.md](04-treasure-to-gene.md) |
| Volume 5: Choice to Rebirth | 40 - 46 | not recorded | 7 | 17 h 33 min | [05-choice-to-rebirth.md](05-choice-to-rebirth.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Volume 5, Chapter 44: Path | 3 h 07 min |
| longest | Volume 5, Chapter 46: Rebirth | 3 h 02 min |
| longest | Volume 5, Chapter 42: Only One | 2 h 52 min |
| longest | Volume 5, Chapter 41: Birth | 2 h 20 min |
| longest | Volume 3, Chapter 24: Banishment | 2 h 20 min |
| shortest | Volume 1, Chapter 00: Fall | 8 min |
| shortest | Volume 1, Chapter 03: Enlightenment | 12 min |
| shortest | Volume 2, Chapter 10: Comrade | 20 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->NIKKE<!--/f-->:

- **Structure:** the chapter list and the chapter titles come from the
[Story page](https://nikke-goddess-of-victory-international.fandom.com/wiki/Story)
of the Nikke Goddess of Victory International Wiki,
which carries them as one flat navigation box,
and from the individual chapter pages, which carry the synopses.
- **The unit is the chapter, and the volumes are this report's own device.**
The game numbers its campaign chapters straight through from the prologue,
presents them as one continuous map,
and groups them under nothing:
no arc, no season, no part.
Splitting the run into volumes of ten is a way of getting it into files
a reader can hold in one hand,
and the line between one volume and the next means nothing in the game.
Read the chapter numbers, not the volume boundaries.
- **Searches:** for every chapter, YouTube was searched by chapter number
and title, by "main story" and "campaign" phrasings,
and by title plus arabic chapter number,
because that is how this game's walkthrough channels write their titles.
- **The chapter number has to be in the title.** Most of this game's chapters
are named with a single ordinary word - *Key*, *Path*, *Return*, *Choice* -
and matching an upload on that word alone would sweep in
everything from bond stories to boss guides.
An upload counts as evidence for such a chapter only if it also says
which chapter it is (`data/act_keys.json`).
The cost is the uploads that abbreviate it to "CH 31",
which the number matching does not read; those are lost.
- **Combat modes that are not the story:** the pool is thick with
Hard Mode clears, EX-stage and boss clears, Lost Relics location runs
and Commission sub-quests, all of which take place on a chapter's map
and none of which is the chapter's story.
They are screened out as not being playthroughs (`data/not_playthrough.txt`).
- **Clips:** the same maps produce a great many highlight clips
that name the chapter and run a couple of minutes.
No wording catches them, so this report sets a runtime floor
(`data/min_minutes.txt`) below the length of the prologue,
which is the shortest chapter here.
- **Fragments:** the game's own stage numbering ("32-12") and the "(1/2)"
half-uploads mark a split with no second reading,
so those are screened out for good;
a "Part 3" may still be readmitted on its runtime,
since it is as likely to be the third instalment of a complete playthrough.

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

- **The wiki records no release version for any chapter**, and no version
pages exist on it at all, so the Versions column reads "not recorded"
throughout and the harvest could not search recent chapters
by patch branding or search them any deeper than the settled ones.
- **The wiki stops where it stops.** Its chapter list ends at the last
chapter published here, while uploads for later chapters are already in
the search results. Those are screened out as naming no chapter this
report knows, and the report covers what the wiki documents.
- **What an upload of a NIKKE chapter contains varies more than in any other
report here.** A chapter is a map of battles with story scenes between them,
and the uploads divide into ones that fight every battle
and ones that walk the story path in Story Mode;
the second kind can be less than half the length of the first.
That is the single biggest source of the spreads below,
and a chapter can be rated *low* on a pool of a dozen uploads
purely because its uploaders were not playing the same way.
- **The early chapters are minutes long and the late ones are hours long.**
The prologue is a tutorial and the recent chapters are full expeditions.
Do not read the totals as if the units were comparable across the run.
- The second pass that fetches exact view counts, upload dates and
chapter markers did not finish.
YouTube's bot check cut it off after a third of the candidates,
so most view counts here are the search listing's rounded figures,
marked with a `~`, and most upload dates read "n/a".
The estimates themselves are unaffected:
they come from the runtimes, which the harvest already had.
- The wiki records no quest parts, no stage list and no act division
for a chapter, so there are no quest-part bullets in this report
and the chapter markers of an upload had nothing to be matched against
except the chapter's own number and title.
- NIKKE gates a battle behind a recommended Combat Power rather than
behind an account level, and the wiki records no requirement per chapter,
so this report publishes no gate.

Data collected <!--f:date-->2026-08-26<!--/f-->.
