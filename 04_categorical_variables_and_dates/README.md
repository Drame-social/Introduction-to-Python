# Phase 04 — Categorical Variables & Dates

## Topics Covered

Grouping a continuous variable with fixed cut points and with data-driven tertiles, deriving birth weight and BMI, converting SAS date numbers and text dates, and computing age at survey.

## Files

| File | Description |
|------|-------------|
| `04_categorical_variables_and_dates.py` | Create categories and work with dates |

## Datasets Used

mod4.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
mod4["wt3lev_py"]  = pd.cut(mod4["weight"], bins=[0, 126, 149, np.inf], labels=[0, 1, 2])
mod4["wt_tertile"] = pd.qcut(mod4["weight"], q=3, labels=[0, 1, 2])   # PROC RANK GROUPS=3

SAS_EPOCH = pd.Timestamp("1960-01-01")
mod4["birth_date"] = SAS_EPOCH + pd.to_timedelta(mod4["bd"], unit="D")
mod4["calc_age"] = (pd.to_datetime(mod4["surveydt"]) - mod4["birth_date"]).dt.days / 365.25
```
