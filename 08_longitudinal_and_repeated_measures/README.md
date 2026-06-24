# Phase 08 — Longitudinal & Repeated Measures

## Topics Covered

Sorting and creating lag variables with groupby().shift(), group-level aggregation with groupby().agg(), wide-to-long reshaping with pd.melt(), long-to-wide with pivot_table(), and selecting first/last records per subject.

## Files

| File | Description |
|------|-------------|
| `08_longitudinal_and_repeated_measures.py` | Longitudinal analysis and reshaping |

## Datasets Used

mod9.csv, mod8_c.csv

## Key Python Syntax

```python
# Lag within group
df = df.sort_values(["studyid","visitdate"])
df["prev_vl"] = df.groupby("studyid")["vl"].shift(1)

# Group summary
summary = df.groupby("studyid").agg(
    n_visits=("visitdate","count"),
    mean_vl =("vl","mean")).reset_index()

# Wide → Long
long_df = df.melt(id_vars=id_cols, value_vars=visit_cols,
                  var_name="visit", value_name="result")
```
