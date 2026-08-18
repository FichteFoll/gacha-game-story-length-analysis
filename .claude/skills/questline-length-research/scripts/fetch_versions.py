#!/usr/bin/env python3
"""Fetch the release version of every act, and each version's number and date.

Usage: fetch_versions.py <workdir> <wiki-host>
       e.g. fetch_versions.py data genshin-impact.fandom.com

Reads  <workdir>/acts.tsv
Writes <workdir>/versions.json       {act title: version name or null}
       <workdir>/version_index.json  {version name: {number, date}}

Run this before harvesting, not after: the version an act shipped in is what
recent uploads put in their titles ("Genshin Impact 6.6 Act 10 ..."), so the
harvest needs it to search for them, and the release date is what tells the
harvest how recent an act is.

Fandom serves a Cloudflare challenge to plain HTTP clients on /wiki/<Page>, so
everything here goes through the MediaWiki API, which is not challenged. The
release version is not in the wikitext: it is a category the templates add.
"""
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

AGENT = "Mozilla/5.0 (X11; Linux x86_64)"
BATCH = 50                  # titles per API request, the MediaWiki limit
RELEASED_IN = re.compile(r"^Category:Released in Version (.+)$")


def api(host, **params):
    params.setdefault("format", "json")
    url = f"https://{host}/api.php?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def act_titles(workdir):
    seen = {}
    for line in (workdir / "acts.tsv").read_text().splitlines():
        if line.strip():
            seen[line.split("\t")[3]] = None
    return list(seen)


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


def released_in(host, titles):
    """Act title -> version name, from the "Released in Version X" category."""
    out = {}
    for start in range(0, len(titles), BATCH):
        for title, cats in categories(host, titles[start:start + BATCH]).items():
            versions = [m.group(1) for m in map(RELEASED_IN.match, cats) if m]
            out[title] = versions[0] if versions else None
    # Redirects and normalisation can rename a page, so report on what was asked
    # for rather than on what came back.
    return {t: out.get(t) for t in titles}


def version_details(host, names):
    """Version name -> {number, date}, from the Version/<name> infobox."""
    out = {}
    for name in names:
        wikitext = api(host, action="parse", page=f"Version/{name}",
                       prop="wikitext")["parse"]["wikitext"]["*"]
        fields = dict(re.findall(r"^\|\s*(number|date)\s*=\s*(\S+)", wikitext,
                                 re.M))
        out[name] = {"number": fields.get("number", name),
                     "date": fields.get("date")}
    return out


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    workdir, host = pathlib.Path(argv[1]), argv[2]

    versions = released_in(host, act_titles(workdir))
    index = version_details(host, sorted(set(filter(None, versions.values()))))

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
