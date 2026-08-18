"""Authored prose for the report: chapter framing and per-act one-liners."""

CHAPTERS = [
    dict(
        id="prologue", slug="00-prologue-mondstadt", wiki_page="Prologue", region="Mondstadt",
        versions="1.0",
        title="Prologue: The Outlander Who Caught the Wind",
        blurb="The Traveler is torn from their sibling by an unknown god, \n"
              "washes up in Mondstadt with Paimon, \n"
              "and gets pulled into the Knights of Favonius' struggle \n"
              "against the corrupted dragon Dvalin.",
        pacing="Every act here lands within about a quarter hour of an hour. \n"
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
               "Acts II and III roughly double the Prologue's per-act length, \n"
               "largely because of the Osial set piece and the Childe fight. \n"
               "Act IV - Prelude is the shortest entry in the entire questline, \n"
               "a single conversation-heavy quest with Dainsleif.",
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
        pacing="The most uneven chapter in the game. \n"
               "Act I and Act III are marathon acts of two and a half to three hours, \n"
               "while Act II consists of only two quest parts \n"
               "and takes well under an hour. \n"
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
        pacing="Where the questline changes scale. \n"
               "Four of the six acts run past two hours, \n"
               "and Act V is the chapter centrepiece \n"
               "at roughly four and a half hours, \n"
               "one of the three longest acts in the game. \n"
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
        pacing="The most consistently long chapter. \n"
               "Five of its six acts sit above two hours, \n"
               "and Act V is the longest act outside Nod-Krai, \n"
               "at close to five hours. \n"
               "Fontaine's acts are cutscene-dense rather than traversal-dense, \n"
               "which is why the sampled uploads agree unusually closely.",
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
               "the numbered acts cluster between two and three and a half hours. \n"
               "The Interlude is the exception, \n"
               "a one-part cooldown quest of well under an hour. \n"
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
        pacing="By far the largest chapter: eleven entries, \n"
               "and a running time comparable to Sumeru and Fontaine combined. \n"
               "Act I alone is the single longest act in the game \n"
               "at roughly five hours. \n"
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
        pacing="Only two acts exist so far, \n"
               "but both are long: roughly four hours each. \n"
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
    "ch2|Act II": "Two quest parts only: \n"
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
                 "and Nahida taking back the Akasha. \n"
                 "One of the three longest acts in the game.",
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
                 "and Neuvillette taking the seat of judgment. \n"
                 "The longest act outside Nod-Krai.",
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
    "ch5|Interlude": "One quest part: the tribes rebuild after the invasion. \n"
                     "A deliberate cooldown between Act IV and Act V.",
    "ch5|Act V": "The Night Kingdom, the truth about Mavuika's bargain, \n"
                 "and the price already paid for the Ode of Resurrection.",
    "ch5|Act VI": "Traveler chapter: the Loom of Fate \n"
                  "and the closest thing yet to a reunion with the sibling.",
    "sotwm|Prelude": "Still in Natlan: rogue Secret Source Automatons, \n"
                     "and a strange woman washed ashore looking for someone. \n"
                     "Ineffa's introduction.",
    "sotwm|Act I": "Departure from Natlan and arrival in Nod-Krai, \n"
                   "with Sandrone already tracking the Traveler. \n"
                   "The single longest act in the game.",
    "sotwm|Act II": "Nasha Town under Wild Hunt incursion, \n"
                    "the Kuuvahki Cannon repair, \n"
                    "and Rerir regaining physical form.",
    "sotwm|Act III": "Hunting Rerir across the kuuvahki-rich islands \n"
                     "with Flins, Aino, Lauma, and Jahoda.",
    "sotwm|Act IV": "Columbina in tow, Albedo and Durin return, \n"
                    "Arlecchino and Sandrone circle each other, \n"
                    "and fate starts closing in.",
    "sotwm|Act V": "Two quest parts around Moon-Prayer Night, \n"
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
AR = {
    "prologue|Act I": "-", "prologue|Act II": "10", "prologue|Act III": "18",
    "ch1|Act I": "23", "ch1|Act II": "25", "ch1|Act III": "28",
    "ch1|Act IV - Prelude": "28", "ch1|Act IV": "28",
    "ch7|Act I": "18", "ch7|Act II": "-",
}
AR_DEFAULT = {"ch2": "30", "ch3": "35", "ch4": "40", "ch5": "40", "sotwm": "40"}

# Acts the wiki has not categorized with a release version yet.
# These fall back to the version named in the sampled upload titles.
VERSION_FALLBACK = {
    "A Traveler on a Winter's Night": "Luna IV (6.3)",
    "True Moon": "Luna IV (6.3)",
    "As All Falls to Emptiness": "Luna VII (6.6)",
    "Truth Amongst the Pages of Purana": "Luna VII (6.6)",
    "Wraith's Nocturne": "7.0",
}
