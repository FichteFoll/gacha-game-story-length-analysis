"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game calls a
group of entries and one entry, the noun it numbers them with, and the arcs in
the order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

Honkai Impact 3rd is the one game here whose entry *is* a chapter: its story
chapters are numbered across the whole game rather than within a group, and the
groups the wiki files them under are named arcs, not places. So `container` is
an arc, `unit` is a chapter, and the column that holds a region elsewhere holds
the part of the narrative the arc belongs to.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a chapter's own wiki page reaches the
renderer through `analysis.json` instead.
"""

REPORT = dict(
    # The wiki page that documents the story as a whole, linked by hand from
    # README.md's method section and from every arc's sources bullets.
    overview_page="Story",
    # Nothing on this wiki records a level requirement for a story chapter, so
    # there is no gate to publish.
    gate_label=None,
    unit="Chapter",
    container="Arc",
    region_label="Part",
    date="2026-08-26",
)

CHAPTERS = [
    dict(
        id="wdb", slug="01-where-dreams-began", wiki_page="Story#Where Dreams Began",
        region="Part 1", versions="not recorded",
        title="Where Dreams Began",
    ),
    dict(
        id="teod", slug="02-the-end-of-destiny", wiki_page="Story#The End of Destiny",
        region="Part 1", versions="not recorded",
        title="The End of Destiny",
    ),
    dict(
        id="utfs", slug="03-under-the-falling-sky",
        wiki_page="Story#Under the Falling Sky",
        region="Part 1", versions="not recorded - 3.0",
        title="Under the Falling Sky",
    ),
    dict(
        id="ftdo", slug="04-from-the-deep-ocean",
        wiki_page="Story#From the Deep Ocean",
        region="Part 1", versions="3.0 - 3.4",
        title="From the Deep Ocean",
    ),
    dict(
        id="shooting_star", slug="05-a-shooting-star",
        wiki_page="Story#A Shooting Star Streaking Across the Night",
        region="Part 1", versions="3.5 - 3.6",
        title="A Shooting Star Streaking Across the Night",
    ),
    dict(
        id="ety", slug="06-elegy-to-yesterday", wiki_page="Story#Elegy to Yesterday",
        region="Part 1", versions="3.8 - 4.0",
        title="Elegy to Yesterday",
    ),
    dict(
        id="hlb", slug="07-here-lies-bellflower",
        wiki_page="Story#Here Lies Bellflower",
        region="Part 1", versions="4.1 - 4.2",
        title="Here Lies Bellflower",
    ),
    dict(
        id="txd", slug="08-taixuan-dream", wiki_page="Story#Taixuan Dream",
        region="Part 1", versions="4.3 - 4.5",
        title="Taixuan Dream",
    ),
    dict(
        id="rf", slug="09-remaining-flames", wiki_page="Story#Remaining Flames",
        region="Part 1", versions="4.7 - 4.9",
        title="Remaining Flames",
    ),
    dict(
        id="tsa", slug="10-thus-spoke-apocalypse",
        wiki_page="Story#Thus Spoke Apocalypse",
        region="Part 1", versions="5.1 - 5.4",
        title="Thus Spoke Apocalypse",
    ),
    dict(
        id="ttf", slug="11-to-the-flawless", wiki_page="Story#To the Flawless",
        region="Part 1", versions="5.7 - 5.9",
        title="To the Flawless",
    ),
    dict(
        id="dotf", slug="12-the-day-of-transcending-finality",
        wiki_page="Story#The Day of Transcending Finality",
        region="Part 1", versions="6.0 - 6.4",
        title="The Day of Transcending Finality",
    ),
    dict(
        id="atfots", slug="13-at-the-fingertip-of-the-sea",
        wiki_page="Story#At the Fingertip of the Sea",
        region="Part 1.5", versions="6.5 - 6.8",
        title="At the Fingertip of the Sea",
    ),
    dict(
        id="bts", slug="14-beyond-the-stars", wiki_page="Story#Beyond the Stars",
        region="Part 1.5", versions="6.9 - 7.2",
        title="Beyond the Stars",
    ),
    dict(
        id="ttgb", slug="15-tides-of-time-gone-by",
        wiki_page="Story#Tides of Time Gone By",
        region="Part 2", versions="7.3 - 7.6",
        title="Tides of Time Gone By",
    ),
    dict(
        id="asuw", slug="16-a-shore-under-watch",
        wiki_page="Story#A Shore Under Watch",
        region="Part 2", versions="7.7",
        title="A Shore Under Watch",
    ),
    dict(
        id="datrow", slug="17-dawn-after-the-remaining-old-wish",
        wiki_page="Story#Dawn after the Remaining Old Wish",
        region="Part 2", versions="7.8 - 8.4",
        title="Dawn after the Remaining Old Wish",
    ),
    dict(
        id="aric", slug="18-a-rose-in-a-curtsy",
        wiki_page="Story#A Rose in a Curtsy",
        region="Part 2", versions="8.5 - 8.9",
        title="A Rose in a Curtsy",
    ),
]

# Nothing on this wiki records a requirement for entering a story chapter, so
# there is nothing to gate on and `gate_label` above is None.
GATES = {}
GATE_DEFAULT = {}
