# Phase 06 — Python Functions

## Topics Covered

Character functions (equivalents of SAS COMPRESS, UPCASE, SCAN, SUBSTR, INDEX, COUNTW), numeric functions across columns (MEAN, SUM, N, ABS, INT, SQRT), date parts, and a user-defined function.

## Files

| File | Description |
|------|-------------|
| `06_python_functions.py` | String, numeric, and custom functions |

## Datasets Used

mock_data.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
mock["phone_digits"] = mock["phone_num"].str.replace(r"\D", "", regex=True)  # COMPRESS
mock["email_domain"] = mock["email"].str.split("@").str[1]                    # SCAN
mock["score_mean"]   = mock[score_cols].mean(axis=1)                          # MEAN(of ...)
mock["score_band"]   = mock["score_mean"].apply(score_band)
```
