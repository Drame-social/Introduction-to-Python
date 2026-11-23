# Phase 10 — Reporting & Export

## Topics Covered

Frequency tables with percentages, grouped descriptive statistics, cross-tabulations with counts and row percentages, and exporting a multi-sheet Excel report and a CSV file.

## Files

| File | Description |
|------|-------------|
| `10_reporting_and_export.py` | Summary tables and file export |

## Datasets Used

final_demo.csv, final_clin.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
demo_clin = final_demo.merge(final_clin, on="id", how="left")
demo_clin.groupby("hlevel")["bleeds"].agg(["count", "mean", "std", "median"])
pd.crosstab(demo_clin["htype"], demo_clin["hlevel"], normalize="index")

with pd.ExcelWriter("outputs/clinical_cohort_report.xlsx") as writer:
    summary_tbl.to_excel(writer, sheet_name="Summary", index=False)
```
