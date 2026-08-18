"""This report's configuration and its authored prose.

The generic renderer in the skill's `gen_docs.py` reads everything game-specific
from here: what the questline and its level gate are called, which wiki page
documents the structure, and the framing prose the method text sits between.
No number is written down here; the prose carries placeholders that `facts.py`
fills at render time.

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
    title="Zenless Zone Zero, Phaethon's Story: How Long Each Chapter Takes",
    intro="Duration estimates for every chapter of the main story, \n"
          "from the prologue on Sixth Street to the newest season in Roscaelifer, \n"
          "each one backed by the YouTube playthroughs it was measured from.",
    # The wiki page that documents the questline as a whole, linked from the
    # method section and from every chapter's sources.
    overview_page="Phaethon's Story",
    # Zenless Zone Zero gates story progress behind Inter-Knot Level and the
    # Rank-Up commissions, but the wiki records no requirement per chapter, so
    # there is nothing to put in a gate column. See the caveats.
    gate_label=None,
    # What this game numbers its acts with, and what the entry count counts,
    # for the renderer's own headings.
    unit="Chapter",
    entries_are="chapters, interludes and epilogues",
    # What the searches in data/query_templates.txt do, in words.
    queries="For every chapter, YouTube was searched four ways: \n"
            "by season plus chapter number plus chapter title, \n"
            "by chapter title alone, \n"
            "and twice by the patch branding recent uploads use \n"
            "instead of chapter titles \n"
            "(\"Zenless Zone Zero 3.1 Season 3 Chapter 2 full quest gameplay\").",
    # Two compilation titles this game's uploaders actually use, for the reader.
    compilations="\"Full Season 1 Story\" or \"all main stories\"",
    # The mirror image, in this game's wording. Optional; a game whose uploaders
    # do not split an act across uploads leaves it out.
    partials="uploads covering part of a chapter rather than all of it, \n"
             "which in this game means the numbered kind \n"
             "(\"Part 3\", \"Episode 4\", \"1/2\"), \n"
             "unless their runtime says they cover the chapter after all",
    # Limits of this report in particular, beyond the ones every report shares.
    caveats=[
        "Season 1 ships each chapter in two halves, (A) and (B), \n"
        "released together and played back to back. \n"
        "Almost nobody titles an upload after one half, \n"
        "so a Season 1 figure here covers the whole chapter, both halves. \n"
        "The two epilogues are the exception: \n"
        "their halves shipped a version apart, \n"
        "their uploads say which half they are, \n"
        "and they are counted as two entries.",
        "Season 1 is the softest part of this report, \n"
        "and its figures should be read as a range rather than as an estimate. \n"
        "Dialogue is skippable in this game and a great deal of Season 1 is dialogue, \n"
        "so the same chapter takes one uploader an hour and another three; \n"
        "the pools are also the oldest and the thinnest, \n"
        "and *A Call From the Hollow's Heart* in particular \n"
        "rests on a handful of complete runs. \n"
        "Where a median moved once the queries were widened, \n"
        "the confidence rating says so.",
        "The game gates chapters behind Inter-Knot Level \n"
        "and the Rank-Up commissions that raise Inter-Knot Reputation Rank, \n"
        "but the wiki documents no level requirement per chapter, \n"
        "so this report has no gate column. \n"
        "What it does document is the other direction: \n"
        "the Senior Proxy rank-up requires the Chapter 2 Interlude commission \n"
        "*Invisible Assistant*.",
        "The prologue and Chapter 1 are categorized on the wiki \n"
        "under version 0.13, the 2022 Tuning Test closed beta \n"
        "in which they were first shown. \n"
        "Players met them at the 1.0 release on 2024-07-04, \n"
        "which is what the season's version range says instead.",
        "Chapter markers are rarer here than in any other game in this repository, \n"
        "and where they exist they usually mark single steps \n"
        "rather than the episodes a chapter is divided into. \n"
        "Almost every figure in this report is therefore whole-video runtime, \n"
        "not a span located inside a longer upload.",
        "Season 3 is still being released. \n"
        "*The Long Goodbye* (3.1) is the newest chapter at the time of writing, \n"
        "and there is nothing to measure beyond it yet.",
    ],
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="s1", slug="01-season-1", wiki_page="Season 1",
        region="New Eridu: Sixth Street, Lumina Square and the Outer Ring",
        versions="1.0 - 1.7",
        title="Season 1",
        blurb="A brother and sister run a video store on Sixth Street by day \n"
              "and smuggle people through the Hollows as Phaethon by night. \n"
              "The commissions start with a lost cat and a gang of Ether-addled thugs, \n"
              "and by the end of the season \n"
              "the city's factions, its police and its corporations \n"
              "are all pulling at the same thread.",
        pacing="The season the game teaches you with, \n"
               "and by a distance the cheapest to get through: \n"
               "{n_entries} entries and {total} in total. \n"
               "The two epilogue halves stand apart from the rest, \n"
               "at {len_Epilogue_A} and {len_Epilogue_B}; \n"
               "everything before them sits between {shortest_len} \n"
               "and {len_Chapter_4}. \n"
               "These are also the least settled figures in the report: \n"
               "Season 1 is mostly dialogue, dialogue is skippable, \n"
               "and the uploads disagree accordingly. \n"
               "See the caveats in [README.md](README.md).",
    ),
    dict(
        id="s2", slug="02-season-2", wiki_page="Season 2",
        region="Waifei Peninsula: Yunkui Summit and Suibian Temple",
        versions="2.0 - 2.8",
        title="Season 2",
        blurb="Neon and asphalt give way to cloud-covered mountains, \n"
              "a temple in disrepair and a disciple who insists on repairing it. \n"
              "What looks like a change of scenery turns into \n"
              "the aftermath of an old calamity \n"
              "that the peninsula has been outrunning for generations.",
        pacing="Where the story changes scale: \n"
               "{n_above_3h} of Season 2's {n_entries} entries run past three hours, \n"
               "and *{longest_title}*, the season's climax, \n"
               "alone takes {longest_len}: \n"
               "the longest single entry in the game. \n"
               "Around it the season is remarkably even, \n"
               "every other entry landing between {len_Epilogue_B} \n"
               "and {len_Interlude}.",
    ),
    dict(
        id="s3", slug="03-season-3", wiki_page="Season 3",
        region="Roscaelifer",
        versions="3.0 - 3.1",
        title="Season 3",
        blurb="Roscaelifer, where the Proxy meets a version of themselves \n"
              "inside a dream that nobody wakes from, \n"
              "and the season opens with a confession \n"
              "that nobody is quite awake to hear.",
        pacing="Still being released: {n_entries} chapters so far, \n"
               "{total} between them, at {len_Chapter_1} and {len_Chapter_2}. \n"
               "Both were written at the Season 2 scale rather than the Season 1 one, \n"
               "and both are recent enough \n"
               "that their evidence pools have had the least time to settle.",
    ),
]

# One line per chapter, keyed "<season id>|<chapter label>". Where the wiki gives
# the chapter a description of its own, the note follows it.
ACT_NOTES = {
    "s1|Chapter 0": "The prologue: a Hollow, a Bangboo, \n"
                    "and the two halves of Phaethon meeting the client \n"
                    "who turns the video store into a business.",
    "s1|Chapter 1": "A lost cat, a client with two tails, \n"
                    "and an escort job through an abandoned rally point \n"
                    "that turns out to be about \n"
                    "what a Vagrant left behind rather than what was lost.",
    "s1|Chapter 1 Intermission": "A restricted area, \n"
                                 "an encounter that should not be there, \n"
                                 "and a pursuit the game does not tell you \n"
                                 "was a chapter of its own until it is over.",
    "s1|Chapter 2": "Belobog Heavy Industries takes a commission it cannot finish, \n"
                    "and the Proxy walks into a Hollow \n"
                    "with a prototype, two sisters and a Steel Devourer in it.",
    "s1|Chapter 2 Interlude": "The Public Security Bureau's turn: \n"
                              "a theft case on Sixth Street, \n"
                              "an unexpected reunion, \n"
                              "and the commission *Invisible Assistant*, \n"
                              "which the game also uses \n"
                              "as the gate to the Senior Proxy rank.",
    "s1|Chapter 3": "A mysterious letter, a perilous building, \n"
                    "and Victoria Housekeeping cleaning up something \n"
                    "far darker than a hotel.",
    "s1|Chapter 4": "Out past the city into Cinder Lake, \n"
                    "where the Sons of Calydon race, \n"
                    "the legends are louder than the facts, \n"
                    "and the flames turn out to be someone's business plan.",
    "s1|Chapter 5": "Strike down the schemes threatening New Eridu \n"
                    "like a bolt of lightning: \n"
                    "a temporary partner, a falling star, \n"
                    "and the Bringer's scheme underneath both.",
    "s1|Epilogue (A)": "Through his veins flows a curse called \"fate\". \n"
                       "The first half of the Season 1 epilogue: \n"
                       "a gentleman's visit, a raffle, \n"
                       "and a phantom thief working the moonlight.",
    "s1|Epilogue (B)": "She foresaw hardship, \n"
                       "but \"destiny\" would rather sing an ode to hope. \n"
                       "The second half closes Season 1 \n"
                       "on the Mockingbird and the sacrifice core.",
    "s2|Chapter 1": "The vestiges of a past calamity herald the beginning of another. \n"
                    "Arrival on the Waifei Peninsula, \n"
                    "and a restoration project at Suibian Temple \n"
                    "that nobody but its disciple believes in.",
    "s2|Chapter 2": "Echoes of the aftermath linger, \n"
                    "as destiny treads softly back to shore. \n"
                    "A safety inspection, a pursuit across Sailume Bay, \n"
                    "and the source of the Obscuras.",
    "s2|Chapter 3": "The embers of last night still linger, \n"
                    "spoiling the calm of a quiet dream. \n"
                    "The winner's rules, a soldier's creed, \n"
                    "and a story that refuses to end where it should.",
    "s2|Chapter 4": "The pain of being awake comes from dreams that once existed. \n"
                    "A town that should not be inhabited, \n"
                    "a slumbering mystery underneath it, \n"
                    "and a rescue that costs more than it saves.",
    "s2|Chapter 5": "When you gaze into the abyss, the abyss gazes back. \n"
                    "A new resident, dark tides, \n"
                    "and the question of who has been watching all along.",
    "s2|Chapter 6": "Even in the depth of the abyss, sparks can light up the night. \n"
                    "The season's climax: \n"
                    "the storm, the Creator, and the end of Season 2's arc.",
    "s2|Interlude": "Once old dreams fade into the night, \n"
                    "we'll reunite in the delusions of dawn. \n"
                    "A festival commission that turns into \n"
                    "a case about the Construct series.",
    "s2|Epilogue (A)": "Yet now, the past buries its champions. \n"
                       "The Hollow Champion Competition starts, \n"
                       "a ragtag crew signs up, \n"
                       "and the first stage goes about as well as expected.",
    "s2|Epilogue (B)": "The sun sets in the lowly west. \n"
                       "Who here is awaiting the night? \n"
                       "Looking for Ramiel, and the last word on the competition.",
    "s3|Chapter 1": "I dreamed of another me, \n"
                    "in a dream I would never wake up from. \n"
                    "Landing in Roscaelifer, \n"
                    "where the trouble starts before the luggage is unpacked.",
    "s3|Chapter 2": "Fate plucks the strings. \n"
                    "Is this the prelude to tomorrow, or the finale of farewell? \n"
                    "A visitor from beyond the curtain, \n"
                    "the En-Nah Gang of the Retroflux Zone, \n"
                    "and a game that was checkmated before it began.",
}

# The wiki records no Inter-Knot Level requirement per chapter, so there is no
# gate column to fill; gate_label above is None and these stay empty.
GATES = {}
GATE_DEFAULT = {}
