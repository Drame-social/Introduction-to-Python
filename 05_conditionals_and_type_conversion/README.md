# Phase 05 — Conditionals & Type Conversion

## Topics Covered

IF-THEN-ELSE logic with np.where(), ordered ELSE IF chains with np.select(), converting text to numbers and dates (SAS INPUT), converting numbers to text (SAS PUT), and missing values in conditions.

## Files

| File | Description |
|------|-------------|
| `05_conditionals_and_type_conversion.py` | Conditionals, type conversion, and missing data |

## Datasets Used

atlgrades.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
grades["course"] = np.where(grades["grade"] >= 60, "Pass", "Fail")

conditions = [grades["grade"] >= 90, grades["grade"] >= 80,
              grades["grade"] >= 70, grades["grade"] >= 60]
grades["ltrgrade"] = np.select(conditions, ["A", "B", "C", "D"], default="F")

pd.to_datetime("01-11-2019", format="%m-%d-%Y")   # INPUT(x, mmddyy10.)
```
