#!/usr/bin/env python3
"""Emit the YouTube searches to run for every act, and how deep to run them.

Usage: queries.py <workdir>

Reads  <workdir>/acts.tsv
       <workdir>/versions.json        act title -> version name
       <workdir>/version_index.json   version name -> {number, date}
       <workdir>/query_templates.txt  one template per line (optional)
       <workdir>/game.txt             the game's name, for branded queries
Writes one "<slug> <TAB> <depth> <TAB> <query>" line per search, to stdout.

Two things the plain "chapter, act label, act title" search cannot reach:

- Recent uploads are titled by patch branding rather than by act title
  ("Genshin Impact 6.6 Act 10 Full Walkthrough"), which carries neither act-title
  words nor a chapter keyword. The version-branded templates search for those.
- A search that is deep enough for an act with hundreds of uploads is far too
  shallow for one released a month ago, so recent acts get a deeper search.
"""
import json
import pathlib
import sys

from analyze import ROMAN, act_number, load_acts

DEPTH = 6                    # results per query for settled content
RECENT_DEPTH = 12            # ... and for acts released in the last few versions
RECENT_VERSIONS = 4          # how many versions back still counts as recent

DEFAULT_TEMPLATES = [
    "{chapter} {act_label} {act_title} full walkthrough no commentary",
    "{act_title} full quest gameplay",
]


def read_lines(path):
    return [l.strip() for l in path.read_text().splitlines() if l.strip()] \
        if path.exists() else []


def recent_versions(version_index, count=RECENT_VERSIONS):
    """The names of the `count` most recently released versions."""
    dated = [(v["date"], name) for name, v in version_index.items() if v["date"]]
    return {name for _, name in sorted(dated)[-count:]}


def act_queries(templates, fields):
    """A template that names a field the act has no value for is skipped.

    That is how the version-branded templates stay out of the way for an act the
    wiki has not categorized yet, instead of searching for "None Act 3".
    """
    for template in templates:
        try:
            yield template.format(**fields).strip()
        except KeyError:
            continue


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    workdir = pathlib.Path(argv[1])
    versions = json.loads((workdir / "versions.json").read_text())
    version_index = json.loads((workdir / "version_index.json").read_text())
    templates = read_lines(workdir / "query_templates.txt") or DEFAULT_TEMPLATES
    game = " ".join(read_lines(workdir / "game.txt"))
    recent = recent_versions(version_index)

    for act in load_acts(workdir):
        version = versions.get(act["act_title"])
        details = version_index.get(version or "", {})
        number = act_number(act["act_label"])
        fields = {
            "game": game,
            "chapter": act["chapter_title"].split(":")[0],
            "act_label": act["act_label"],
            "act_title": act["act_title"],
        }
        if number:
            fields["act_number"] = number
            fields["act_roman"] = next(k for k, v in ROMAN.items() if v == number)
        if version:
            fields["version"] = version
            fields["number"] = details.get("number", version)
        depth = RECENT_DEPTH if version in recent else DEPTH
        for query in act_queries(templates, fields):
            print(f"{act['slug']}\t{depth}\t{query}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
