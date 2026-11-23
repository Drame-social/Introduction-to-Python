# Phase 09 — Variable Documentation

## Topics Covered

Variable labels kept as a metadata dictionary (SAS LABEL), value labels with map() and pd.cut() (PROC FORMAT), formatted cross-tabulations, and a codebook table (PROC CONTENTS). Variables without a documented meaning are left unlabeled.

## Files

| File | Description |
|------|-------------|
| `09_variable_documentation.py` | Labels, value formats, and codebook |

## Datasets Used

mod6.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
yesno = {0: "No", 1: "Yes"}
mod6["smoke_label"] = mod6["smoke"].map(yesno)
mod6["age_group"] = pd.cut(mod6["entryage"], bins=[14, 24, 29, 100],
                           labels=["<25", "25-29", "30+"])
```
