# CT7201 Python Guide Notebooks

This repository is a cleaned, structured, GitHub-ready study guide built from the supplied course slides, PDFs, datasets, starter code, and existing student notebooks for Python Notebooks and Scripting.

It is organised as a complete course repository rather than a loose collection of files:
- `weeks/` contains the final week-by-week learning folders
- `data/` contains the datasets used in the later analysis and ML material
- `references/` preserves the original source materials and extracted text snapshots
- `src/` contains reusable Python helpers
- `notes/` contains roadmap and dataset notes

## What This Repository Includes

- 12 structured weekly folders
- A `summary.md`, `tasks.md`, and `notebook.ipynb` for each week
- Executed notebooks that were checked locally
- A cleaned `Stats` helper module for descriptive statistics
- Housing and Framingham datasets copied into a consistent project layout
- Original course materials preserved for traceability

## Repository Layout

```text
ct7201-guide/
|-- README.md
|-- ATTRIBUTION.md
|-- requirements.txt
|-- data/
|-- notes/
|-- references/
|-- src/
`-- weeks/
```

## Weekly Roadmap

| Week | Topic | Focus |
| --- | --- | --- |
| 01 | Jupyter and Python Fundamentals | Notebooks, Markdown, variables, and basic Python types |
| 02 | Functions, Control Flow, and Loops | Functions, operators, conditionals, and loop-based problem solving |
| 03 | Collections and Strings | Lists, slicing, string operations, and practice tasks |
| 04 | Dictionaries and Nested Data | Dictionaries, sets, tuples, and structured records |
| 05 | Input, While Loops, and OOP | Input validation, loops, classes, and objects |
| 06 | Standard Library and Environments | Built-ins, modules, conda, and pip |
| 07 | Scripts, Modules, and Third-Party Libraries | `.py` files, imports, pandas, and reusable helpers |
| 08 | Data Analysis Basics | Dataset inspection, profiling, plotting, and train/test splitting |
| 09 | Correlation, Feature Engineering, and Imputation | Signal analysis, engineered features, and missing-value handling |
| 10 | Data Preprocessing Pipelines | Encoding, scaling, custom transformers, and pipelines |
| 11 | Introduction to Machine Learning | Classification, regression, and clustering basics |
| 12 | Applied Machine Learning Capstone | End-to-end regression and classification mini-projects |

## Quick Start

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open Jupyter from the repository root:

```bash
jupyter lab
```

4. Work through the folders in `weeks/` in order.

## Key Folders

### `weeks/`
Each week folder contains:
- `summary.md`
- `tasks.md`
- `notebook.ipynb`

### `data/`
Datasets used in the later analytical and machine-learning sections:
- California housing
- Framingham cardiovascular dataset

### `references/`
Preserved copies of:
- original PowerPoint files
- original PDF materials
- source notebook references
- extracted text snapshots used to structure the final guide

## Important Note On Weeks 8-12

The later supplied files were mostly topic-based (`Data Analysis`, `Data Handling`, `Intro to ML`) rather than clearly named by exact week. Weeks 8-12 in this repository were therefore organised by topic progression inferred from the source materials so the course remains coherent from start to finish.

## Verification

The generated notebooks were executed locally after creation to check for broken imports, path issues, and notebook cell errors.

## Attribution

This repository reorganises and supplements the supplied teaching materials for study use. See `ATTRIBUTION.md` and the `references/` folder for source tracking.
