#!/usr/bin/env python3
"""Fetch the release version of every act, and each version's number and date.

Usage: fetch_versions.py <workdir>

Reads  <workdir>/acts.tsv
       <workdir>/wiki.json           which wiki, and how it records versions:
                                     host, name, released_in, version_page,
                                     version_fields (see DEFAULTS below)
Writes <workdir>/versions.json       {act title: version name or null}
       <workdir>/version_index.json  {version name: {number, date}}

Run this before harvesting, not after: the version an act shipped in is what
recent uploads put in their titles ("Genshin Impact 6.6 Act 10 ..."), so the
harvest needs it to search for them, and the release date is what tells the
harvest how recent an act is.

Fandom serves a Cloudflare challenge to plain HTTP clients on /wiki/<Page>, so
everything here goes through the MediaWiki API, which is not challenged. The
release version is not in the wikitext: it is a category the templates add.

The defaults are what the HoYoverse-style wikis share, but the version infobox
does differ between them (Genshin has |number and |date, Honkai: Star Rail has
|version and |release_date), which is what version_fields is for. A game whose
wiki does not categorize by version at all sets released_in to null: the harvest
then searches by act title alone, and no act counts as recent.

Some wikis record which acts a version shipped instead on the version page, in
prose no script can read ("New Main Story up to Chapter II Process VI"). There,
set released_in to null and write versions.json by hand from those pages: a
mapping already on disk is kept rather than overwritten with nulls, and the
versions it names are still indexed from their infoboxes here.
"""
import json
import pathlib
import re
import sys
from datetime import datetime
import urllib.parse
import urllib.request

AGENT = "Mozilla/5.0 (X11; Linux x86_64)"
BATCH = 50                  # titles per API request, the MediaWiki limit
DEFAULTS = dict(
    released_in=r"Released in Version (.+)",   # the category, minus "Category:"
    version_page="Version/{version}",          # the page its infobox sits on
    version_fields=dict(number="number", date="date"),
)


def api(host, **params):
    params.setdefault("format", "json")
    url = f"https://{host}/api.php?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def act_pages(workdir):
    """Act title -> the wiki page documenting it, which carries the category.

    The two differ wherever acts.tsv names a page in its fifth column, which is
    what a game whose act titles are not page titles needs.
    """
    seen = {}
    for line in (workdir / "acts.tsv").read_text().splitlines():
        if line.strip():
            title, *page = line.split("\t")[3:]
            seen[title] = page[0] if page else title
    return seen


def categories(host, titles):
    """Page title -> its categories, following the continuation the API returns.

    A batch of 50 pages runs past the 500-entry response limit, and the pages
    that get cut off come back looking uncategorized, which is how five acts
    ended up with no release version at all.
    """
    out = {}
    params = dict(action="query", prop="categories", cllimit="max",
                  titles="|".join(titles))
    while True:
        response = api(host, **params)
        for page in response["query"]["pages"].values():
            out.setdefault(page["title"], []).extend(
                c["title"] for c in page.get("categories", []))
        if "continue" not in response:
            return out
        params.update(response["continue"])


def released_in(wiki, pages, recorded):
    """Act title -> version name, from the "Released in Version X" category.

    A wiki that does not categorize by version leaves the mapping to whatever
    versions.json already records, so that a mapping read off the version pages
    by hand survives a re-run instead of being flattened to nulls.
    """
    if not wiki["released_in"]:
        return {t: recorded.get(t) for t in pages}
    pattern = re.compile(f"^Category:{wiki['released_in']}$")
    titles = list(dict.fromkeys(pages.values()))
    out = {}
    for start in range(0, len(titles), BATCH):
        for title, cats in categories(wiki["host"],
                                      titles[start:start + BATCH]).items():
            versions = [m.group(1) for m in map(pattern.match, cats) if m]
            out[title] = versions[0] if versions else None
    # Redirects and normalisation can rename a page, so report on what was asked
    # for rather than on what came back.
    return {act: out.get(page) for act, page in pages.items()}


def iso_date(value):
    """`July 29, 2026` and `05:00, JUN 26, 2025` both as ISO, or unchanged.

    One wiki writes both forms, sometimes on neighbouring version pages, and the
    dates are sorted against each other to decide which acts count as recent, so
    a spelled-out month left as it stands would sort after every real date.
    """
    if not value:
        return None
    # A footnote or a citation template often follows the date, and one wiki
    # leads with the clock time rather than trailing it ("05:00, JUN 26, 2025").
    plain = re.sub(r"(<ref|\{\{).*$", "", value, flags=re.S)
    plain = re.sub(r"^\s*\d{1,2}:\d{2}\s*,?\s*", "", plain)
    plain = re.sub(r"\s*\d{1,2}:\d{2}.*$", "", plain).strip()
    plain = re.sub(r"(?<=\d)(st|nd|rd|th)\b", "", plain)   # September 4th, 2025
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%B %d, %Y", "%d %B %Y", "%b %d, %Y",
                "%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(plain, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value


def version_details(wiki, names):
    """Version name -> {number, date}, from the version page's infobox."""
    number_field, date_field = (wiki["version_fields"][k]
                                for k in ("number", "date"))
    field = re.compile(rf"^\|\s*({number_field}|{date_field})\s*=\s*(.+?)\s*$",
                       re.M)
    out = {}
    for name in names:
        page = wiki["version_page"].format(version=name)
        wikitext = api(wiki["host"], action="parse", page=page,
                       prop="wikitext")["parse"]["wikitext"]["*"]
        fields = dict(field.findall(wikitext))
        out[name] = {"number": fields.get(number_field, name),
                     "date": iso_date(fields.get(date_field))}
    return out


def load_wiki(workdir):
    """The wiki's conventions, over the defaults the HoYoverse-style wikis share."""
    return {**DEFAULTS, **json.loads((workdir / "wiki.json").read_text())}


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    workdir = pathlib.Path(argv[1])
    wiki = load_wiki(workdir)

    recorded = json.loads((workdir / "versions.json").read_text()) \
        if (workdir / "versions.json").exists() else {}
    versions = released_in(wiki, act_pages(workdir), recorded)
    index = version_details(wiki, sorted(set(filter(None, versions.values()))))

    (workdir / "versions.json").write_text(
        json.dumps(dict(sorted(versions.items())), indent=1,
                   ensure_ascii=False) + "\n")
    (workdir / "version_index.json").write_text(
        json.dumps(index, indent=1) + "\n")

    missing = [t for t, v in versions.items() if not v]
    print(f"{len(versions) - len(missing)} acts categorized, "
          f"{len(index)} versions indexed")
    for title in missing:
        print(f"  no release version on the wiki yet: {title}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
