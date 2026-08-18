"""This report's configuration and its authored prose.

The generic renderer in the skill's `gen_docs.py` reads everything game-specific
from here: what the questline and its level gate are called, which wiki page
documents the structure, and the framing prose the method text sits between.
No number is written down here; the prose carries placeholders that `facts.py`
fills at render time.
"""

REPORT = dict(
    title="Genshin Impact Archon Questline: How Long Each Act Takes",
    intro="Duration estimates for every main act of the Archon Quest storyline, \n"
          "from the Mondstadt Prologue to Chapter VII, \n"
          "each one backed by the YouTube playthroughs it was measured from.",
    # The wiki page that documents the questline as a whole, linked from the
    # method section and from every chapter's sources.
    overview_page="Archon Quest",
    # The account-level requirement acts are gated behind, as the game names it.
    # None for a game that gates its story some other way.
    gate_label="Adventure Rank",
    # What the searches in data/query_templates.txt do, in words.
    queries="For every act, YouTube was searched four ways: \n"
            "by chapter plus act label plus act title, by act title alone, \n"
            "and twice by the patch branding recent uploads use instead of act titles \n"
            "(\"Genshin Impact 6.6 Act 10 ...\").",
    # Two compilation titles this game's uploaders actually use, for the reader.
    compilations="\"Acts 9 & 10\" or \"Full Sumeru Archon Quest\"",
    # Limits of this report in particular, beyond the ones every report shares.
    caveats=[
        "The newest acts (Nod-Krai's later acts, Chapter VII) \n"
        "have the fewest uploads to draw on, \n"
        "so their figures are the softest. \n"
        "They are marked *low* or *medium* confidence accordingly.",
        "Interlude Chapter acts \n"
        "(*The Crane Returns on the Wind*, *Perilous Trail*, \n"
        "*Inversion of Genesis*, *Paralogism*) \n"
        "are Archon Quests but not part of the main chapter progression, \n"
        "so they are outside this report's scope.",
    ],
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="prologue", slug="00-prologue-mondstadt", wiki_page="Prologue", region="Mondstadt",
        versions="1.0",
        title="Prologue: The Outlander Who Caught the Wind",
        blurb="The Traveler is torn from their sibling by an unknown god, \n"
              "washes up in Mondstadt with Paimon, \n"
              "and gets pulled into the Knights of Favonius' struggle \n"
              "against the corrupted dragon Dvalin.",
        pacing="Every act here lands within about a quarter hour of an hour \n"
               "({shortest_len} to {longest_len}). \n"
               "Mondstadt is the tutorial region, \n"
               "so quest parts are small, combat is trivial at the intended Adventure Rank, \n"
               "and the walking distances are short. \n"
               "Expect roughly a single evening for the whole Prologue.",
    ),
    dict(
        id="ch1", slug="01-chapter-i-liyue", wiki_page="Chapter I", region="Liyue",
        versions="1.0 - 1.4",
        title="Chapter I: Farewell, Archaic Lord",
        blurb="Rex Lapis is apparently assassinated at the Rite of Descension, \n"
              "the Traveler is framed for it, \n"
              "and the investigation that follows ends with Morax handing his Gnosis \n"
              "to the Fatui of his own free will.",
        pacing="A clear step up from the Prologue: \n"
               "Acts II and III ({len_Act_II} and {len_Act_III}) \n"
               "roughly double the Prologue's per-act length, \n"
               "largely because of the Osial set piece and the Childe fight. \n"
               "Act IV - Prelude is a single conversation-heavy quest \n"
               "with Dainsleif, at {len_Act_IV_Prelude}.",
    ),
    dict(
        id="ch2", slug="02-chapter-ii-inazuma", wiki_page="Chapter II", region="Inazuma",
        versions="1.6 - 2.6",
        title="Chapter II: Omnipresence Over Mortals",
        blurb="Inazuma has sealed itself off under the Sakoku Decree \n"
              "and the Vision Hunt Decree. \n"
              "The Traveler joins the Watatsumi resistance, \n"
              "kills the Fatui Harbinger Signora in a duel, \n"
              "and confronts the Raiden Shogun over what eternity costs her people.",
        pacing="Uneven in a way the earlier chapters are not. \n"
               "Act I and Act III are marathon acts of {len_Act_I} and {len_Act_III}, \n"
               "while Act II consists of only {parts_Act_II} quest parts \n"
               "and takes {len_Act_II}. \n"
               "Act IV (Enkanomiya) arrived much later than the rest \n"
               "and plays as a compact epilogue.",
    ),
    dict(
        id="ch3", slug="03-chapter-iii-sumeru", wiki_page="Chapter III", region="Sumeru",
        versions="3.0 - 3.5",
        title="Chapter III: Truth Amongst the Pages of Purana",
        blurb="The Akademiya has locked Sumeru's Archon away and rules through the Akasha. \n"
              "The Traveler frees Nahida from a looping dream, \n"
              "crosses the desert with Cyno and Candace, \n"
              "and storms the Divine Throne to break the Akademiya's god-making project.",
        pacing="Where the questline changes scale, \n"
               "with {n_above_2h} of the {n_entries} acts past two hours \n"
               "and Act V as the chapter centrepiece at {len_Act_V}. \n"
               "Sumeru also adds heavy traversal, \n"
               "so uploads vary more here than in earlier chapters.",
    ),
    dict(
        id="ch4", slug="04-chapter-iv-fontaine", wiki_page="Chapter IV", region="Fontaine",
        versions="4.0 - 4.7",
        title="Chapter IV: Masquerade of the Guilty",
        blurb="A prophecy says Fontaine will dissolve into the waters. \n"
              "Between courtroom trials, a prison at the bottom of the sea, \n"
              "and a rising primordial tide, \n"
              "the Traveler uncovers Furina's five-hundred-year performance \n"
              "and watches Focalors execute herself to void the prophecy.",
        pacing="The most consistently long chapter, \n"
               "with {n_above_2h} of its {n_entries} acts above two hours \n"
               "and Act V, at {len_Act_V}, as its centrepiece. \n"
               "Fontaine's acts are cutscene-dense rather than traversal-dense, \n"
               "which is why the sampled uploads agree as closely as they do.",
    ),
    dict(
        id="ch5", slug="05-chapter-v-natlan", wiki_page="Chapter V", region="Natlan",
        versions="5.0 - 5.7",
        title="Chapter V: Incandescent Ode of Resurrection",
        blurb="Natlan fights the Abyss with Ancient Names borrowed from the Night Kingdom. \n"
              "The Traveler joins the tribes, loses Capitano as an ally, \n"
              "and learns what Mavuika has been quietly paying \n"
              "to keep the Sacred Flame burning.",
        pacing="Uniformly long without any single outlier: \n"
               "the numbered acts run from {acts_low} to {acts_high}. \n"
               "The Interlude is the exception, \n"
               "a {parts_Interlude}-part cooldown quest of {len_Interlude}. \n"
               "Natlan's mobility gadgets keep traversal overhead lower \n"
               "than Sumeru's despite the map size.",
    ),
    dict(
        id="sotwm", slug="06-song-of-the-welkin-moon-nod-krai", wiki_page="Song of the Welkin Moon", region="Nod-Krai, later Sumeru",
        versions="5.8 - Luna VII (6.x)",
        title="Song of the Welkin Moon (unofficially Chapter VI)",
        blurb="Ineffa leads the Traveler out of Natlan to Nod-Krai, \n"
              "where the Wild Hunt, the Fatui, and the history of Teyvat's three moons \n"
              "converge on Columbina's fading identity. \n"
              "The final two acts return to Sumeru \n"
              "and finally deliver the Chapter III title drop.",
        pacing="By far the largest chapter: {n_entries} entries, \n"
               "and a running time of {total}, \n"
               "comparable to Sumeru and Fontaine combined. \n"
               "Act I alone runs {len_Act_I}. \n"
               "The later acts are also the most recent content sampled, \n"
               "so their evidence pools are the thinnest and their spreads the widest.",
    ),
    dict(
        id="ch7", slug="07-chapter-vii-snezhnaya", wiki_page="Chapter VII", region="Snezhnaya",
        versions="7.0",
        title="Chapter VII: Everwinter Without Mercy",
        blurb="The Traveler reaches Snezhnaya, \n"
              "where the Tsaritsa has been gathering the Gnoses \n"
              "and where the sibling's requested journey was always meant to end.",
        pacing="Only {n_entries} acts exist so far, \n"
               "but both are long: {len_Act_I} and {len_Act_II}. \n"
               "This is the newest content in the sample, \n"
               "and several uploads bundle both acts together, \n"
               "so per-act figures rest on a smaller pool than the older chapters.",
    ),
]

# One line per act, keyed "<chapter id>|<act label>".
ACT_NOTES = {
    "prologue|Act I": "Arrival in Mondstadt with Amber, the first Stormterror attack, \n"
                      "and the introduction to the Knights of Favonius.",
    "prologue|Act II": "Venti reveals himself, \n"
                       "the Abyss Order's hand in Dvalin's corruption comes to light, \n"
                       "and the attempt to reach the dragon through his memories fails.",
    "prologue|Act III": "The Holy Lyre is recovered, \n"
                        "Dvalin is freed at the Light Guiding Ceremony, \n"
                        "and Signora takes Barbatos' Gnosis.",
    "ch1|Act I": "The Rite of Descension goes wrong, \n"
                 "Rex Lapis falls, \n"
                 "and the Traveler flees the Millelith as the prime suspect.",
    "ch1|Act II": "Working the funeral rites with Zhongli: \n"
                  "the three perfumes, Guizhong's memory, \n"
                  "and a lesson in what contracts mean in Liyue.",
    "ch1|Act III": "Osial rises, the Jade Chamber falls, \n"
                   "Childe is beaten, \n"
                   "and Zhongli reveals that the whole thing was his own retirement plan.",
    "ch1|Act IV - Prelude": "A single quest: Dainsleif introduces himself \n"
                            "and the Khaenri'ah backstory behind the Abyss Order.",
    "ch1|Act IV": "Dainsleif leads the Traveler to the Abyss Order's ritual, \n"
                  "where the sibling is revealed as its leader.",
    "ch2|Prologue": "Kazuha, Beidou, and the Crux run the Thunder Sword barrier \n"
                    "to get the Traveler into a sealed Inazuma.",
    "ch2|Act I": "Ritou, the Sacred Sakura Cleansing Ritual, \n"
                 "and a first audience with the Raiden Shogun that ends in defeat.",
    "ch2|Act II": "Only {parts_Act_II} quest parts: \n"
                  "joining Sangonomiya Kokomi's resistance \n"
                  "and uncovering the Delusion factory.",
    "ch2|Act III": "Yae Miko opens the way into the Plane of Euthymia, \n"
                   "Signora dies in a duel, \n"
                   "and the Vision Hunt Decree is repealed.",
    "ch2|Act IV": "Enkanomiya, the Black Serpent Knights, \n"
                  "and Dainsleif's account of the sibling's part in the cataclysm.",
    "ch3|Act I": "Arrival in the rainforest with Collei and Tighnari: \n"
                 "the Withering, Eleazar, the Aranara, \n"
                 "and the Akasha's grip on Sumeru City.",
    "ch3|Act II": "The Sabzeruz Festival repeats itself until the Traveler breaks the loop \n"
                  "and pulls Nahida out of the Akademiya's dream.",
    "ch3|Act III": "Nahida joins the party properly, \n"
                   "and the Akademiya's god-making project behind Scaramouche surfaces.",
    "ch3|Act IV": "Into the desert with Cyno and Candace, \n"
                  "chasing King Deshret's legacy and the cause of Eleazar.",
    "ch3|Act V": "The assault on the Divine Throne: \n"
                 "Shouki no Kami, one of Dottore's segments, \n"
                 "and Nahida taking back the Akasha.",
    "ch3|Act VI": "Traveler chapter: Dainsleif, Kaeya, \n"
                  "and the sinner Caribert at the edge of Khaenri'ah.",
    "ch4|Act I": "Fontaine, Lyney and Lynette, \n"
                 "and an opera-house trial over the stolen Hydro Gnosis.",
    "ch4|Act II": "Furina and Neuvillette, the Oratrice, \n"
                  "and a trial that sentences the Traveler to the Fortress of Meropide.",
    "ch4|Act III": "Life under Wriothesley in Meropide, \n"
                   "the escape, \n"
                   "and the first hard evidence for the prophecy of dissolution.",
    "ch4|Act IV": "Elynas and the Melusines, Childe underwater, \n"
                  "and the primordial sea beginning to rise.",
    "ch4|Act V": "The flood, Furina's five-hundred-year act, \n"
                 "Focalors' self-execution, \n"
                 "and Neuvillette taking the seat of judgment.",
    "ch4|Act VI": "Traveler chapter: a cold case in Fontaine \n"
                  "that turns into memories that should not exist.",
    "ch5|Act I": "Farewells in Fontaine, then Natlan: \n"
                 "Mualani, Kachina, Ancient Names, \n"
                 "and the pilgrimage of the Sacred Flame.",
    "ch5|Act II": "The Ode of Resurrection fails to bring Kachina back, \n"
                  "and the Abyss turns out to have tailored a disaster for every tribe.",
    "ch5|Act III": "Mavuika mobilizes the tribes and the Adventurers' Guild together \n"
                   "while Capitano's purpose in Natlan comes into focus.",
    "ch5|Act IV": "The strike against the Fatui and the Secret Source, \n"
                  "the Abyss' full assault, \n"
                  "and Capitano's end.",
    "ch5|Interlude": "Just {parts_Interlude} quest part: \n"
                     "the tribes rebuild after the invasion. \n"
                     "A deliberate cooldown between Act IV and Act V.",
    "ch5|Act V": "The Night Kingdom, the truth about Mavuika's bargain, \n"
                 "and the price already paid for the Ode of Resurrection.",
    "ch5|Act VI": "Traveler chapter: the Loom of Fate \n"
                  "and the closest thing yet to a reunion with the sibling.",
    "sotwm|Prelude": "Still in Natlan: rogue Secret Source Automatons, \n"
                     "and a strange woman washed ashore looking for someone. \n"
                     "Ineffa's introduction.",
    "sotwm|Act I": "Departure from Natlan and arrival in Nod-Krai, \n"
                   "with Sandrone already tracking the Traveler.",
    "sotwm|Act II": "Nasha Town under Wild Hunt incursion, \n"
                    "the Kuuvahki Cannon repair, \n"
                    "and Rerir regaining physical form.",
    "sotwm|Act III": "Hunting Rerir across the kuuvahki-rich islands \n"
                     "with Flins, Aino, Lauma, and Jahoda.",
    "sotwm|Act IV": "Columbina in tow, Albedo and Durin return, \n"
                    "Arlecchino and Sandrone circle each other, \n"
                    "and fate starts closing in.",
    "sotwm|Act V": "Only {parts_Act_V} quest parts, around Moon-Prayer Night, \n"
                   "with Columbina weakening after the fight with Rerir.",
    "sotwm|Act VI": "The Hyperborean ruins, \n"
                    "the full history of Teyvat's three moons, \n"
                    "and the search for Columbina's true name.",
    "sotwm|Act VII": "North to Dottore's lab with the Fatui as temporary allies.",
    "sotwm|Act VIII": "Dottore's realm, his offer refused, \n"
                      "the Wanderer's rescue, \n"
                      "and the Welkin Moon's homecoming.",
    "sotwm|Act IX": "Back to Sumeru through Collei's letter: \n"
                    "identities in Sumeru City have been switched around.",
    "sotwm|Act X": "Kaveh, Alhaitham, and Thoth open the Aaru, \n"
                   "and Chapter III finally gets its title drop.",
    "ch7|Act I": "Farewell at The Flagship, then into Snezhnaya, \n"
                 "where Paimon starts feeling the cold in a way she should not.",
    "ch7|Act II": "The Korolevskiy Theater, Lelek's confession, \n"
                  "and the ballet that stops mid-performance.",
}

# Adventure Rank gates, from the Archon Quest overview page.
GATES = {
    "prologue|Act I": "-", "prologue|Act II": "10", "prologue|Act III": "18",
    "ch1|Act I": "23", "ch1|Act II": "25", "ch1|Act III": "28",
    "ch1|Act IV - Prelude": "28", "ch1|Act IV": "28",
    "ch7|Act I": "18", "ch7|Act II": "-",
}
GATE_DEFAULT = {"ch2": "30", "ch3": "35", "ch4": "40", "ch5": "40", "sotwm": "40"}
