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
    overview_page="Archon Quest",
    # The account-level requirement acts are gated behind, as the game names it.
    # None for a game that gates its story some other way.
    gate_label="Adventure Rank",
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="prologue", slug="00-prologue-mondstadt", wiki_page="Prologue", region="Mondstadt",
        versions="1.0",
        title="Prologue: The Outlander Who Caught the Wind",
    ),
    dict(
        id="ch1", slug="01-chapter-i-liyue", wiki_page="Chapter I", region="Liyue",
        versions="1.0 - 1.4",
        title="Chapter I: Farewell, Archaic Lord",
    ),
    dict(
        id="ch2", slug="02-chapter-ii-inazuma", wiki_page="Chapter II", region="Inazuma",
        versions="1.6 - 2.6",
        title="Chapter II: Omnipresence Over Mortals",
    ),
    dict(
        id="ch3", slug="03-chapter-iii-sumeru", wiki_page="Chapter III", region="Sumeru",
        versions="3.0 - 3.5",
        title="Chapter III: Truth Amongst the Pages of Purana",
    ),
    dict(
        id="ch4", slug="04-chapter-iv-fontaine", wiki_page="Chapter IV", region="Fontaine",
        versions="4.0 - 4.7",
        title="Chapter IV: Masquerade of the Guilty",
    ),
    dict(
        id="ch5", slug="05-chapter-v-natlan", wiki_page="Chapter V", region="Natlan",
        versions="5.0 - 5.7",
        title="Chapter V: Incandescent Ode of Resurrection",
    ),
    dict(
        id="sotwm", slug="06-song-of-the-welkin-moon-nod-krai", wiki_page="Song of the Welkin Moon", region="Nod-Krai, later Sumeru",
        versions="5.8 - Luna VII (6.x)",
        title="Song of the Welkin Moon (unofficially Chapter VI)",
    ),
    dict(
        id="ch7", slug="07-chapter-vii-snezhnaya", wiki_page="Chapter VII", region="Snezhnaya",
        versions="7.0",
        title="Chapter VII: Everwinter Without Mercy",
    ),
]

# Adventure Rank gates, from the Archon Quest overview page.
GATES = {
    "prologue|Act I": "-", "prologue|Act II": "10", "prologue|Act III": "18",
    "ch1|Act I": "23", "ch1|Act II": "25", "ch1|Act III": "28",
    "ch1|Act IV - Prelude": "28", "ch1|Act IV": "28",
    "ch7|Act I": "18", "ch7|Act II": "-",
}
GATE_DEFAULT = {"ch2": "30", "ch3": "35", "ch4": "40", "ch5": "40", "sotwm": "40"}
