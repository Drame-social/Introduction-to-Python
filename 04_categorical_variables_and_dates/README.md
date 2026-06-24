# Phase 04 — Categorical Variables & Dates

## Topics Covered

Creating binned categories with pd.cut(), mapping value labels with .map(), computing value frequencies with value_counts(), parsing dates with pd.to_datetime(), date arithmetic, and extracting year/month from datetime columns.

## Files

| File | Description |
|------|-------------|
| `04_categorical_variables_and_dates.py` | Create categories and work with dates |

## Datasets Used

mod4.csv

## Key Python Syntax

```python
import pandas as pd, numpy as np

# Categorize age
df["age_group"] = pd.cut(df["age"],
    bins   = [0, 17, 34, 49, 64, np.inf],
    labels = ["<18","18-34","35-49","50-64","65+"])

# Date arithmetic
df["visitdate_dt"] = pd.to_datetime(df["visitdate"])
df["visit_year"]   = df["visitdate_dt"].dt.year
```
