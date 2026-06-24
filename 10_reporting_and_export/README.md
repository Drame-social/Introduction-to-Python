# Phase 10 — Reporting & Export

## Topics Covered

Generating descriptive statistics with describe() and value_counts(), cross-tabulations with pd.crosstab(), exporting multi-sheet Excel workbooks with pd.ExcelWriter, and writing CSVs with to_csv().

## Files

| File | Description |
|------|-------------|
| `10_reporting_and_export.py` | Summary tables and file export |

## Datasets Used

final_demo.csv, final_clin.csv

## Key Python Syntax

```python
# Cross-tabulation
pd.crosstab(df["sex"], df["suppressed"],
            normalize="index").round(3)

# Multi-sheet Excel export
with pd.ExcelWriter("outputs/report.xlsx",
                    engine="openpyxl") as writer:
    demo.to_excel(writer, sheet_name="Demographics", index=False)
    clin.to_excel(writer, sheet_name="Clinical",     index=False)
```
