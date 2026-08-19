"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game's level
gate is called, the noun it numbers its acts with, and the chapters in the
order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because an act's own wiki page reaches the
renderer through `analysis.json` instead.

Terminology: Phaethon's Story is cut into seasons, and a season into chapters
with interludes and epilogues between them. A chapter here is a season and an
act is one of those chapters, because that is the unit the game numbers, the
wiki documents and the uploaders title their videos after.

Season 1 releases each of its chapters in two halves, (A) and (B), and its
uploads cover both at once, so this report measures the whole chapter. The two
epilogues are the exception: their halves shipped a version apart and their
uploads are titled apart, so they are two entries here as well.
"""

REPORT = dict(
    # The wiki page that documents the questline as a whole, linked by hand from
    # README.md's method section and from every chapter's sources bullets.
    overview_page="Phaethon's Story",
    # Zenless Zone Zero gates story progress behind Inter-Knot Level and the
    # Rank-Up commissions, but the wiki records no requirement per chapter, so
    # there is nothing to put in a gate column. See "Limits of this report" in
    # README.md.
    gate_label=None,
    # What this game numbers its acts with, for the renderer's own headings.
    unit="Chapter",
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="s1", slug="01-season-1", wiki_page="Season 1",
        region="New Eridu: Sixth Street, Lumina Square and the Outer Ring",
        versions="1.0 - 1.7",
        title="Season 1",
    ),
    dict(
        id="s2", slug="02-season-2", wiki_page="Season 2",
        region="Waifei Peninsula: Yunkui Summit and Suibian Temple",
        versions="2.0 - 2.8",
        title="Season 2",
    ),
    dict(
        id="s3", slug="03-season-3", wiki_page="Season 3",
        region="Roscaelifer",
        versions="3.0 - 3.1",
        title="Season 3",
    ),
]

# The wiki records no Inter-Knot Level requirement per chapter, so there is no
# gate column to fill; gate_label above is None and these stay empty.
GATES = {}
GATE_DEFAULT = {}
