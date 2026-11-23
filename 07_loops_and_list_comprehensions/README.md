# Phase 07 — Loops & List Comprehensions

## Topics Covered

Python loops and vectorized operations as equivalents of SAS arrays: recoding a missing-value code across many columns, scoring across items, flagging any matching code across columns, and counting non-missing entries.

## Files

| File | Description |
|------|-------------|
| `07_loops_and_list_comprehensions.py` | Loops, list comprehensions, and batch reads |

## Datasets Used

mod8_a.csv, mod8_b.csv, mod8_c.csv, mod8_d.csv, flbygroup.csv, screener_data.csv, survey.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
for col in var_cols:                                   # ARRAY ... DO i = 1 TO 15
    mod8_a[col] = mod8_a[col].replace(9, np.nan)

mod8_c["LOC"] = mod8_c[loc_cols].isin([1, 2, 6, 7]).any(axis=1).astype(int)
mod8_d["DRUGS"] = mod8_d[drug_cols].notna().sum(axis=1)
```
