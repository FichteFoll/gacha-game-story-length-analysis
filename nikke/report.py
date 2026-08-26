"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game calls a
group of entries and one entry, the noun it numbers them with, and the groups in
the order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

NIKKE numbers its campaign chapters straight through from 00 to 46 and groups
them under nothing at all: the wiki lists them as one flat navbox, the game
presents them as one continuous campaign map, and no page records an arc, a
season or a part. So the volumes below are this report's own device, ten
chapters to a file in story order, and `region_label` holds the span of chapter
numbers a volume covers rather than a place. The README says so in as many
words, because a reader is otherwise entitled to think the game draws the line
where this report does.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a chapter's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the story as a whole, linked by hand from
    # README.md's method section and from every volume's sources bullets.
    overview_page="Story",
    # NIKKE gates a stage behind a recommended Combat Power rather than behind
    # an account level, and the wiki records no requirement per chapter, so
    # there is no gate to publish.
    gate_label=None,
    unit="Chapter",
    container="Volume",
    region_label="Chapters",
    date="2026-08-26",
)

CHAPTERS = [
    dict(
        id="v1", slug="01-fall-to-secret", wiki_page="Story",
        region="00 - 09", versions="not recorded",
        title="Volume 1: Fall to Secret",
    ),
    dict(
        id="v2", slug="02-comrade-to-eden", wiki_page="Story",
        region="10 - 19", versions="not recorded",
        title="Volume 2: Comrade to Eden",
    ),
    dict(
        id="v3", slug="03-flame-dragon-to-rescue", wiki_page="Story",
        region="20 - 29", versions="not recorded",
        title="Volume 3: Flame Dragon to Rescue",
    ),
    dict(
        id="v4", slug="04-treasure-to-gene", wiki_page="Story",
        region="30 - 39", versions="not recorded",
        title="Volume 4: Treasure to Gene",
    ),
    dict(
        id="v5", slug="05-choice-to-rebirth", wiki_page="Story",
        region="40 - 46", versions="not recorded",
        title="Volume 5: Choice to Rebirth",
    ),
]

# The wiki records no requirement for entering a story chapter, so there is
# nothing to gate on and `gate_label` above is None.
GATES = {}
GATE_DEFAULT = {}
