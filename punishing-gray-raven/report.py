"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game calls a
group of entries and one entry, the noun it numbers them with, and the groups in
the order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

Punishing: Gray Raven numbers its main story chapters straight through from 1 to
42 and groups them under nothing: the game presents the campaign as one list,
and the wiki's `Main Story` page bands the chapters it covers in fives purely to
fit them into a tabber. So the volumes below are this report's own device, ten
chapters to a file in story order and twelve in the last one, and `region_label`
holds the span of chapter numbers a volume covers rather than a place. The README
says so in as many words, because a reader is otherwise entitled to think the
game draws the line where this report does.

The six EX chapters are the exception the game itself makes: they are numbered
EX-00 to EX-05 rather than in the main run, they are filed under the main story
all the same, and they are collected here in a volume of their own.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a chapter's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the story as a whole, linked by hand from
    # README.md's method section and from every volume's sources bullets.
    overview_page="Main Story",
    # A story stage carries a recommended level in-game, and the wiki records
    # none of it, so there is no gate to publish.
    gate_label=None,
    unit="Chapter",
    container="Volume",
    region_label="Chapters",
    date="2026-08-28",
)

CHAPTERS = [
    dict(
        id="v1", slug="01-graffiti-art-to-eternal-engine", wiki_page="Main Story",
        region="1 - 10", versions="launch - Eternal Engine",
        title="Volume 1: Graffiti Art to Eternal Engine",
    ),
    dict(
        id="v2", slug="02-nona-ouroboros-to-across-the-ruined-sea",
        wiki_page="Main Story",
        region="11 - 20", versions="Nona Ouroboros - Across The Ruined Sea",
        title="Volume 2: Nona Ouroboros to Across The Ruined Sea",
    ),
    dict(
        id="v3", slug="03-spiral-of-chronos-to-stars-ensnared",
        wiki_page="Main Story",
        region="21 - 30", versions="Spiral of Chronos - Stars Ensnared",
        title="Volume 3: Spiral of Chronos to Stars Ensnared",
    ),
    dict(
        id="v4", slug="04-shapers-ripples-to-steering-by-light",
        wiki_page="Main Story",
        region="31 - 42", versions="Shaper's Ripples - Steering By Light",
        title="Volume 4: Shaper's Ripples to Steering By Light",
    ),
    dict(
        id="vex", slug="05-ex-frozen-darkness-to-inscription-of-labyrinth",
        wiki_page="Main Story",
        region="EX-00 - EX-05",
        versions="Frozen Darkness - Inscription of Labyrinth",
        title="Volume EX: Frozen Darkness to Inscription of Labyrinth",
    ),
]

# A story stage recommends a level rather than requiring one, and the wiki
# records neither, so there is nothing to gate on and `gate_label` is None.
GATES = {}
GATE_DEFAULT = {}
