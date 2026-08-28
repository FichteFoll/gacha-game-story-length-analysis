# <!--f:game-->Girls' Frontline 2 Exilium<!--/f--> Main Story: How Long Each Chapter Takes

Duration estimates for every numbered main story chapter of *Girls' Frontline 2: Exilium*,
from the opening simulation to the latest campaign the wiki gives a number,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole numbered main story: <!--f:grand_total-->101 h 21 min<!--/f-->** (<!--f:n_report_entries-->25<!--/f--> chapters counting the five filed between two whole numbers, measured against <!--f:n_videos-->245<!--/f--> accepted uploads out of <!--f:n_candidates-->573<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Volumes

<!--gen:chapters-->
| Volume | Chapters | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Volume 1: Double Pendulum Simulation to Harmonic Cycle | 1 - 6 | not recorded | 6 | 16 h 34 min | [01-double-pendulum-to-harmonic-cycle.md](01-double-pendulum-to-harmonic-cycle.md) |
| Volume 2: Sojourners of the Glass Island to Bitter Thorns and Daisies | 6.5 - 8.7 | not recorded | 6 | 19 h 22 min | [02-sojourners-to-bitter-thorns.md](02-sojourners-to-bitter-thorns.md) |
| Volume 3: Aphelion to Intertwined Assault | 9 - 12.5 | not recorded | 5 | 20 h 31 min | [03-aphelion-to-intertwined-assault.md](03-aphelion-to-intertwined-assault.md) |
| Volume 4: Corposant to Antiparallel | 13 - 17 | not recorded | 5 | 28 h 28 min | [04-corposant-to-antiparallel.md](04-corposant-to-antiparallel.md) |
| Volume 5: Dawnforger to Needy Catgirl Overload | 18 - 20 | not recorded | 3 | 16 h 26 min | [05-dawnforger-to-needy-catgirl-overload.md](05-dawnforger-to-needy-catgirl-overload.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Volume 4, Chapter 15: Corposant - Part 2 | 7 h 17 min |
| longest | Volume 4, Chapter 16: Antiparallel - Part 1 | 6 h 55 min |
| longest | Volume 5, Chapter 19: Dawnforger - Part 2 | 6 h 36 min |
| longest | Volume 4, Chapter 14: Corposant - Part 1.5 | 6 h 09 min |
| longest | Volume 2, Chapter 8.7: Bitter Thorns and Daisies | 5 h 40 min |
| shortest | Volume 1, Chapter 1: Double Pendulum Simulation | 1 h 39 min |
| shortest | Volume 2, Chapter 6.7: Sojourners of the Glass Island - Part 2 | 1 h 56 min |
| shortest | Volume 2, Chapter 8.3: Amidst Wings of Gray | 2 h 14 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Girls' Frontline 2 Exilium<!--/f-->:

- **Structure:** the chapter list, the chapter titles and the stage lists come
from the [GFL2 Story page](https://iopwiki.com/wiki/GFL2_Story) of IOP Wiki,
which carries the whole campaign as one page, one tab per chapter,
and from its [Summary page](https://iopwiki.com/wiki/GFL2_Story/Summary),
which carries one section per chapter and the release order per server.
It is the second report here that does not read a Fandom wiki:
IOP Wiki is the series wiki, and the only one
that documents this game's story at all.
- **The unit is the chapter, and the volumes are this report's own device.**
The game assigns each main story chapter a number in the Campaign menu
and groups the chapters under nothing.
Every chapter from 6.5 onwards shipped as a named campaign,
but those campaigns cover one, two or three chapters each,
and the eight before them shipped under no name at all,
so there is no grouping to read off the wiki.
Splitting the run into five volumes is a way of getting it into files
a reader can hold in one hand, cut where a campaign ends;
the line between one volume and the next means nothing in the game.
Read the chapter numbers, not the volume boundaries.
- **Five chapters carry a decimal number.** Chapters 6.5, 6.7, 8.3, 8.7 and 12.5
are campaigns the game filed between two whole-numbered chapters,
and they are chapters of the main story like any other.
A whole chapter's number is a prefix of theirs,
so Chapters 6, 8 and 12 have to rule the decimals out by hand
(`data/act_keys.json`) or an upload of Chapter 6.5
would count as evidence for Chapter 6.
- **A campaign shipped as several chapters is uploaded under the campaign's
name and a part number.** "Deep Oblivion Part 2" carries none of Chapter 12's
own words, and *Corposant* alone covers three chapters,
so each chapter of a multi-chapter campaign requires either its own number
or its part number in the title (`data/act_keys.json`).
An upload that names the campaign and no part is evidence for none of them.
- **Searches:** for every chapter, YouTube was searched by chapter number
and title, by "main story" and "all missions" phrasings,
and by title alone with the game abbreviated to GFL2,
because that is how this game's walkthrough channels write their titles.
The thinnest chapters were then topped up by hand,
by campaign name and part number rather than by chapter number.
- **Combat that is not the story:** a chapter is a map of story stages,
and the same map carries Hard Mode clears, boss rushes and simulation modes.
Those are screened out as not being playthroughs
(`data/not_playthrough.txt`), along with the usual gacha and tier-list traffic.
- **Fragments:** the game's own stage codes ("5-10", "LA-1-16") and the
"(1/5)" instalment numbering mark less than a whole chapter,
as does a title naming one of the chapter's stages;
the stage codes admit of no second reading and are screened out for good,
while an instalment number may still be readmitted on its runtime.
A generic "Part 3" is *not* screened out here,
because in this game's vocabulary a part number usually names the chapter
rather than a split of it.
- **Clips:** the story stages produce a great many highlight clips
that name the chapter and run a couple of minutes,
and no wording catches them, so this report sets a runtime floor
(`data/min_minutes.txt`) below the length of the shortest chapter here.

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

- **This report covers the chapters the game gives a number.**
Two further main story campaigns have shipped,
[Moonshroud Requiem](https://iopwiki.com/wiki/Moonshroud_Requiem) and
[Chiral Redundancy](https://iopwiki.com/wiki/Chiral_Redundancy),
which the wiki files under the main story with no chapter number against them,
and a third, *Siege of Iliad*, which has only reached the Chinese server.
None of the three is measured here.
- **The wiki records no release version for any chapter**, and no GFL2 version
pages exist on it at all, so the Versions column reads "not recorded"
throughout and the harvest could not search the newest chapters
by patch branding or search them any deeper than the settled ones.
What the wiki does record is the release order per server,
which is what the chapter order here follows.
- **The Chinese server is roughly a year ahead**, and it reordered the story
on the way to the other servers: chapter numbers were applied retroactively,
and several campaigns arrived in a different order.
Uploads from the Chinese server are screened out where they say so,
but an upload of the same chapter is the same chapter whichever server it is.
- **Skippable dialogue is the largest single source of spread here.**
A chapter is roughly half story stages and half combat,
and an uploader who reads is on screen for twice as long as one who skips.
Several chapters are rated *low* on a pool of ten uploads
purely because their uploaders were not playing at the same speed.
- **The story-collection uploads are longer than the playthroughs.**
Several channels publish a chapter as a "story collection"
that includes the between-stage scenes a playthrough clicks past,
and those sit at the top of most of the ranges below.
- The second pass that fetches exact view counts, upload dates and
chapter markers did not finish.
YouTube's bot check cut it off with well over a hundred candidates unfetched,
so many view counts here are the search listing's rounded figures,
marked with a `~`, and many upload dates read "n/a".
The estimates themselves are barely affected:
they come from the runtimes, which the harvest already had.
- **Most chapters have no quest-part bullets.** The stage list is on the wiki
for every chapter, but a stage's time can only be published
where enough uploaders marked it out with a chapter marker,
and the unfinished second pass is what limits that.
- **Two stages are missing from the stage lists**, deliberately.
A stage named after its own chapter
("2-9: Signal" in *Second Signal*, "GW-1-9: Amidst Wings of Gray")
would make every complete upload of that chapter
read as an upload of one stage of it,
so those two are left out of `data/quest_parts.json`
and the numbering in the quest-part bullets skips them.
- A stage carries a recommended power level in-game
and the wiki records none of it,
so this report publishes no gate.

Data collected <!--f:date-->2026-08-28<!--/f-->.
