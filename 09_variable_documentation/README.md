# Phase 09 — Variable Documentation

## Topics Covered

Renaming columns with rename() and str.lower(), storing variable labels in a Python dictionary, mapping value labels to create readable categorical columns, and printing a codebook with column types, missing counts, and labels.

## Files

| File | Description |
|------|-------------|
| `09_variable_documentation.py` | Column renaming, labels, and codebook |

## Datasets Used

mod6.csv

## Key Python Syntax

```python
# Rename columns
df.columns = df.columns.str.lower().str.strip()
df = df.rename(columns={"pt_id":"studyid","gender":"sex"})

# Variable label dictionary
var_labels = {
    "studyid": "Unique study participant identifier",
    "age":     "Age in years at enrollment"}

# Value labels
df["sex_label"] = df["sex"].map({1:"Male", 2:"Female"})
```
