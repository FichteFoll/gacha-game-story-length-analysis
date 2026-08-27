"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game calls a
group of entries and one entry, the noun it numbers them with, and the groups in
the order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

Reverse: 1999 numbers its main story chapters straight through and groups them
into three named arcs, which the wiki's `Main Story` page carries as the three
tabs of its chapter list. So the arcs below are read off the wiki rather than
invented, and `region_label` holds the span of chapter numbers an arc covers,
because an arc belongs to a stretch of the story rather than to a place.

Between the numbered chapters sit a prologue and two inter chapters, which the
game files under the main story and this report counts as entries. They are what
`unit` cannot be read off: an entry here is a chapter, and the chapters are
grouped by arc, so `container` and `unit` are different words for once.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a chapter's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the story as a whole, linked by hand from
    # README.md's method section and from every arc's sources bullets.
    overview_page="Main Story",
    # A story stage carries a recommended level in-game, and the wiki records
    # none of it: the stage tables hold the in-story timestamp and the enemies,
    # so there is no gate to publish.
    gate_label=None,
    unit="Chapter",
    container="Arc",
    region_label="Chapters",
    date="2026-08-27",
)

CHAPTERS = [
    dict(
        id="a1", slug="01-the-living-and-the-rest", wiki_page="Main Story",
        region="Prologue - 7", versions="up to 1.9",
        title="Arc 1: The Living and the Rest",
    ),
    dict(
        id="a2", slug="02-the-journey-back", wiki_page="Main Story",
        region="8 - 10", versions="2.2 - 2.8",
        title="Arc 2: The Journey Back",
    ),
    dict(
        id="a3", slug="03-the-roots-of-the-tale", wiki_page="Main Story",
        region="11 - 13", versions="3.0 onwards",
        title="Arc 3: The Roots of the Tale",
    ),
]

# The wiki records no level requirement for entering a story chapter, so there
# is nothing to gate on and `gate_label` above is None.
GATES = {}
GATE_DEFAULT = {}
