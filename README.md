# CT7201 Python Guide Notebooks

This repository is a cleaned, GitHub-ready study guide built from the supplied lecture slides, PDFs, datasets, starter code, and student notebooks for Python Notebooks and Scripting.

## Repository Structure

- `weeks/`: the main learning path, one folder per week
- `docs/`: roadmap and dataset notes
- `data/`: canonical dataset copies used by the notebooks
- `src/`: reusable Python helpers
- `references/course_materials/`: archived lecture materials and extracted text
- `references/student_work/`: archived student notebooks and extracted text

## What Is Included

- 12 structured weekly folders
- a `summary.md`, `tasks.md`, and `notebook.ipynb` in every week
- executed notebooks checked locally for runtime errors
- a cleaned `Stats` helper in `src/stats.py`
- de-duplicated source archives instead of repeated copies across multiple week folders

## Repository Layout

```text
ct7201-guide/
|-- README.md
|-- ATTRIBUTION.md
|-- .gitattributes
|-- requirements.txt
|-- data/
|-- docs/
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
2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Start Jupyter from the repository root:

```bash
jupyter lab
```

4. Work through the folders in `weeks/` in order.

## Folder Notes

### `weeks/`
Each week contains:
- `summary.md`
- `tasks.md`
- `notebook.ipynb`

### `docs/`
Contains:
- `course_roadmap.md`
- `housing_dataset.md`
- `framingham_dataset.md`

### `data/`
This is the canonical location for datasets used by the notebooks. The reference archive no longer repeats those dataset files week after week.

### `references/`
The reference archive is split into:
- `course_materials/` for lecture and tutorial source files
- `student_work/` for the original notebook work that informed the cleaned version

## Important Note On Weeks 8-12

The later supplied files were mostly topic-based (`Data Analysis`, `Data Handling`, `Intro to ML`) rather than clearly labelled by exact week number. Weeks 8-12 in this repository were therefore organised by topic progression inferred from those materials so the course remains coherent from start to finish.

## Verification

The generated notebooks were executed locally after creation and checked for notebook cell errors.

## Attribution

This repository reorganises and supplements the supplied teaching materials for study use. See `ATTRIBUTION.md` and the `references/` folder for source tracking.
