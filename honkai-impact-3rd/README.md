# <!--f:game-->Honkai Impact 3rd<!--/f--> Story: How Long Each Chapter Takes

Duration estimates for every chapter of the Story menu,
from the opening run aboard the Selene to the current Part 2 arc,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole story: <!--f:grand_total-->143 h 55 min<!--/f-->** (<!--f:n_report_entries-->65<!--/f--> chapters counting the EX chapters and the bridge interlude, measured against <!--f:n_videos-->564<!--/f--> accepted uploads out of <!--f:n_candidates-->2903<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->chapter<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Arcs

<!--gen:chapters-->
| Arc | Part | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Where Dreams Began | Part 1 | not recorded | 2 | 1 h 17 min | [01-where-dreams-began.md](01-where-dreams-began.md) |
| The End of Destiny | Part 1 | not recorded | 4 | 2 h 46 min | [02-the-end-of-destiny.md](02-the-end-of-destiny.md) |
| Under the Falling Sky | Part 1 | not recorded - 3.0 | 5 | 4 h 42 min | [03-under-the-falling-sky.md](03-under-the-falling-sky.md) |
| From the Deep Ocean | Part 1 | 3.0 - 3.4 | 4 | 6 h 47 min | [04-from-the-deep-ocean.md](04-from-the-deep-ocean.md) |
| A Shooting Star Streaking Across the Night | Part 1 | 3.5 - 3.6 | 2 | 1 h 47 min | [05-a-shooting-star.md](05-a-shooting-star.md) |
| Elegy to Yesterday | Part 1 | 3.8 - 4.0 | 3 | 4 h 17 min | [06-elegy-to-yesterday.md](06-elegy-to-yesterday.md) |
| Here Lies Bellflower | Part 1 | 4.1 - 4.2 | 2 | 2 h 47 min | [07-here-lies-bellflower.md](07-here-lies-bellflower.md) |
| Taixuan Dream | Part 1 | 4.3 - 4.5 | 3 | 6 h 08 min | [08-taixuan-dream.md](08-taixuan-dream.md) |
| Remaining Flames | Part 1 | 4.7 - 4.9 | 3 | 10 h 52 min | [09-remaining-flames.md](09-remaining-flames.md) |
| Thus Spoke Apocalypse | Part 1 | 5.1 - 5.4 | 4 | 6 h 51 min | [10-thus-spoke-apocalypse.md](10-thus-spoke-apocalypse.md) |
| To the Flawless | Part 1 | 5.7 - 5.9 | 3 | 6 h 04 min | [11-to-the-flawless.md](11-to-the-flawless.md) |
| The Day of Transcending Finality | Part 1 | 6.0 - 6.4 | 5 | 10 h 31 min | [12-the-day-of-transcending-finality.md](12-the-day-of-transcending-finality.md) |
| At the Fingertip of the Sea | Part 1.5 | 6.5 - 6.8 | 4 | 9 h 46 min | [13-at-the-fingertip-of-the-sea.md](13-at-the-fingertip-of-the-sea.md) |
| Beyond the Stars | Part 1.5 | 6.9 - 7.2 | 4 | 10 h 13 min | [14-beyond-the-stars.md](14-beyond-the-stars.md) |
| Tides of Time Gone By | Part 2 | 7.3 - 7.6 | 4 | 11 h 19 min | [15-tides-of-time-gone-by.md](15-tides-of-time-gone-by.md) |
| A Shore Under Watch | Part 2 | 7.7 | 1 | 3 h 10 min | [16-a-shore-under-watch.md](16-a-shore-under-watch.md) |
| Dawn after the Remaining Old Wish | Part 2 | 7.8 - 8.4 | 7 | 25 h 29 min | [17-dawn-after-the-remaining-old-wish.md](17-dawn-after-the-remaining-old-wish.md) |
| A Rose in a Curtsy | Part 2 | 8.5 - 8.9 | 5 | 19 h 09 min | [18-a-rose-in-a-curtsy.md](18-a-rose-in-a-curtsy.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->chapters<!--/f-->

<!--gen:extremes-->
| | Chapter | Estimate |
| --- | --- | --- |
| longest | Part 2, Chapter IX: If Destiny Concludes Today | 5 h 37 min |
| longest | Part 1.5, Chapter XXXVIII: Lone Tower, Fallen Star | 5 h 26 min |
| longest | Part 2, Chapter II: The Seven Shus in the Maze | 4 h 39 min |
| longest | Part 2, Chapter XI: A Mass for Atheists | 4 h 24 min |
| longest | Part 2, Chapter XII: With You, Whom I Never Knew | 4 h 19 min |
| shortest | Part 1, Chapter VII: Lift the Sword of Rebellion | 21 min |
| shortest | Part 1, Chapter XIV: Dispel the Darkness | 27 min |
| shortest | Part 1, Chapter I: Dusk, Girls, Battleship | 28 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Honkai Impact 3rd<!--/f-->:

- **Structure:** the arc and chapter list and the chapter titles come from the
[Story page](https://honkaiimpact3.fandom.com/wiki/Story)
of the Honkai Impact 3 Wiki,
which groups the chapters under named arcs and the arcs under parts,
and from the individual chapter pages,
which carry the in-game act each of a chapter's stages belongs to.
- **The unit is the chapter.** This is the one game in this repository
whose entry *is* a chapter: the chapters are numbered across the whole game
rather than within a group, Part 1 running to Chapter XLII
before Part 2 restarts at Chapter I.
The arcs are what the wiki files them under and what this report
gives a file to; they are stretches of narrative, not places,
so the column that holds a region elsewhere holds the part here.
- **Searches:** for every chapter, YouTube was searched by chapter title,
by part plus chapter number plus title,
and by the patch branding recent uploads carry.
Because that harvest came back thin almost everywhere,
every chapter was then searched again
with eight further phrasings copied from the title formats
that the channels publishing whole chapters actually use.
- **Fragments:** a chapter of this game divides into in-game **acts**,
and most of its uploaders publish one video per act,
sometimes one per stage.
Those uploads are screened out as covering less than one chapter.
For the wordings that admit of no second reading
("Act 3", "Stage 38-4", "Episode 2", "Side Story")
the screening is final, because in this game they are never the whole chapter;
a "Part 3" may still be readmitted on its runtime,
since it is as likely to be the third instalment of a complete playthrough,
or the game's own Part 2, as a split.
This is the single biggest screening problem the game poses,
and it is why so many chapters here rest on small pools:
the complete uploads are the minority.
- **Instalments under one title:** several channels publish a chapter in
instalments and reuse the title verbatim for each of them.
Where an uploader has more than one video under one title for a chapter,
the set is read as a split.
- **Clips:** the pool carries a great many highlight clips
that name the chapter, say nothing about their scope and run a few minutes.
No wording catches them, so this report sets a runtime floor
(`data/min_minutes.txt`) below the length of the shortest chapter here,
and an upload under it is counted out as not being a playthrough.
- **Cutscene cuts:** the story is dialogue-heavy and largely skippable,
and several channels publish a "Full CG" cut of a chapter
that runs almost as long as playing it.
Those are screened out as not being playthroughs.

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

- The two Part 1.5 arcs, *At the Fingertip of the Sea* and
*Beyond the Stars*, are the weakest stretch of this report.
Their chapters run for hours, nearly every channel that recorded them
published one video per in-game act,
and what is left to measure a whole chapter with is one or two uploads.
Every entry in them is rated *low*, and the sample size is printed
next to each estimate; read them as orders of magnitude.
- The second pass that fetches exact view counts, upload dates and
chapter markers did not finish.
YouTube's bot check cut it off after a few hundred of the candidates,
so most view counts here are the search listing's rounded figures,
marked with a `~`, and most upload dates read "n/a".
The estimates themselves are unaffected:
they come from the runtimes, which the harvest already had.
- The game is ten years old and its early chapters are short,
which is the opposite of the pattern every other report here shows.
Chapter I is a tutorial; the Part 2 chapters are open-world arcs
that run for hours.
Do not read the totals as if the units were comparable across the run.
- Uploaders disagree about this game a great deal.
The story can be skipped through, and some uploaders do;
others record every optional conversation.
Confidence is *low* far more often than in the other reports,
and it is saying something real.
- No `Version 1.x` page exists on the wiki,
so the eight launch chapters and the first EX chapter
have no release version to publish and read "unknown".
- Nothing on the wiki records a level requirement for entering a chapter,
so this report publishes no gate.
- The wiki records the in-game act a stage belongs to for the earlier
chapters only, and not at all for Part 2,
so the quest-part bullets stop partway through the run.
- *The Star Which the Moon Gazes Upon* shipped as an event rather than
as a numbered chapter, and the wiki gives it a heading of its own
on the Story page while the navigation box files it under
*Beyond the Stars*. It is measured here as that arc's interlude.
- *Banquet Dance of Shade* sits in the Story page's chapter list
with no title of its own and is a side story rather than a stage;
it is left out.

Data collected <!--f:date-->2026-08-26<!--/f-->.
