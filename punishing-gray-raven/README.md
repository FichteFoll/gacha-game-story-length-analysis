# <!--f:game-->Punishing Gray Raven<!--/f--> Main Story: How Long Each Chapter Takes

Duration estimates for every chapter of the *Punishing: Gray Raven* main story,
from the first descent onto the surface to the chapter the global client is on,
plus the six EX chapters the game files alongside them,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main story: <!--f:grand_total-->125 h 19 min<!--/f-->** (<!--f:n_report_entries-->48<!--/f--> chapters counting the six EX chapters, measured against <!--f:n_videos-->244<!--/f--> accepted uploads out of <!--f:n_candidates-->3278<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians,
so treat it as an order of magnitude
rather than a number anyone actually clocked end to end.

## Volumes

<!--gen:chapters-->
| Volume | Chapters | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Volume 1: Graffiti Art to Eternal Engine | 1 - 10 | launch - Eternal Engine | 10 | 7 h 57 min | [01-graffiti-art-to-eternal-engine.md](01-graffiti-art-to-eternal-engine.md) |
| Volume 2: Nona Ouroboros to Across The Ruined Sea | 11 - 20 | Nona Ouroboros - Across The Ruined Sea | 10 | 24 h 33 min | [02-nona-ouroboros-to-across-the-ruined-sea.md](02-nona-ouroboros-to-across-the-ruined-sea.md) |
| Volume 3: Spiral of Chronos to Stars Ensnared | 21 - 30 | Spiral of Chronos - Stars Ensnared | 10 | 33 h 50 min | [03-spiral-of-chronos-to-stars-ensnared.md](03-spiral-of-chronos-to-stars-ensnared.md) |
| Volume 4: Shaper's Ripples to Steering By Light | 31 - 42 | Shaper's Ripples - Steering By Light | 12 | 45 h 44 min | [04-shapers-ripples-to-steering-by-light.md](04-shapers-ripples-to-steering-by-light.md) |
| Volume EX: Frozen Darkness to Inscription of Labyrinth | EX-00 - EX-05 | Frozen Darkness - Inscription of Labyrinth | 6 | 13 h 15 min | [05-ex-frozen-darkness-to-inscription-of-labyrinth.md](05-ex-frozen-darkness-to-inscription-of-labyrinth.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Volume 4, Chapter 38: Sightline Breach | 6 h 59 min |
| longest | Volume 2, Chapter 17: The Surviving Lucem | 5 h 44 min |
| longest | Volume 4, Chapter 41: Homecoming Voyage | 5 h 34 min |
| longest | Volume 4, Chapter 40: A Better Tomorrow | 5 h 19 min |
| longest | Volume 3, Chapter 27: Aeon Reforged | 5 h 01 min |
| shortest | Volume 4, Chapter 35: Echoes Adrift | 23 min |
| shortest | Volume 1, Chapter 5: Shattered Phantom | 34 min |
| shortest | Volume 1, Chapter 4: Forgotten Golden Sand | 38 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Punishing Gray Raven<!--/f-->:

- **Structure:** the chapter list comes from the
[Main Story page](https://punishing-gray-raven.fandom.com/wiki/Main_Story)
of the Punishing: Gray Raven Wiki,
which carries the chapters it covers as tabbed plot summaries,
and from the patch pages in
[Category:Content Updates](https://punishing-gray-raven.fandom.com/wiki/Category:Content_Updates),
which announce the chapters released since.
- **The unit is the chapter, and the volumes are this report's own device.**
The game numbers its main story chapters straight through
and groups them under nothing:
no arc, no season, no part.
The wiki bands them in fives to fit a tabber, and that is all the banding is.
Splitting the run into volumes of ten
is a way of getting it into files a reader can hold in one hand,
and the line between one volume and the next means nothing in the game.
Read the chapter numbers, not the volume boundaries.
- **The chapter numbers past 20 are not stated on the wiki.**
Its `Main Story` page stops at Chapter 20,
and after that a chapter's number appears only where a patch page happens
to give it, which is Chapters 31, 32 and 34 to 42.
The numbers in between are reconstructed
from the order the patch pages are chained in
and confirmed against the upload titles that name both number and chapter;
the reconstruction closes exactly on the numbers the wiki does state.
Chapter 29 is the one place where a patch page contradicts itself:
*Source Beacon* is announced as an ER chapter
under a screenshot named after the main story,
and it is Chapter 29 in every upload that names it.
- **The wiki's chapter titles are its own translations.**
Half a dozen of the early ones differ from what the global client calls them
(*Torturos Journey* against *Journey of Torture*,
*Shattered Phantom* against *Shattered Illusion*),
and this report publishes the wiki's spelling
because the wiki is what the structure is traceable to.
The searches lean on the chapter number for those,
which is what almost every upload title carries anyway.
- **Searches:** for every chapter, YouTube was searched by chapter number
and title, by "main story" and "walkthrough" phrasings,
and by title plus arabic chapter number,
because that is how this game's playthrough channels write their titles.
- **EX chapters are not in the numbered run.** The game labels them
EX-00 to EX-05, files them under the main story
and gates them behind the chapters they sit between.
They are collected here in a volume of their own,
and every numbered chapter demands that a title
not also say "EX" (`data/act_keys.json`),
because "EX Chapter 3" would otherwise count as evidence for Chapter 3.
- **Content that happens in a chapter without being its story:**
the pool carries Phantom Pain Cage and War Zone runs, boss guides,
coating and friendship stories and the Journal of Promise,
all of which are screened out as not being playthroughs
(`data/not_playthrough.txt`),
as are the several-hour "Story Collection" reels,
which are cutscenes rather than a playthrough.
- **Fragments:** most channels publish a chapter of this game a stage at a time,
so the screening for that is what decides the medians here.
The game's own stage numbering ("24-10", "EX05-8"),
the bare "(7)" instalment numbering, a node number and a closing "(Final)"
mark a split with no second reading, and those are screened out for good;
a "Part 3", a "Phase 2", a title naming stages
and one naming the hidden branch may still be readmitted on runtime,
since any of them may equally well be the whole chapter.
- **A runtime floor** (`data/min_minutes.txt`) sits under the shortest chapter
this game has. Nothing catches the side content that names a chapter
and says nothing else about itself - a bonus story, a coating story,
a summary in another language - and where a chapter's complete uploads
are missing altogether, one of those becomes its median unless the floor
counts it out.

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

- **The wiki records no version numbers.** Punishing: Gray Raven names its
patches rather than numbering them on this wiki, there are no `Version` pages,
and the patch pages carry no infobox,
so the Versions columns here hold patch names
and no patch has a release date the pipeline can read.
Nothing was therefore searched as recent,
and the newest chapters were topped up by hand instead.
- **The eight launch chapters have no release patch at all.** The wiki's patch
pages begin after global launch, so Chapters 1 to 8 read "unknown".
- **The wiki records no stage titles**, so there are no quest-part bullets in
this report, and the chapter markers of an upload had nothing to be matched
against except the chapter's own number and title.
- **What an upload of a chapter contains varies enormously.** The story stages
are combat stages with scenes between them, the dialogue is skippable,
each chapter carries an optional hidden branch,
and the uploads run from a brisk clear of the story path
to a slow read of every line;
several of this game's channels publish uploads
that are three and four times the length of the median for the same chapter.
That is the single biggest source of the spreads below.
- **The tutorial prologue is not a chapter.** The wiki writes it up on the
`Main Story` page and the game files it under nothing,
so it is not measured here.
- **Confidence is *low* almost everywhere, and for a reason
that no amount of re-harvesting fixes.** From Chapter 12 on, a chapter of
this game runs for two hours and more, and a channel that covers it
publishes it a stage or an instalment at a time,
or as a multi-hour stream.
Complete single-video uploads of the late chapters are rare:
close to half of this report's chapters rest on a handful of uploads,
several of them on a single one, and Chapter 26 on none at all.
Where a chapter's figure looks out of line with its neighbours,
that is what has happened, and the chapter's own note says so.
- **Chapter 26 carries no estimate.** Its pool held no upload that was
a playthrough of the whole chapter, so the volume total that includes it,
and the report total, are short by whatever it would have added.
- Chapters 41 and 42 shipped in the four months before the collection date,
and the pools for them are young and thin.
- The second pass that fetches exact view counts, upload dates and chapter
markers reached about a seventh of the candidates before
YouTube's bot check cut it off.
Most view counts here are therefore the search listing's rounded figures,
marked with a `~`, and most upload dates read "n/a".
The estimates themselves are unaffected:
they come from the runtimes, which the harvest already had.

Data collected <!--f:date-->2026-08-28<!--/f-->.
