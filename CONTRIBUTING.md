# Contributing

Thanks for helping grow Awesome BIM Datasets.

## How it works

All dataset information lives in a single file: [`data/datasets.json`](data/datasets.json).
Both the `README.md` and the website (`index.html`) are **generated** from it. Never edit those by hand.

## Adding or fixing a dataset

1. Edit `data/datasets.json`. Add your dataset to the `datasets` array:

```json
{
  "name": "My Dataset",
  "category": "ifc",
  "description": "One or two sentences: what it contains and what it's useful for.",
  "size": "120 IFC models, ~4 GB",
  "license": "CC BY 4.0",
  "year": 2024,
  "source": "Example University",
  "tags": ["ifc", "residential"],
  "links": {
    "download": "https://example.org/download",
    "website": "https://example.org",
    "paper": "https://doi.org/10.xxxx/xxxxx"
  }
}
```

   - `category` must be one of the ids in the `categories` array (`ifc`, `pointcloud`, `floorplan`, `city`, `energy`, `construction`, `synthetic`, `benchmark`).
   - `license` should be the exact license name the provider states. If access requires a form/agreement, use e.g. `Custom (research use, request form)`. Use `Unspecified` only when the provider genuinely states nothing.
   - At least one of `links.download` or `links.website` is required. Prefer stable, official links.
   - `description`, `size`, `year`, `paper`, and `tags` are optional. Descriptions are not shown in the README table, but they power the website's search, so a short one is still useful.

2. Regenerate the README and website:

```bash
python3 scripts/build.py
```

3. Open a pull request with all three changed files (`data/datasets.json`, `README.md`, `index.html`).

## Guidelines

- **Datasets only**: data you can download or request access to. Tools, viewers, and libraries belong elsewhere.
- Datasets should be relevant to BIM / the built environment: BIM models (IFC, RVT, …), building/indoor point clouds, floorplans, 3D city models, building energy data, construction-site data, or ML benchmarks built on such data.
- Verify the link works and the license statement matches what the provider says today.
- Keep descriptions factual and concise (what's in it, roughly how much).

## Reporting problems

Dead link, wrong license, dataset gone private? [Open an issue](../../issues) with the dataset name and what changed.
