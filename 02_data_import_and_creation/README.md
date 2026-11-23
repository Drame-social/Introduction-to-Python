# Phase 02 — Data Import & Creation

## Topics Covered

Importing CSV files with pd.read_csv(), a legacy Excel file with pd.read_excel(), and a space-delimited text file with no header row; creating a small dataset in code; stacking datasets with pd.concat() and flagging their source.

## Files

| File | Description |
|------|-------------|
| `02_data_import_and_creation.py` | Import, create, and stack datasets |

## Datasets Used

phase1.csv, phase2.csv, cohort1516.csv, cohort1617.csv, raw/RAWDAT1.xls, raw/RAWDATA.TXT

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
rawdata_txt = pd.read_csv("./data/raw/RAWDATA.TXT", sep=r"\s+", header=None,
                          names=["studyid", "caco", "age", "exposure"])

cohort_combined = pd.concat([cohort1516, cohort1617], ignore_index=True)
phases = pd.concat([phase1.assign(phase=1), phase2.assign(phase=2)], ignore_index=True)
```
