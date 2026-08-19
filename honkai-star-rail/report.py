"""This report's configuration and structure.

The generic renderer in the skill's `gen_docs.py` reads what this game's level
gate is called, the noun it numbers its acts with, and the chapters in the
order they are published in. The prose lives in the markdown files next to
this one, which the renderer fills in place rather than writes.

The wiki pages recorded here feed the renderer nothing. They record what the
authored markdown links by hand, because a mission's own wiki page reaches the
renderer through `analysis.json` instead.

Terminology: the wiki calls one Trailblaze Mission a chapter and numbers them
game-wide, first to twenty-sixth. This report groups them by the world they take
place on, so a chapter here is a world and a mission is what the wiki numbers.
"""

REPORT = dict(
    # The wiki page that documents the questline as a whole, linked by hand from
    # README.md's method section and from every chapter's sources bullets.
    overview_page="Trailblaze Mission",
    # The account-level requirement acts are gated behind, as the game names it.
    # Two names for it here, Trailblaze Level and Equilibrium Level, so the
    # values carry the name and the label stays the neutral half.
    gate_label="Level",
    # What this game numbers its acts with, for the renderer's own headings.
    unit="Mission",
    date="2026-08-18",
)

CHAPTERS = [
    dict(
        id="herta", slug="00-herta-space-station", wiki_page="Herta Space Station",
        region="Herta Space Station",
        versions="1.0",
        title="Herta Space Station",
    ),
    dict(
        id="jarilo", slug="01-jarilo-vi", wiki_page="Jarilo-VI",
        region="Jarilo-VI: Belobog and the Underworld",
        versions="1.0",
        title="Jarilo-VI",
    ),
    dict(
        id="luofu", slug="02-xianzhou-luofu", wiki_page="The Xianzhou Luofu",
        region="The Xianzhou Luofu",
        versions="1.0 - 1.3",
        title="The Xianzhou Luofu",
    ),
    dict(
        id="penacony", slug="03-penacony", wiki_page="Penacony",
        region="Penacony, the Land of Dreams",
        versions="2.0 - 2.7",
        title="Penacony",
    ),
    dict(
        id="amphoreus", slug="04-amphoreus", wiki_page="Amphoreus",
        region="Amphoreus, the Eternal Land",
        versions="3.0 - 3.7",
        title="Amphoreus",
    ),
    dict(
        id="planarcadia", slug="05-planarcadia", wiki_page="Planarcadia",
        region="Planarcadia",
        versions="4.0 - 4.4",
        title="Planarcadia",
    ),
]

# The wiki records a level requirement for two missions only, both on Jarilo-VI,
# and both partway through rather than at the mission's start.
GATES = {
    "jarilo|Mission 1": "Trailblaze Level 13, partway through",
    "jarilo|Mission 2": "Equilibrium Level 1",
}
GATE_DEFAULT = {}
