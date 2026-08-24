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

The four Fandom wikis categorize their quest pages as
`Released in Version <name>` and keep the infobox on `Version/<name>`,
so only `version_fields` in `data/wiki.json` differs:

| Game | number | date |
| --- | --- | --- |
| Genshin Impact | `number` | `date` |
| Honkai: Star Rail | `version` | `release_date` |
| Zenless Zone Zero | `version` | `date` |
| Wuthering Waves | `version` | `date` |
| Arknights: Endfield | `version` | `asia start` |

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
- **Arknights: Endfield.** Released 2026-01-22 and the wiki is still thin,
  so expect to derive the act list from the mission pages themselves
  and expect low confidence throughout: the upload pool is young.
