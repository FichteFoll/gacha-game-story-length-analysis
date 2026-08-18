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
| Zenless Zone Zero | `zenless-zone-zero.fandom.com` | Zenless Zone Zero Wiki | `Phaethon's Story` (`Main Story` redirects to it) | Inter-Knot Level |
| Wuthering Waves | `wutheringwaves.fandom.com` | Wuthering Waves Wiki | `Main Quest` | Union Level |
| Arknights: Endfield | `endfield.fandom.com` | Arknights: Endfield Wiki | `Mission` | none found; leave `gate_label` unset |

`starrail.fandom.com` and `wuthering-waves.fandom.com` redirect;
`arknights-endfield.fandom.com` does not exist,
and `arknights.fandom.com` is the original game, not Endfield.

## Version infobox fields

All five categorize their quest pages as `Released in Version <name>`
and keep the infobox on `Version/<name>`,
so only `version_fields` in `data/wiki.json` differs:

| Game | number | date |
| --- | --- | --- |
| Genshin Impact | `number` | `date` |
| Honkai: Star Rail | `version` | `release_date` |
| Zenless Zone Zero | `version` | `date` |
| Wuthering Waves | `version` | `date` |
| Arknights: Endfield | `version` | `date` |

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
- **Zenless Zone Zero.** Phaethon's Story is cut into chapters and interludes.
- **Arknights: Endfield.** Released 2026-01-22 and the wiki is still thin,
  so expect to derive the act list from the mission pages themselves
  and expect low confidence throughout: the upload pool is young.
