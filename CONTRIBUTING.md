# Contributing

Thanks for helping. Every dataset lives in [`data/datasets.json`](data/datasets.json), one per line. The README is generated from it and the [website](https://nbharathik.github.io/awesome-bim-datasets/) reads it directly.

No time for a pull request? [Suggest a dataset](https://github.com/nbharathik/awesome-bim-datasets/issues/new?template=add-dataset.yml) or [report a broken link](https://github.com/nbharathik/awesome-bim-datasets/issues/new).

## Add a dataset

1. Add a line to `datasets` in `data/datasets.json`:

   ```json
   {"name": "My Dataset", "category": "ifc", "description": "120 IFC models of school buildings with room labels", "license": "CC BY 4.0", "year": 2025, "url": "https://example.org/my-dataset", "paper": "https://arxiv.org/abs/0000.00000"}
   ```

   | Field | |
   | --- | --- |
   | `name` | Name used by the provider |
   | `category` | `ifc`, `pointcloud`, `urban`, `floorplan`, `city`, `energy`, `construction`, `synthetic` or `benchmark` |
   | `description` | One short phrase, no trailing period |
   | `license` | As stated by the provider, e.g. `CC BY 4.0`, `Custom (research only)`, `Not specified` |
   | `url` | Main page of the dataset |
   | `year`, `data`, `paper`, `code` | Optional: release year, direct data link, paper, code |

2. Run `python scripts/build.py`. It validates the data, sorts it and regenerates `README.md`.
3. Open a pull request with both files.

## What belongs here

Data you can download or request that is about buildings, BIM or the built environment. Tools, libraries and papers without data do not.

## Checks

```bash
python scripts/build.py --check
```

```bash
python scripts/build.py --links
```

The first fails if the data or README are out of date. The second reports links that do not respond. GitHub Actions runs the first on every push and the second every Monday.

To preview the website, run `python -m http.server` in the repository and open http://localhost:8000.
