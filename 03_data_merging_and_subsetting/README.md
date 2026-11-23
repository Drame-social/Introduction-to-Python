# Phase 03 — Data Merging & Subsetting

## Topics Covered

Merging by ID with merge(), checking match status with indicator=True, keeping only records from one side (SAS IN=), subsetting rows and columns, anti-joins, and sorting.

## Files

| File | Description |
|------|-------------|
| `03_data_merging_and_subsetting.py` | Merge, filter, and sort datasets |

## Datasets Used

phase2.csv, labs.csv, mod3lab.csv, final_demo.csv, final_clin.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
p2_labs = phase2.merge(labs, on="studyid", how="left")          # MERGE ... IF A;
females = mod3lab[mod3lab["sex"] == "female"]                    # WHERE
lifestyle = mod3lab[["studyid", "sex", "smoke", "sleep"]]        # KEEP=

check = final_demo.merge(final_clin[["id"]], on="id", how="left", indicator=True)
unmatched = check[check["_merge"] == "left_only"]
```
