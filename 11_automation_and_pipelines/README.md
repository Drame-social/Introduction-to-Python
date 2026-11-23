# Phase 11 — Automation & Pipelines

## Topics Covered

Parameterized functions as equivalents of SAS macros, loops over datasets (%DO), and a small pipeline function that reads, cleans, summarizes, and saves in one call.

## Files

| File | Description |
|------|-------------|
| `11_automation_and_pipelines.py` | Reusable functions and batch pipelines |

## Datasets Used

final_demo.csv, final_clin.csv, mod3lab.csv, mod4.csv, mod6.csv, mod9.csv, patients.csv, screener_data.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
def summarize_by(df, group_col, outcome_col):
    g = df.groupby(group_col, dropna=False)[outcome_col]
    return pd.DataFrame({"n": g.count(), "mean": g.mean(), "sd": g.std()})

summarize_by(demo_clin, "hlevel", "bleeds")
run_screening_pipeline("screener_data.csv", "screening_by_site_month.csv")
```
