# =============================================================================
# Phase 04 — Categorical Variables & Dates
# Python equivalent of SAS Module 4
# Libraries: pandas, numpy
# =============================================================================
import pandas as pd
import numpy as np
import os

DATA_PATH = "./data"

mod4 = pd.read_csv(os.path.join(DATA_PATH, "mod4.csv"))

# ----------------------------------------------------------------------------
# 4.1 Create categorical variable from numeric — equivalent to SAS FORMAT
# ----------------------------------------------------------------------------
mod4["age_group"] = pd.cut(
    mod4["age"],
    bins   = [0, 17, 34, 49, 64, np.inf],
    labels = ["<18", "18-34", "35-49", "50-64", "65+"],
    right  = True
)

mod4["sex_label"] = mod4["sex"].map({1: "Male", 2: "Female"})

# ----------------------------------------------------------------------------
# 4.2 Frequency counts — equivalent to SAS PROC FREQ
# ----------------------------------------------------------------------------
print("--- Age Group Distribution ---")
print(mod4["age_group"].value_counts().sort_index())

print("\n--- Sex Distribution ---")
print(mod4["sex_label"].value_counts())

# ----------------------------------------------------------------------------
# 4.3 Date parsing and arithmetic — equivalent to SAS date functions
# ----------------------------------------------------------------------------
mod4["visitdate_dt"] = pd.to_datetime(mod4["visitdate"], errors="coerce")
mod4["birthdate_dt"] = pd.to_datetime(mod4["birthdate"], errors="coerce")

mod4["age_calc"]    = ((mod4["visitdate_dt"] - mod4["birthdate_dt"]).dt.days / 365.25).astype("Int64")
mod4["visit_year"]  = mod4["visitdate_dt"].dt.year
mod4["visit_month"] = mod4["visitdate_dt"].dt.month_name()

print("\n--- Visit Year Distribution ---")
print(mod4["visit_year"].value_counts().sort_index())

mod4.to_csv(os.path.join(DATA_PATH, "mod4_processed.csv"), index=False)
