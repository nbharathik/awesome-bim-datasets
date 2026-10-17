#!/usr/bin/env python3
"""Validate and sort data/datasets.json, then generate README.md from it.

  python scripts/build.py           validate, sort the data and write README.md
  python scripts/build.py --check   fail if the data or README.md are out of date
  python scripts/build.py --links   also report links that do not respond
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://nbharathik.github.io/awesome-bim-datasets/"
FIELDS = ("name", "category", "description", "license", "year", "url", "data", "paper", "code")
REQUIRED = ("name", "category", "description", "license", "url")
LINKS = ("url", "data", "paper", "code")


def load():
    data = json.loads((ROOT / "data/datasets.json").read_text(encoding="utf-8"))
    categories = {c["id"] for c in data["categories"]}
    errors, names = [], set()
    for d in data["datasets"]:
        name = d.get("name", "?")
        errors += [f"{name}: missing {k}" for k in REQUIRED if not str(d.get(k, "")).strip()]
        errors += [f"{name}: unknown field {k}" for k in d if k not in FIELDS]
        errors += [f"{name}: {k} must start with http" for k in LINKS if k in d and not d[k].startswith("http")]
        if d.get("category") not in categories:
            errors.append(f"{name}: unknown category {d.get('category')}")
        if name.casefold() in names:
            errors.append(f"{name}: duplicate name")
        names.add(name.casefold())
    if "\\u2014" in json.dumps(data):
        errors.append("Use a comma or colon instead of an em dash")
    if errors:
        sys.exit("\n".join(errors))
    order = [c["id"] for c in data["categories"]]
    data["datasets"] = sorted(({k: d[k] for k in FIELDS if k in d} for d in data["datasets"]),
                              key=lambda d: (order.index(d["category"]), d["name"].casefold()))
    return data


def dump(data):
    rows = lambda items: ",\n".join("    " + json.dumps(item, ensure_ascii=False) for item in items)
    return "{\n" + ",\n".join(f'  "{k}": [\n{rows(data[k])}\n  ]' for k in ("categories", "related", "datasets")) + "\n}\n"


def anchor(title):
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", title.lower()))


def cell(text):
    return str(text).replace("|", "\\|")


def readme(data):
    datasets = data["datasets"]
    lines = [
        "# Awesome BIM Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A curated list of open datasets for Building Information Modeling (BIM) and the built environment.",
        "",
        f"**[Search all {len(datasets)} datasets on the website]({SITE})** · "
        "[Suggest a dataset](https://github.com/nbharathik/awesome-bim-datasets/issues/new?template=add-dataset.yml)",
        "",
        "## Contents",
        "",
    ]
    groups = [(c, [d for d in datasets if d["category"] == c["id"]]) for c in data["categories"]]
    lines += [f"- [{c['name']}](#{anchor(c['name'])}) ({len(items)})" for c, items in groups if items]
    lines += ["- [Related lists](#related-lists)", ""]
    for c, items in groups:
        if not items:
            continue
        lines += [f"## {c['name']}", "", "| Dataset | Description | License | Links |", "| --- | --- | --- | --- |"]
        for d in items:
            links = " · ".join(f"[{k.title()}]({d[k]})" for k in ("data", "paper", "code") if k in d)
            lines.append(f"| [{cell(d['name'])}]({d['url']}) | {cell(d['description'])} | {cell(d['license'])} | {links} |")
        lines.append("")
    lines += ["## Related lists", ""]
    lines += [f"- [{r['name']}]({r['url']}): {r['note']}." for r in data["related"]]
    lines += [
        "",
        "## Contributing",
        "",
        "All entries live in [`data/datasets.json`](data/datasets.json). This README is generated from it and the website"
        " reads it directly. See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "Licenses are shown as stated by each provider. Check the source before use. This list is released under [CC0](LICENSE).",
        "",
    ]
    return "\n".join(lines)


def status(url, tries=3):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link check; awesome-bim-datasets)"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except Exception as error:
        if tries > 1:
            time.sleep(3)
            return status(url, tries - 1)
        return str(getattr(error, "reason", error))


def check_links(data):
    urls = sorted({(d[k], d["name"]) for d in data["datasets"] for k in LINKS if k in d})
    urls += [(r["url"], r["name"]) for r in data["related"]]
    with ThreadPoolExecutor(8) as pool:
        results = list(pool.map(lambda item: status(item[0]), urls))
    broken = 0
    for (url, name), code in zip(urls, results):
        if code in (401, 403, 405, 429):
            print(f"blocked {code}  {name}  {url}")
        elif not isinstance(code, int) or code >= 400:
            print(f"BROKEN  {code}  {name}  {url}")
            broken += 1
    print(f"Checked {len(urls)} links, {broken} broken.")
    return broken


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the data or README.md are out of date")
    parser.add_argument("--links", action="store_true", help="check that every link responds")
    args = parser.parse_args()
    data = load()
    for name, text in {"data/datasets.json": dump(data), "README.md": readme(data)}.items():
        path = ROOT / name
        if not args.check:
            path.write_text(text, encoding="utf-8", newline="\n")
        elif path.read_text(encoding="utf-8") != text:
            sys.exit(f"{name} is out of date. Run: python scripts/build.py")
    print(f"{len(data['datasets'])} datasets OK.")
    if args.links and check_links(data):
        sys.exit(1)


if __name__ == "__main__":
    main()
