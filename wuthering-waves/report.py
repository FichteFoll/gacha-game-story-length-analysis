"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game's level
gate is called, the noun it numbers its acts with, and the chapters in the
order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because an act's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the questline as a whole, linked by hand from
    # README.md's method section and from every chapter's sources bullets.
    overview_page="Main Quest",
    # The account-level requirement acts are gated behind, as the game names it.
    # None for a game that gates its story some other way.
    gate_label="Union Level",
    date="2026-08-24",
)

CHAPTERS = [
    dict(
        id="prologue", slug="00-prologue", wiki_page="Prologue", region="Huanglong",
        versions="1.0",
        title="Prologue: Utterance of Marvels",
    ),
    dict(
        id="ch1", slug="01-chapter-i-jinzhou", wiki_page="Chapter I",
        region="Huanglong, later the Black Shores",
        versions="1.0 - 1.3",
        title="Chapter I: Jinzhou Rising",
    ),
    dict(
        id="ch2", slug="02-chapter-ii-rinascita", wiki_page="Chapter II",
        region="Rinascita",
        versions="2.0 - 2.8",
        title="Chapter II: Even When Divinity Remains Silent",
    ),
    dict(
        id="ch3", slug="03-chapter-iii-roya-frostlands", wiki_page="Chapter III",
        region="Roya Frostlands, Lahai-Roi",
        versions="3.0 - 3.4",
        title="Chapter III: To the Stars Yet to Shine",
    ),
    dict(
        id="ch4", slug="04-chapter-iv-mengzhou", wiki_page="Chapter IV",
        region="Mengzhou",
        versions="3.5 - 3.6",
        title="Chapter IV: Rebirth From the Depths",
    ),
]

# Union Level gates. The wiki records a requirement on the quest page of only
# two entries, so everything else is a "-" rather than a figure this report
# would be inventing: the game gates every act, the wiki does not write it down.
GATES = {
    "ch1|Act IV": "11",
    "ch2|Interlude": "14",
}
GATE_DEFAULT = {}
