"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game's level
gate is called, the noun it numbers its acts with, and the chapters in the
order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because an act's own wiki page reaches the
renderer through `analysis.json` instead.

Terminology: Arknights: Endfield cuts its Main Missions into chapters, a
chapter into numbered processes, and a process into missions. A chapter here
is a chapter and an act is a process, because the process is what the game
labels on screen ("Chapter II Process III: The Long Feud"), what the wiki
tabulates and what the uploads are titled after. The two missions the game
plays before Chapter I Process I are its prologue, and are one entry here.

The wiki this report reads is the wiki.gg one rather than the Fandom one:
Fandom's Endfield wiki has empty placeholder pages where the questline should
be, and documents the main missions only indirectly, through achievement
requirements.
"""

REPORT = dict(
    # The wiki page that documents the questline as a whole, linked by hand from
    # README.md's method section and from every chapter's sources bullets.
    overview_page="Mission/Main",
    # No level gates the main missions: progress is gated by the story itself,
    # and the wiki records no requirement on any main mission page. See "Limits
    # of this report" in README.md.
    gate_label=None,
    # What this game numbers its acts with, for the renderer's own headings.
    unit="Process",
    date="2026-08-24",
)

CHAPTERS = [
    dict(
        id="ch1", slug="01-chapter-i", wiki_page="Mission/Main",
        region="Valley IV: The Hub, Valley Pass, Aburrey Quarry, "
               "Originium Science Park, Origin Lodespring and Power Plateau",
        versions="1.0",
        title="Chapter I",
    ),
    dict(
        id="ch2", slug="02-chapter-ii", wiki_page="Mission/Main",
        region="Wuling: Jingyu Valley, Qingbo Stockade, Wuling City "
               "and the North Wuling Exclusion Zone",
        versions="1.0 - 1.4",
        title="Chapter II",
    ),
]

# No main mission on the wiki records a level requirement, so there is no gate
# column to fill; gate_label above is None and these stay empty.
GATES = {}
GATE_DEFAULT = {}
