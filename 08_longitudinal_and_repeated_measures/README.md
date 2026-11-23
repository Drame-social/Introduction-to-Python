# Phase 08 — Longitudinal & Repeated Measures

## Topics Covered

Working with several visits per patient: visits per patient, first visit (SAS FIRST.), visit numbers, lagged values and change, per-patient summaries merged back to baseline, and reshaping wide to long and back (PROC TRANSPOSE).

## Files

| File | Description |
|------|-------------|
| `08_longitudinal_and_repeated_measures.py` | Longitudinal analysis and reshaping |

## Datasets Used

patients.csv, mod8_c.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
patients = patients.sort_values(["id", "visdate"])
first_visit = patients.groupby("id").head(1)                      # IF FIRST.id
patients["prev_weight"] = patients.groupby("id")["weight"].shift(1)   # LAG

per_patient = patients.groupby("id").agg(totvisit=("visdate", "count"),
                                         avgblds=("allblds", "mean"))
```
