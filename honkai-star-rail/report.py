"""This report's configuration and its authored prose.

The generic renderer in the skill's `gen_docs.py` reads everything game-specific
from here: what the questline and its level gate are called, which wiki page
documents the structure, and the framing prose the method text sits between.
No number is written down here; the prose carries placeholders that `facts.py`
fills at render time.

Terminology: the wiki calls one Trailblaze Mission a chapter and numbers them
game-wide, first to twenty-sixth. This report groups them by the world they take
place on, so a chapter here is a world and a mission is what the wiki numbers.
"""

REPORT = dict(
    title="Honkai: Star Rail Trailblaze Missions: How Long Each Mission Takes",
    intro="Duration estimates for every Trailblaze Mission of the main storyline, \n"
          "from the Herta Space Station to Planarcadia, \n"
          "each one backed by the YouTube playthroughs it was measured from.",
    # The wiki page that documents the questline as a whole, linked from the
    # method section and from every chapter's sources.
    overview_page="Trailblaze Mission",
    # The account-level requirement acts are gated behind, as the game names it.
    # Two names for it here, Trailblaze Level and Equilibrium Level, so the
    # values carry the name and the label stays the neutral half.
    gate_label="Level",
    # What this game numbers its acts with, and what the entry count counts,
    # for the renderer's own headings.
    unit="Mission",
    entries_are="missions",
    # What the searches in data/query_templates.txt do, in words.
    queries="For every mission, YouTube was searched four ways: \n"
            "by world plus mission title, by mission title alone, \n"
            "and twice by the patch branding recent uploads use instead of mission titles \n"
            "(\"Honkai: Star Rail 4.4 Planarcadia Trailblaze Mission Walkthrough\").",
    # Two compilation titles this game's uploaders actually use, for the reader.
    compilations="\"Full Amphoreus Trailblaze Quest\" or \"100% all missions\"",
    # The mirror image, in this game's wording. Optional; a game whose uploaders
    # do not split an act across uploads leaves it out.
    partials="uploads covering part of a mission rather than all of it, \n"
             "which in this game means both the numbered kind (\"Part 3\") \n"
             "and the kind titled after a single quest part of the mission, \n"
             "unless their runtime says they cover the mission after all",
    # Limits of this report in particular, beyond the ones every report shares.
    caveats=[
        "The 1.0 missions are the hardest of all to measure. \n"
        "The uploads that exist are the oldest on YouTube, \n"
        "and the convention then was to cut a mission into scene-length videos, \n"
        "so *In the Withering Wintry Night* in particular \n"
        "rests on a small pool of genuinely complete runs.",
        "Planarcadia is the newest content sampled. \n"
        "Walkthrough channels covered it thoroughly, \n"
        "so the pools are not thin, \n"
        "but they have had the least time to settle, \n"
        "and the accepted uploads of its opening mission \n"
        "still disagree by a factor of two.",
        "Astropolis and its mission *To Roll the Stars in Astropolis* \n"
        "are still upcoming content at the time of writing (Version 4.5), \n"
        "so there is nothing to measure yet.",
        "*Memories are the Prelude to Dreams* is a Finality Mission: \n"
        "supplemental Penacony story released long after the world was finished. \n"
        "The Trial of Equilibrium missions are level-cap trials \n"
        "rather than story. \n"
        "Neither is part of the main progression, \n"
        "so both are outside this report's scope.",
    ],
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="herta", slug="00-herta-space-station", wiki_page="Herta Space Station",
        region="Herta Space Station",
        versions="1.0",
        title="Herta Space Station",
        blurb="A strange woman arrives at the Space Station at 23:44:59 system time, \n"
              "leaves a Stellaron in the Trailblazer's chest, \n"
              "and the Astral Express crew picks up a new passenger on the way out.",
        pacing="The game's tutorial world, and the only one with a single mission. \n"
               "{len_Mission_1} covers the Stellaron, Kafka and the departure, \n"
               "which makes this the shortest chapter in the report by a wide margin \n"
               "and the only one that fits into an evening.",
    ),
    dict(
        id="jarilo", slug="01-jarilo-vi", wiki_page="Jarilo-VI",
        region="Jarilo-VI: Belobog and the Underworld",
        versions="1.0",
        title="Jarilo-VI",
        blurb="A planet buried under an eternal blizzard, \n"
              "where a walled city rations its warmth \n"
              "and the people it locked underground have built their own. \n"
              "The Trailblazer arrives in the middle of both, \n"
              "and ends up deciding how the two halves of Belobog settle it.",
        pacing="Two missions, split by the descent into the Underworld: \n"
               "{len_Mission_1} and {len_Mission_2}. \n"
               "The opener is the longer of the two, \n"
               "and the one the Trailblaze Level gate sits inside; \n"
               "the second is a straight run at Cocolia \n"
               "and ends the world on its boss fight. \n"
               "Both figures are the softest in the report, \n"
               "for the reason given under the caveats in \n"
               "[README.md](README.md).",
    ),
    dict(
        id="luofu", slug="02-xianzhou-luofu", wiki_page="The Xianzhou Luofu",
        region="The Xianzhou Luofu",
        versions="1.0 - 1.3",
        title="The Xianzhou Luofu",
        blurb="A generation ship of immortals with a Stellaron in its hold \n"
              "and a sacred tree growing again after centuries of being dead. \n"
              "The Stellaron Hunters wanted the Trailblazer here for a reason, \n"
              "and it takes all three missions for that reason to surface.",
        pacing="A long opening mission and then a steep taper: \n"
               "{len_Mission_1}, {len_Mission_2}, {len_Mission_3}. \n"
               "The Luofu was released over four versions rather than in one drop, \n"
               "and the last mission is an epilogue of \n"
               "{parts_Mission_3} quest part, \n"
               "the shortest entry in the game.",
    ),
    dict(
        id="penacony", slug="03-penacony", wiki_page="Penacony",
        region="Penacony, the Land of Dreams",
        versions="2.0 - 2.7",
        title="Penacony",
        blurb="A hedonistic dream resort throws a Charmony Festival, \n"
              "two murders happen that could not have happened, \n"
              "and everyone at the banquet turns out to be working an angle \n"
              "on the Watchmaker's legacy.",
        pacing="Where the questline changes scale. \n"
               "{n_above_3h} of Penacony's {n_entries} missions run past three hours, \n"
               "where before it only Jarilo-VI and the Luofu \n"
               "had one at all, \n"
               "and *{longest_title}* alone takes {longest_len}. \n"
               "The last two missions are the wind-down, \n"
               "at {len_Mission_4} and {len_Mission_5}.",
    ),
    dict(
        id="amphoreus", slug="04-amphoreus", wiki_page="Amphoreus",
        region="Amphoreus, the Eternal Land",
        versions="3.0 - 3.7",
        title="Amphoreus",
        blurb="A world locked in a doomed cycle, \n"
              "where twelve Chrysos Heirs chase Coreflames \n"
              "to buy their land one more dawn. \n"
              "The Express arrives near the end of the last cycle \n"
              "and stays for all of it.",
        pacing="By far the largest chapter: \n"
               "{n_entries} missions and {total} in total, \n"
               "released across the whole of the 3.x cycle. \n"
               "Every one of them runs past three hours. \n"
               "*{longest_title}*, the arrival on Amphoreus, is the longest \n"
               "at {longest_len}, \n"
               "and even the shortest, *{shortest_title}*, takes {shortest_len}.",
    ),
    dict(
        id="planarcadia", slug="05-planarcadia", wiki_page="Planarcadia",
        region="Planarcadia",
        versions="4.0 - 4.4",
        title="Planarcadia",
        blurb="A paradise inside a painted scroll, \n"
              "with a vacant divine throne and a reward for whoever entertains \n"
              "the masses best. \n"
              "Everyone wears a mask, the Fool works the crowd, \n"
              "and Elation turns out to have a bill attached.",
        pacing="The opening mission is the longest, at {longest_len}, \n"
               "and the four after it settle between \n"
               "{shortest_len} and {len_Mission_2}. \n"
               "This is also the newest content in the sample, \n"
               "so its evidence pools are the youngest \n"
               "and its figures the least settled.",
    ),
]

# One line per mission, keyed "<chapter id>|<mission label>".
# The framing follows the mission's own description on the wiki.
ACT_NOTES = {
    "herta|Mission 1": "The Stellaron in the Space Station, \n"
                       "Kafka's visit, \n"
                       "and the Trailblazer's first departure aboard the Astral Express.",
    "jarilo|Mission 1": "Arrival on a frozen planet, \n"
                        "the descent into the Underworld, \n"
                        "and the fight to free its people from the cage Svarog built \n"
                        "to keep them safe.",
    "jarilo|Mission 2": "Back to the Overworld to face Cocolia, \n"
                        "the ruler who was preserving Belobog's freedom \n"
                        "by handing the planet to the Stellaron.",
    "luofu|Mission 1": "The Express is diverted to the Luofu, \n"
                       "where the Mara-struck, the Cloud Knights \n"
                       "and a stirring Ambrosial Arbor \n"
                       "all point at the same buried problem.",
    "luofu|Mission 2": "Someone else brought a Stellaron aboard, \n"
                       "the Arbor is growing again, \n"
                       "and the Stellaron Hunters' reason for luring the Trailblazer here \n"
                       "finally surfaces.",
    "luofu|Mission 3": "A single quest part: \n"
                       "the clean-up after the Arbor goes quiet, \n"
                       "and goodbyes on the Luofu.",
    "penacony|Mission 1": "Into the Dreamscape for the Charmony Festival, \n"
                          "and a first pass through Penacony's guests, \n"
                          "hosts and Family, \n"
                          "ending on a murder that cannot have happened.",
    "penacony|Mission 2": "Two impossible murders and two guests with no interest \n"
                          "in the legacy, \n"
                          "who between them start prying open \n"
                          "the mystery of the Watchmaker.",
    "penacony|Mission 3": "The banquet's long middle, \n"
                          "the Great Septimus, \n"
                          "and the sense of rowing against a current \n"
                          "that keeps pulling everyone back into the past.",
    "penacony|Mission 4": "The final encore on the stage of dreams: \n"
                          "the Family's accounts settled, \n"
                          "and everyone heading for their next stop.",
    "penacony|Mission 5": "A late return to the Dreamscape. \n"
                          "Some come back, some leave for good, \n"
                          "and seeing the way ahead means looking back first.",
    "amphoreus|Mission 1": "The Express reaches the Eternal Land \n"
                           "where three Paths intersect, \n"
                           "and joins the flame-chase \n"
                           "that Amphoreus has been running for longer than anyone admits.",
    "amphoreus|Mission 2": "The homecoming is exiled and the departing set out: \n"
                           "one generation of Chrysos Heirs rises \n"
                           "as another wilts.",
    "amphoreus|Mission 3": "Across the River of Souls into the land of repose, \n"
                           "among the Antila flowers, \n"
                           "the dead of the past and the wanderers of the future.",
    "amphoreus|Mission 4": "For a new sun to rise, \n"
                           "the sky's last eye has to be put out. \n"
                           "The mission that turns the cycle over.",
    "amphoreus|Mission 5": "The Paean of Era Nova, \n"
                           "and the shortest mission on Amphoreus: \n"
                           "the nymphs' chase of the scorching dawn, \n"
                           "told in {parts_Mission_5} quest parts.",
    "amphoreus|Mission 6": "Countless embers over the firmament, \n"
                           "and the one star that has stayed constant through all of it.",
    "amphoreus|Mission 7": "Night wanes, the outlanders march without rest, \n"
                           "and the reunion is set for the edge of the world \n"
                           "where the morning star rises.",
    "amphoreus|Mission 8": "The close of the Amphoreus saga, \n"
                           "asked to be remembered rather than mourned.",
    "planarcadia|Mission 1": "Arrival in the painted paradise: \n"
                             "Phantasmoon, imagenesis, \n"
                             "and the reward THEY left behind \n"
                             "for anyone who wants a minute of godhood.",
    "planarcadia|Mission 2": "Happiness painted over pain, \n"
                             "the living seeking justice for the dead, \n"
                             "and a hero's name that some carry and some betray.",
    "planarcadia|Mission 3": "Near the spire's peak the Fool works the crowd \n"
                             "like a marionette theater, \n"
                             "handing out the freedom of Elation \n"
                             "and the chains that come with it.",
    "planarcadia|Mission 4": "Down to the painting's edge \n"
                             "where the Lethe runs and memories surface, \n"
                             "among wanderers looking for a last rest.",
    "planarcadia|Mission 5": "The Navigator sets a course for the apocalypse, \n"
                             "and only the Trailblaze finds a way through \n"
                             "the realm of death.",
}

# The wiki records a level requirement for two missions only, both on Jarilo-VI,
# and both partway through rather than at the mission's start.
GATES = {
    "jarilo|Mission 1": "Trailblaze Level 13, partway through",
    "jarilo|Mission 2": "Equilibrium Level 1",
}
GATE_DEFAULT = {}
