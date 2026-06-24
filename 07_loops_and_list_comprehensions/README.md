# Phase 07 — Loops & List Comprehensions

## Topics Covered

for loops over column names, computing column-level statistics inside loops, list comprehensions as a concise loop alternative, reading multiple datasets in a loop, and using DataFrame.apply() for row/column operations.

## Files

| File | Description |
|------|-------------|
| `07_loops_and_list_comprehensions.py` | Loops, list comprehensions, and batch reads |

## Datasets Used

mod8_a.csv, flbygroup.csv, screener_data.csv, survey.csv

## Key Python Syntax

```python
# Loop over columns
for col in numeric_cols:
    print(f"{col}: mean={df[col].mean():.2f}")

# List comprehension
means = {col: round(df[col].mean(), 2) for col in numeric_cols}

# Batch read
datasets = {name: pd.read_csv(f"./data/{name}.csv")
            for name in file_list}
```
