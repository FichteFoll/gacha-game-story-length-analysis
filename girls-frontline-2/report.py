"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game calls a
group of entries and one entry, the noun it numbers them with, and the groups in
the order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

Girls' Frontline 2 assigns its main story chapters a decimal number in the
Campaign menu and groups them under nothing: the wiki's `GFL2 Story` page lists
them one after another, and while every chapter from 6.5 on shipped as a named
campaign, those campaigns cover one, two or three chapters each and the eight
before them shipped under no name at all. So the volumes below are this report's
own device, five files in chapter order cut where a campaign ends, and
`region_label` holds the span of chapter numbers a volume covers rather than a
place. The README says so in as many words, because a reader is otherwise
entitled to think the game draws the line where this report does.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a chapter's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the story as a whole, linked by hand from
    # README.md's method section and from every volume's sources bullets.
    overview_page="GFL2 Story",
    # A stage carries a recommended power level in-game, and the wiki records
    # none of it: the story pages hold the stage list and the scripts, so there
    # is no gate to publish.
    gate_label=None,
    unit="Chapter",
    container="Volume",
    region_label="Chapters",
    date="2026-08-28",
)

CHAPTERS = [
    dict(
        id="v1", slug="01-double-pendulum-to-harmonic-cycle",
        wiki_page="GFL2 Story", region="1 - 6", versions="not recorded",
        title="Volume 1: Double Pendulum Simulation to Harmonic Cycle",
    ),
    dict(
        id="v2", slug="02-sojourners-to-bitter-thorns",
        wiki_page="GFL2 Story", region="6.5 - 8.7", versions="not recorded",
        title="Volume 2: Sojourners of the Glass Island to Bitter Thorns and Daisies",
    ),
    dict(
        id="v3", slug="03-aphelion-to-intertwined-assault",
        wiki_page="GFL2 Story", region="9 - 12.5", versions="not recorded",
        title="Volume 3: Aphelion to Intertwined Assault",
    ),
    dict(
        id="v4", slug="04-corposant-to-antiparallel",
        wiki_page="GFL2 Story", region="13 - 17", versions="not recorded",
        title="Volume 4: Corposant to Antiparallel",
    ),
    dict(
        id="v5", slug="05-dawnforger-to-needy-catgirl-overload",
        wiki_page="GFL2 Story", region="18 - 20", versions="not recorded",
        title="Volume 5: Dawnforger to Needy Catgirl Overload",
    ),
]

# The wiki records no requirement for entering a story chapter, so there is
# nothing to gate on and `gate_label` above is None.
GATES = {}
GATE_DEFAULT = {}
