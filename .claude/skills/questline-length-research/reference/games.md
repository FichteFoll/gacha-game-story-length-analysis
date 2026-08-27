# Per-game starting points

What a new report needs before step 1, for the games looked at so far.
Everything here was read off the wikis' own `api.php`
(`action=query&meta=siteinfo` for the host, `titles=` for the pages)
and is a starting point, not a substitute for checking:
wikis rename pages, and the young ones are still being built.

| Game | Wiki host | Wiki name | Questline page | Level gate |
| --- | --- | --- | --- | --- |
| Genshin Impact | `genshin-impact.fandom.com` | Genshin Impact Wiki | `Archon Quest` | Adventure Rank |
| Honkai: Star Rail | `honkai-star-rail.fandom.com` | Honkai: Star Rail Wiki | `Trailblaze Mission` | Trailblaze Level (Equilibrium Level for difficulty) |
| Zenless Zone Zero | `zenless-zone-zero.fandom.com` | Zenless Zone Zero Wiki | `Phaethon's Story` (`Main Story` redirects to it) | Inter-Knot Level, but not recorded per chapter; leave `gate_label` unset |
| Wuthering Waves | `wutheringwaves.fandom.com` | Wuthering Waves Wiki | `Main Quest` | Union Level |
| Arknights: Endfield | `endfield.wiki.gg` | Endfield Talos Wiki | `Mission/Main` | none found; leave `gate_label` unset |
| Honkai Impact 3rd | `honkaiimpact3.fandom.com` | Honkai Impact 3 Wiki | `Story` (`Main Story` redirects to it) | none recorded; leave `gate_label` unset |
| Goddess of Victory: NIKKE | `nikke-goddess-of-victory-international.fandom.com` | Nikke Goddess of Victory International Wiki | `Story`, whose chapter list is `Template:Navbox Story Chapters` | recommended Combat Power per battle, not per chapter and not on the wiki; leave `gate_label` unset |
| Reverse: 1999 | `reverse1999.fandom.com` | Reverse: 1999 Wiki | `Main Story` | none recorded per chapter; leave `gate_label` unset |

`starrail.fandom.com` and `wuthering-waves.fandom.com` redirect;
`arknights-endfield.fandom.com` does not exist,
and `arknights.fandom.com` is the original game, not Endfield.

Endfield is the one game here whose report does not read a Fandom wiki.
`endfield.fandom.com` exists and answers, but its questline pages
(`Chapter I`, `Chapter II`, `Undying Cinders`, `Path of Glory/Main Mission`)
are zero-byte placeholders untouched since January 2026,
and the only trace of the main missions on it is the requirement text of the
achievement pages in `Category:Medals`. `endfield.wiki.gg` carries the whole
structure on one page. It answers `api.php` the same way Fandom does, and it
serves no Cloudflare challenge, but it does return a "Blocked" page to some
requests; a repeat of the same request has gone through every time.

## Version infobox fields

Four of the Fandom wikis categorize their quest pages as
`Released in Version <name>` and keep the infobox on `Version/<name>`,
so only `version_fields` in `data/wiki.json` differs:

| Game | number | date |
| --- | --- | --- |
| Genshin Impact | `number` | `date` |
| Honkai: Star Rail | `version` | `release_date` |
| Zenless Zone Zero | `version` | `date` |
| Wuthering Waves | `version` | `date` |
| Arknights: Endfield | `version` | `asia start` |
| Honkai Impact 3rd | none | `debut_NA` |
| Goddess of Victory: NIKKE | none | none |
| Reverse: 1999 | none | none |

Endfield is the exception in both halves.
Its version pages are named after the version
(`Zeroth Directive`, not `Version/1.0`),
so `version_page` is `{version}`,
and they carry a per-server start time rather than one date.
Nothing categorizes a mission by version at all:
which processes a version shipped is stated in prose
in that version's own `Missions` section
("New Main Story up to Chapter II Process VI"),
so `released_in` is null and `versions.json` is written by hand from
those five sentences, which `fetch_versions.py` then leaves alone.

Honkai Impact 3rd is the second exception. Nothing categorizes a chapter by
version; each version page states in its `summary` bullets which chapter it
shipped (`*[[Part 2 Chapter IX|Part 2 Main Story Chapter IX]].`), so
`released_in` is null and `versions.json` is written out from those bullets,
which `fetch_versions.py` then leaves alone. Its version pages are named
`Version 8.3` rather than `Version/8.3`, they carry no version number field of
their own, and they date themselves per server; `debut_NA` is the earliest one
every page has. No `Version 1.x` page exists, so the eight launch chapters and
the first EX chapter have no release version to publish.

Genshin is the odd one out in a second way:
its recent versions are named (`Luna VII`) with the patch number alongside,
where the others use the patch number as the version name.
Both shapes work; the report prints "name (number)" only when the two differ.

## Structure, per game

- **Genshin Impact.** Chapters with roman-numbered acts,
  plus preludes, prologues and interludes that are entries but not acts.
- **Wuthering Waves.** Main Quests are divided into chapters,
  chapters into acts, and each act is gated behind a Union Level.
  The closest structural match to Genshin.
  The whole structure is on `Main Quest`, and each chapter page repeats it
  as a `List of Acts`; the act pages carry a `Quest Infobox` whose `actNum`
  is the label ("IV", but also "Segue"), and only three acts have a
  `List of Parts` for `quest_parts.json`.
  Besides acts, a chapter holds a prologue, an interlude and any number of
  **segues**, short afterstories the wiki lists in story order but does not
  number; number them yourself for a unique act label, but write the label
  so that `act_number()` cannot read a number out of it (`Segue - III`, not
  `Segue III`), or every segue is searched for as that chapter's "Act 3".
  The Union Level gate is real but barely recorded: the infobox `requirement`
  is filled on two quest pages in four chapters, so most acts get no gate.
  The prologue ships as `Utterance of Marvels: I` and `: II`, whose titles
  differ only in a numeral the word matching never sees, so they need
  `act_keys.json` the way Zenless Zone Zero's epilogue halves do;
  so do `Wishes in the Bell` and `Wishes in the Bell: Epilogue`.
  An event chapter doubles as the Chapter II interlude, and its `/Story` page
  carries no version category even though each of its quest parts does.
- **Honkai: Star Rail.** Trailblaze Missions are grouped by world
  (Herta Space Station, Jarilo-VI, ...) rather than by numbered chapter.
  Use the world as the chapter and the mission as the act,
  and put the world in `chapter_keys.json`: uploads title by world name.
  The wiki itself calls one mission a chapter and numbers them game-wide,
  so `Welcome to Arcadia` is "the twenty-first Trailblaze Mission chapter";
  numbering them within their world reads better and searches no worse.
  The overview page carries the quest parts of every mission,
  so `quest_parts.json` needs no per-mission fetch.
  Finality Missions and the Trial of Equilibrium
  are in the sequence but not in the main progression;
  the report so far leaves both out.
  Its uploaders split a mission across several uploads more than any other
  game looked at, which is what `partials.txt` exists for.
- **Zenless Zone Zero.** Phaethon's Story is cut into seasons,
  and a season into chapters with an intermission, an interlude and an epilogue
  among them. Use the season as the chapter and the chapter as the act.
  The structure is not on `Phaethon's Story` itself, which only transcludes it:
  read `Season 1`, `Season 2` and `Season 3`, or `Template:Chapter Navbox`,
  which carries all three plus the headers the chapters group under.
  The pages are named after the chapter's title, not after "Chapter 1A",
  and the quest parts are the links under each page's `Episodes` heading.
  Every chapter ships in an (A) and a (B) half;
  chapters 1 to 5 shipped both halves in one version and are uploaded as one
  chapter, the two epilogues shipped a version apart and are uploaded apart.
  The wiki records no Inter-Knot Level per chapter, only the other direction:
  the Senior Proxy rank-up requires the Chapter 2 Interlude commission.
  Expect low confidence across Season 1: the game is dialogue-heavy,
  the dialogue is skippable, and its uploads disagree by a factor of three.
- **Honkai Impact 3rd.** The one game here whose *entry* is a chapter. Story
  chapters are numbered across the whole game (Part 1 runs to Chapter XLII,
  then Part 2 restarts at Chapter I), and the wiki groups them under named
  arcs on `Story`, which is the container the report files them in: `unit` is
  `Chapter`, `container` is `Arc`, and `region_label` is `Part`, because an arc
  belongs to a part of the narrative rather than to a place.
  The whole structure is on `Story`, as `{{Chapter Summary}}` calls under a
  `=part=` / `==arc==` heading pair; `Template:Story Navigation` carries the
  same grouping plus the side stories interleaved with it, and is what settles
  where the bridge chapter `The Star Which the Moon Gazes Upon` belongs.
  Chapter pages are named in roman numerals (`Chapter XX`, `Chapter IX — EX-1`
  with an em dash, `EX Chapter`, `Part 2 Chapter V`), and the arabic redirects
  resolve to them.
  Because the numbering is game-wide, the chapter identifier the act-number
  fallback insists on is redundant within a part and essential between them:
  give the Part 1 arcs a key every upload carries (`honkai impact`) and the
  Part 2 arcs `part 2`, then keep Part 1's Chapters I to XIII apart from Part
  2's with a `^(?!.*\bpart ?(?:2|ii)\b)` in `act_keys.json`, and the four
  chapters that ship an EX sibling of the same number apart from it with
  `^(?!.*\bex\b)`.
  A chapter divides into in-game **acts**, which is what `partials.txt` is for
  here: "Chapter 40 Act 1" is a third of a chapter. The wiki records that
  division in the stage infobox `act` field for half the run and not at all
  for Part 2, so `quest_parts.json` covers 32 of the 65 chapters.
  Expect a wide spread: the story is dialogue-heavy and skippable, and its
  uploaders differ by a factor of two on the same chapter.

- **Goddess of Victory: NIKKE.** The second game here whose *entry* is a
  chapter, and the only one whose chapters are grouped by nothing: the game
  presents its campaign as one continuous map, the wiki lists the chapters as
  one flat `Template:Navbox Story Chapters`, and no page records an arc, a
  season or a part. The report therefore invents its container — volumes of
  ten chapters, `region_label` holding the span of chapter numbers — and says
  so in its README, because the boundaries mean nothing in the game.
  Chapter pages are named after the chapter title rather than its number
  (`Chapter 1` redirects to `Corruption`), four of them carry a
  `(chapter)` disambiguator, and the number is in the infobox `chapter_no`,
  which is worth checking the extracted list against.
  Nothing on the wiki records a release version, and no version pages exist,
  so `released_in` is null, `versions.json` stays empty and no act is ever
  searched as recent.
  Most chapter titles are a single ordinary word (`Key`, `Path`, `Return`),
  which matches far too much on its own; give every such chapter an
  `act_keys.json` mark demanding that the title also say which chapter it is.
  The pool is thick with things that happen on a chapter's map without being
  its story - Hard Mode clears, EX and boss clears, Lost Relics runs,
  Commission sub-quests - so `not_playthrough.txt` is long.
  Expect wide spreads: an upload either fights every battle on the map or
  walks the story path in Story Mode, and the two differ by a factor of two.

- **Reverse: 1999.** The third game here whose *entry* is a chapter, and the
  one whose grouping is both real and purely narrative: the main story
  chapters are numbered straight through and the wiki's `Main Story` page
  carries them as the three tabs of one wikitable, one tab per named arc
  (`The Living and the Rest`, `The Journey Back`, `The Roots of the Tale`).
  The `Template:<arc name>` calls that page's tabber uses lag behind the
  table, so read the table. Chapter pages are named after the chapter title
  (`Chapter 1` redirects to `In Our Time`), and among the numbered chapters
  sit a prologue and two **inter chapters**, whose stage prefixes are `5SP`
  and `7SP`. Label those so that `act_number()` reads no number out of them
  (`Inter Chapter - I`, as with Wuthering Waves's segues), or a title saying
  "Interlude" pins them by the `l` in it.
  A chapter is a run of 15 to 30 named story stages, tabulated in a
  `{{Stage Summary}}` call per stage (positionally: code, in-story timestamp,
  name), which is what `quest_parts.json` holds; the prologue and the first
  inter chapter use a plain wikitable instead, and the second inter chapter
  has named character meetings rather than stages. An unnamed stage repeats
  its timestamp in the name slot, and Chapter 6 closes on a stage named after
  the chapter, which has to be left out or every complete upload of that
  chapter reads as a fragment of it.
  Nothing categorizes a chapter by version. A version page announces
  "The new main story chapter [X]" from 1.4 on, and its banner file is named
  after the chapter, so `released_in` is null and `versions.json` is written
  out from those pages; the launch chapters, both inter chapters and the
  newest chapter are recorded nowhere. The version pages carry no infobox at
  all - the run dates are prose in a `<center><small>` - so no version gets a
  date and nothing is ever searched as recent; top the newest chapter up by
  hand. Its version pages are named `Version 1.4`, so `version_page` is
  `Version {version}`, and `Version 1.0` does not exist.
  Two things this pool punishes. "Full story" is the ordinary phrasing for
  one complete chapter, so screening it as a compilation throws away the best
  evidence for every entry; and the chapters run for four to eight hours, so
  most uploaders split them, which makes `partials.txt` the file that decides
  the medians. Catch every `Part N` rather than only the high numbers: seeded
  from a pool of halves, `readmit_partials()` sets a median at half the real
  length and the trim then discards the complete uploads as outliers.
  Expect a wide spread and thin samples: the dialogue is skippable, and only
  a handful of channels publish a whole chapter as one video.

- **Arknights: Endfield.** Released 2026-01-22 and the wiki is still thin,
  so expect to derive the act list from the mission pages themselves
  and expect low confidence throughout: the upload pool is young.
