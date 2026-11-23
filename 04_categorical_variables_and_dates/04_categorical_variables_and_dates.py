# =============================================================================
# Phase 04 — Categorical Variables & Dates
# Python equivalent of SAS Module 4
# Libraries: pandas, numpy
# =============================================================================
import os
import numpy as np
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

# SAS stores dates as days since 1 January 1960
SAS_EPOCH = pd.Timestamp("1960-01-01")

mod4 = pd.read_csv(os.path.join(DATA_PATH, "mod4.csv"))
mod4.columns = mod4.columns.str.lower()

# ----------------------------------------------------------------------------
# 4.1 Distribution of a continuous variable — equivalent to PROC UNIVARIATE
# ----------------------------------------------------------------------------
print("--- Weight (lb) ---")
print(mod4["weight"].describe().round(1), "\n")

# ----------------------------------------------------------------------------
# 4.2 Two-level and three-level categories — equivalent to IF-THEN grouping
# ----------------------------------------------------------------------------
mod4["wt2lev_py"] = np.where(mod4["weight"] > 135, 1,
                             np.where(mod4["weight"] > 0, 0, np.nan))
mod4["wt3lev_py"] = pd.cut(mod4["weight"], bins=[0, 126, 149, np.inf],
                           labels=[0, 1, 2], right=True)
print("--- WT2LEV (0: <=135 lb, 1: >135 lb) ---")
print(mod4["wt2lev_py"].value_counts(dropna=False).sort_index(), "\n")
print("--- WT3LEV (cut points 126 and 149 lb) ---")
print(mod4["wt3lev_py"].value_counts(dropna=False).sort_index(), "\n")

# Tertiles from the data — equivalent to PROC RANK GROUPS=3
mod4["wt_tertile"] = pd.qcut(mod4["weight"], q=3, labels=[0, 1, 2])
print("--- Weight tertiles (PROC RANK GROUPS=3) ---")
print(mod4["wt_tertile"].value_counts(dropna=False).sort_index(), "\n")

# ----------------------------------------------------------------------------
# 4.3 Derived numeric variables — birth weight and BMI
# ----------------------------------------------------------------------------
mod4["bw_oz"]   = mod4["birthlb"] * 16 + mod4["birthoz"]
mod4["bw_gm"]   = mod4["bw_oz"] * 28.35
mod4["low_bw"]  = np.where(mod4["bw_gm"].isna(), np.nan, (mod4["bw_gm"] <= 2500).astype(float))
mod4["ht_in"]   = mod4["heightft"] * 12 + mod4["heightin"]
mod4["weightkg"] = mod4["weight"] * 0.4536
mod4["heightm"] = mod4["ht_in"] * 0.0254
mod4["bmi"]     = mod4["weightkg"] / mod4["heightm"] ** 2
print("--- Low birth weight (<=2500 g) ---")
print(mod4["low_bw"].value_counts(dropna=False), "\n")
print("--- BMI ---")
print(mod4["bmi"].describe().round(1), "\n")

# ----------------------------------------------------------------------------
# 4.4 Dates — convert a SAS date number and a text date, then compute age
# ----------------------------------------------------------------------------
mod4["birth_date"]  = SAS_EPOCH + pd.to_timedelta(mod4["bd"], unit="D")
mod4["survey_date"] = pd.to_datetime(mod4["surveydt"], errors="coerce")
mod4["calc_age"]    = (mod4["survey_date"] - mod4["birth_date"]).dt.days / 365.25
mod4["entryage"]    = np.floor(mod4["calc_age"])
mod4["survey_year"] = mod4["survey_date"].dt.year

print(mod4[["studyid", "birth_date", "survey_date", "calc_age", "entryage"]].head(), "\n")
print("--- Survey year ---")
print(mod4["survey_year"].value_counts().sort_index(), "\n")

mod4.to_csv(os.path.join(OUTPUTS_PATH, "mod4_processed.csv"), index=False)
print("Saved outputs/mod4_processed.csv")
