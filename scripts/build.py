#!/usr/bin/env python3
"""Build script for Awesome BIM Datasets.

Usage:  python3 scripts/build.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "datasets.json"
README_FILE = ROOT / "README.md"
INDEX_FILE = ROOT / "index.html"

DATA_START = "/*__DATASETS_START__*/"
DATA_END = "/*__DATASETS_END__*/"

SITE_URL = "https://nbharathik.github.io/awesome-bim-datasets/"
REPO_URL = "https://github.com/nbharathik/awesome-bim-datasets"


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def anchor(name: str) -> str:
    """GitHub heading anchor.

    Mirrors GitHub's slugger: lowercase, strip punctuation, then replace each
    whitespace character with a hyphen *without* collapsing runs. This matters
    for headings containing " & " (e.g. "Point Clouds & Scan-to-BIM"), where
    removing the "&" leaves two spaces and GitHub emits a double hyphen.
    """
    a = name.strip().lower()
    a = re.sub(r"[^\w\s-]", "", a)
    return re.sub(r"\s", "-", a)


def dataset_links(d: dict) -> str:
    parts = []
    links = d.get("links", {})
    if links.get("download"):
        parts.append(f"[Download]({links['download']})")
    if links.get("website") and links.get("website") != links.get("download"):
        parts.append(f"[Website]({links['website']})")
    if links.get("paper"):
        parts.append(f"[Paper]({links['paper']})")
    return " · ".join(parts) if parts else "—"


def build_readme(data: dict) -> str:
    cats = data["categories"]
    datasets = data["datasets"]
    by_cat = {c["id"]: [] for c in cats}
    for d in datasets:
        by_cat.setdefault(d["category"], []).append(d)

    lines = []
    lines.append("# Awesome BIM Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated list of open datasets for **Building Information Modeling (BIM)** and the built"
                 " environment: IFC models, point clouds and scan-to-BIM data, floorplans, 3D city models,"
                 " energy and performance data, construction-site data, synthetic scenes, and ML benchmarks.")
    lines.append("")
    lines.append(f"Browse with search and filters on the website: [{SITE_URL.rstrip('/')}]({SITE_URL})")
    lines.append("")

    # Table of contents
    lines.append("## Contents")
    lines.append("")
    for c in cats:
        if not by_cat.get(c["id"]):
            continue
        lines.append(f"- [{c['name']}](#{anchor(c['name'])})")
    if data.get("related"):
        lines.append("- [Related lists](#related-lists)")
    lines.append("- [License notes](#license-notes)")
    lines.append("- [Contributing](#contributing)")
    lines.append("")

    for c in cats:
        items = by_cat.get(c["id"], [])
        if not items:
            continue
        items = sorted(items, key=lambda d: d["name"].lower())
        lines.append(f"## {c['name']}")
        lines.append("")
        lines.append(f"_{c['description']}_")
        lines.append("")
        lines.append("| Dataset | License | Links |")
        lines.append("| --- | --- | --- |")
        for d in items:
            website = d.get("links", {}).get("website") or d.get("links", {}).get("download") or ""
            name = f"[{md_escape(d['name'])}]({website})" if website else md_escape(d["name"])
            lic = md_escape(d.get("license", "Unspecified"))
            lines.append(f"| **{name}** | {lic} | {dataset_links(d)} |")
        lines.append("")

    if data.get("related"):
        lines.append("## Related lists")
        lines.append("")
        for r in data["related"]:
            lines.append(f"- [{r['name']}]({r['url']}): {r['note']}")
        lines.append("")

    lines.append("## License notes")
    lines.append("")
    lines.append("- Licenses shown are those stated by the dataset providers at the time of listing."
                 " **Always verify the current terms at the source before use**, especially for commercial projects.")
    lines.append("- *Custom (research)* means access requires agreeing to a dataset-specific research terms-of-use,"
                 " usually via a request form.")
    lines.append("- This list itself is released under [CC0 1.0](LICENSE).")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("Contributions are welcome. Found a dataset that's missing, or a dead link?"
                 " Please open an issue or a pull request, see [CONTRIBUTING.md](CONTRIBUTING.md)."
                 " All data lives in [`data/datasets.json`](data/datasets.json); run"
                 " `python3 scripts/build.py` to regenerate the README and website from it.")
    lines.append("")
    return "\n".join(lines)


def inject_site_data(data: dict) -> None:
    html = INDEX_FILE.read_text(encoding="utf-8")
    start = html.index(DATA_START) + len(DATA_START)
    end = html.index(DATA_END)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    html = html[:start] + payload + html[end:]
    INDEX_FILE.write_text(html, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    # Basic validation
    cat_ids = {c["id"] for c in data["categories"]}
    names = set()
    for d in data["datasets"]:
        assert d["category"] in cat_ids, f"Unknown category {d['category']!r} for {d['name']!r}"
        assert d["name"] not in names, f"Duplicate dataset name {d['name']!r}"
        names.add(d["name"])
        assert d.get("links", {}).get("download") or d.get("links", {}).get("website"), \
            f"{d['name']!r} needs at least a download or website link"
    README_FILE.write_text(build_readme(data), encoding="utf-8")
    inject_site_data(data)
    print(f"Built README.md and index.html with {len(data['datasets'])} datasets.")


if __name__ == "__main__":
    main()
