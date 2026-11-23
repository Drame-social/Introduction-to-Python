# =============================================================================
# Phase 05 — Conditionals & Type Conversion
# Python equivalent of SAS Module 5
# Libraries: pandas, numpy
# =============================================================================
import os
import numpy as np
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

grades = pd.read_csv(os.path.join(DATA_PATH, "atlgrades.csv"))
grades.columns = grades.columns.str.lower()

# ----------------------------------------------------------------------------
# 5.1 IF-THEN-ELSE — pass/fail
# ----------------------------------------------------------------------------
grades["course"] = np.where(grades["grade"] >= 60, "Pass", "Fail")
print(grades["course"].value_counts(), "\n")

# ----------------------------------------------------------------------------
# 5.2 IF-THEN / ELSE IF chain — letter grades
#     np.select checks conditions in order, like SAS ELSE IF.
#     (Separate IF statements without ELSE would let later conditions
#     overwrite earlier ones, which is the common SAS mistake this mirrors.)
# ----------------------------------------------------------------------------
conditions = [grades["grade"] >= 90, grades["grade"] >= 80,
              grades["grade"] >= 70, grades["grade"] >= 60]
grades["ltrgrade"] = np.select(conditions, ["A", "B", "C", "D"], default="F")
grades.loc[grades["grade"].isna(), "ltrgrade"] = np.nan
print(grades[["name", "grade", "ltrgrade"]].head(), "\n")
print(pd.crosstab(grades["group"], grades["ltrgrade"]), "\n")

# ----------------------------------------------------------------------------
# 5.3 Character to numeric — equivalent to SAS INPUT() with informats
# ----------------------------------------------------------------------------
print("'50000'     ->", pd.to_numeric("50000"))
print("'15%'       ->", float("15%".rstrip("%")) / 100)
print("'43,000.24' ->", float("43,000.24".replace(",", "")))
print("'01-11-2019'->", pd.to_datetime("01-11-2019", format="%m-%d-%Y").date(), "\n")

# ----------------------------------------------------------------------------
# 5.4 Numeric to character — equivalent to SAS PUT()
# ----------------------------------------------------------------------------
grades["grade_txt"] = grades["grade"].map(lambda g: f"{g:.0f}" if pd.notna(g) else "")
grades["attend_txt"] = grades["attendx"].map({1: "Attended", 0: "Absent"})
print(grades.dtypes, "\n")

# ----------------------------------------------------------------------------
# 5.5 Missing values in conditions
# ----------------------------------------------------------------------------
print(f"Missing grades: {grades['grade'].isna().sum()}")

grades.to_csv(os.path.join(OUTPUTS_PATH, "atlgrades_processed.csv"), index=False)
print("Saved outputs/atlgrades_processed.csv")
