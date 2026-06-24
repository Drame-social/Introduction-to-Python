# Phase 11 — Automation & Pipelines

## Topics Covered

Writing reusable analysis functions with **kwargs-style flexibility, running functions across multiple outcomes in a loop, batch processing datasets with list comprehensions, and composing full end-to-end pipeline functions.

## Files

| File | Description |
|------|-------------|
| `11_automation_and_pipelines.py` | Reusable functions and batch pipelines |

## Datasets Used

final_demo.csv, final_clin.csv, mod3lab.csv, mod4.csv, mod6.csv, mod9.csv

## Key Python Syntax

```python
def summarize_cohort(df, group_col, outcome_col):
    return (df.groupby(group_col)[outcome_col]
              .agg(n="count",
                   mean=lambda x: round(x.mean(),2))
              .reset_index())

# Batch apply
results = [run_vl_pipeline(f)
           for f in ["mod3lab.csv","mod9.csv"]]
```
