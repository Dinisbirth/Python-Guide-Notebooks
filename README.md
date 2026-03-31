# Python Guide Notebooks

A clean, GitHub-ready notebook repository for Python, data analysis, preprocessing, and introductory machine learning.

This repository is intentionally minimal. It keeps only the material needed to study and run the notebooks:
- `weeks/` for the main learning path
- `data/` for the datasets used in the notebooks
- `src/` for reusable helper code

Archive-style source folders were removed from the main repository so the GitHub view stays clean and focused.

## Repository Layout

```text
ct7201-guide/
|-- README.md
|-- requirements.txt
|-- data/
|   |-- housing.csv
|   `-- framingham.csv
|-- src/
`-- weeks/
    |-- README.md
    `-- week-xx-topic/
        |-- README.md
        |-- answers/
        |   `-- README.md
        `-- notebooks/
            `-- notebook.ipynb
```

## How To Use This Repository

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Start Jupyter from the repository root:

```bash
jupyter lab
```

3. Open the folders in `weeks/` in order.

Each week folder contains:
- `README.md` with the week overview
- `notebooks/` with the runnable notebook
- `answers/` with the notes, tasks, and worked guidance

## Weekly Guide

| Week | Topic | Folder |
| --- | --- | --- |
| 01 | Jupyter and Python Fundamentals | [weeks/week-01-jupyter-basics](weeks/week-01-jupyter-basics) |
| 02 | Functions, Control Flow, and Loops | [weeks/week-02-functions-and-loops](weeks/week-02-functions-and-loops) |
| 03 | Collections and Strings | [weeks/week-03-collections-and-strings](weeks/week-03-collections-and-strings) |
| 04 | Dictionaries and Nested Data | [weeks/week-04-dictionaries-and-data](weeks/week-04-dictionaries-and-data) |
| 05 | Input, While Loops, and OOP | [weeks/week-05-input-loops-and-oop](weeks/week-05-input-loops-and-oop) |
| 06 | Standard Library and Environments | [weeks/week-06-standard-library](weeks/week-06-standard-library) |
| 07 | Scripts, Modules, and Third-Party Libraries | [weeks/week-07-scripts-and-libraries](weeks/week-07-scripts-and-libraries) |
| 08 | Data Analysis Basics | [weeks/week-08-data-analysis-basics](weeks/week-08-data-analysis-basics) |
| 09 | Correlation, Feature Engineering, and Imputation | [weeks/week-09-feature-engineering-and-imputation](weeks/week-09-feature-engineering-and-imputation) |
| 10 | Data Preprocessing Pipelines | [weeks/week-10-preprocessing-pipelines](weeks/week-10-preprocessing-pipelines) |
| 11 | Introduction to Machine Learning | [weeks/week-11-intro-to-machine-learning](weeks/week-11-intro-to-machine-learning) |
| 12 | Applied Machine Learning Capstone | [weeks/week-12-capstone-projects](weeks/week-12-capstone-projects) |

## Data

The datasets used in the later weeks live in [data](data):
- `housing.csv` for exploratory analysis and preprocessing
- `framingham.csv` for classification practice

## Code

Reusable helper code lives in [src](src), including [src/stats.py](src/stats.py).

## Note On Weeks 8-12

The later supplied teaching materials were topic-based rather than clearly labelled by exact week. Weeks 8-12 in this repository were organised into a clean progression so the course reads properly from start to finish.

## Verification

The notebooks were executed locally and checked for notebook cell errors after generation.
