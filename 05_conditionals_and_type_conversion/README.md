# Phase 05 — Conditionals & Type Conversion

## Topics Covered

Multi-condition logic with np.select(), binary indicators from boolean expressions, type conversions with astype() and pd.to_datetime(), and handling missing values with isna(), fillna(), and dropna().

## Files

| File | Description |
|------|-------------|
| `05_conditionals_and_type_conversion.py` | Conditionals, type conversion, and missing data |

## Datasets Used

final_clin.csv

## Key Python Syntax

```python
import numpy as np

conditions = [df["vl"] < 200, df["vl"] < 1000, df["vl"] < 100000]
choices    = ["Suppressed", "Low", "Moderate"]
df["vl_category"] = np.select(conditions, choices, default="High")

df["suppressed"] = (df["vl"] < 200).astype(int)
df["cd4_imputed"] = df["cd4"].fillna(df["cd4"].mean())
```
