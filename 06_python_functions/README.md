# Phase 06 — Python Functions

## Topics Covered

String methods (str.upper, str[:n], str.strip, str.match), numeric functions from numpy (round, sqrt, floor, abs), descriptive statistics with describe(), and writing custom functions applied with .apply().

## Files

| File | Description |
|------|-------------|
| `06_python_functions.py` | String, numeric, and custom functions |

## Datasets Used

patients.csv

## Key Python Syntax

```python
# String functions
df["name_upper"] = df["name"].str.upper()
df["first3"]     = df["name"].str[:3]

# Custom function applied to a column
def bmi_category(bmi):
    if pd.isna(bmi): return None
    elif bmi < 18.5: return "Underweight"
    elif bmi < 25:   return "Normal"
    else:            return "Overweight/Obese"

df["bmi_cat"] = df["bmi"].apply(bmi_category)
```
