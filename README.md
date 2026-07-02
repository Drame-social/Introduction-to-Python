# Python Programming for Public Health Analytics

*By Aly Drame, MD, MPH, MBA.* The Python (pandas / numpy / matplotlib / seaborn) counterpart to my SAS and R public-health programming repos — the same Emory AEPI537D course datasets (synthetic / course-provided; no real patient or program records), worked from import through reporting.

---

## Overview

This repository applies core Python programming skills to educational public health datasets (synthetic / course-provided; no real patient or program records), organized by the natural data analysis workflow. It is the Python counterpart to [sas-public-health-analytics](https://github.com/Drame-social/sas-public-health-analytics) and [R-Practice](https://github.com/Drame-social/R-Practice), performing equivalent analyses using idiomatic Python (pandas / numpy / seaborn / matplotlib).

---

## Workflow

```
01 Environment Setup
     ↓
02 Data Import & Creation
     ↓
03 Data Merging & Subsetting
     ↓
04 Categorical Variables & Dates
     ↓
05 Conditionals & Type Conversion
     ↓
06 Python Functions
     ↓
07 Loops & List Comprehensions
     ↓
08 Longitudinal & Repeated Measures
     ↓
09 Variable Documentation
     ↓
10 Reporting & Export
     ↓
11 Automation & Pipelines
     ↓
12 Visualization & Mapping
```

---

## Datasets

| File | Rows | Cols | Description |
|------|------|------|-------------|
| aidsvu_2016_newdx_county.csv | 160 | 7 | HIV new diagnoses by county, 2016 |
| atlgrades.csv | 26 | 4 | Student grade records |
| cohort1516.csv | 204 | 6 | Cohort enrollment, 2015–16 |
| cohort1617.csv | 152 | 6 | Cohort enrollment, 2016–17 |
| final_clin.csv | 1,006 | 36 | Clinical HIV outcomes |
| final_demo.csv | 1,006 | 6 | Patient demographics |
| flbygroup.csv | 100 | 3 | Flu data by group |
| labs.csv | 30 | 2 | Laboratory results |
| mod3lab.csv | 356 | 20 | Module 3 lab dataset |
| mod4.csv | 356 | 24 | Module 4 categorical/date data |
| mod6.csv | 356 | 35 | Module 6 variable documentation |
| mod8_a/b/c/d.csv | varies | varies | Arrays and repeated measures |
| mod9.csv | 356 | 20 | Longitudinal visit data |
| mock_data.csv | 50 | 16 | General mock patient data |
| patients.csv | 2,148 | 22 | Patient-level records |
| patients_part2.csv | 1,236 | 22 | Additional patient records |
| phase1.csv / phase2.csv | 20/10 | 4 | Study phase enrollment |
| screener_data.csv | 280 | 5 | Screening questionnaire |
| survey.csv | 356 | 6 | Survey responses |
| tagsetex.csv | 10 | 4 | Tag set example |

---

## Key Libraries

| Library | Purpose |
|---------|---------|
| pandas | Data import, manipulation, merging, export |
| numpy | Numeric operations, conditional logic |
| matplotlib | Base plotting engine |
| seaborn | Statistical visualization (box plots, etc.) |
| openpyxl | Excel export (multi-sheet workbooks) |

---

## How to Run

1. Clone this repo
2. Create a virtual environment and install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl
   ```
3. Run scripts in phase order from the repo root:
   ```bash
   python 02_data_import_and_creation/02_data_import_and_creation.py
   ```
   Each script reads from `./data` and writes outputs to `./data` or a local `./outputs` folder.

---

## Related Repositories

- [sas-public-health-analytics](https://github.com/Drame-social/sas-public-health-analytics) — SAS version (same analyses)
- [R-Practice](https://github.com/Drame-social/R-Practice) — R version (same analyses)
