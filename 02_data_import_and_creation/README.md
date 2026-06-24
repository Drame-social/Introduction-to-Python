# Phase 02 — Data Import & Creation

## Topics Covered

Importing CSV files with pd.read_csv(), reading Excel files with pd.read_excel(), reading delimited text files, stacking datasets with pd.concat(), and merging with DataFrame.merge().

## Files

| File | Description |
|------|-------------|
| `02_data_import_and_creation.py` | Import, merge, and stack datasets |

## Datasets Used

phase1.csv, phase2.csv, cohort1516.csv, cohort1617.csv, labs.csv, RAWDAT1.xls, RAWDATA.TXT

## Key Python Syntax

```python
import pandas as pd

# Import CSV
df = pd.read_csv("./data/phase1.csv")

# Stack datasets
combined = pd.concat([cohort1516, cohort1617], ignore_index=True)

# Left merge
merged = final_demo.merge(final_clin, on="studyid", how="left")
```
