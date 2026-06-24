# =============================================================================
# Phase 09 — Variable Documentation
# Python equivalent of SAS Module 6 (reordered after transformations)
# Libraries: pandas
# =============================================================================
import pandas as pd
import os

DATA_PATH = "./data"

mod6 = pd.read_csv(os.path.join(DATA_PATH, "mod6.csv"))

# ----------------------------------------------------------------------------
# 9.1 Rename columns — equivalent to SAS RENAME=
# ----------------------------------------------------------------------------
mod6.columns = mod6.columns.str.lower().str.strip()

rename_map = {}
if "pt_id"  in mod6.columns: rename_map["pt_id"]  = "studyid"
if "gender" in mod6.columns: rename_map["gender"] = "sex"
if rename_map:
    mod6 = mod6.rename(columns=rename_map)

# ----------------------------------------------------------------------------
# 9.2 Variable labels as a metadata dictionary — equivalent to SAS LABEL
# ----------------------------------------------------------------------------
var_labels = {
    "studyid":   "Unique study participant identifier",
    "age":       "Age in years at enrollment",
    "sex":       "Biological sex (1=Male, 2=Female)",
    "race":      "Self-reported race/ethnicity",
    "vl":        "HIV viral load (copies/mL)",
    "cd4":       "CD4+ T-cell count (cells/mm3)",
    "visitdate": "Date of clinic visit"
}

# ----------------------------------------------------------------------------
# 9.3 Value labels (categorical mapping) — equivalent to SAS FORMAT
# ----------------------------------------------------------------------------
if "sex" in mod6.columns:
    mod6["sex_label"] = mod6["sex"].map({1: "Male", 2: "Female"})

# ----------------------------------------------------------------------------
# 9.4 Codebook — equivalent to SAS PROC CONTENTS + PROC FORMAT listing
# ----------------------------------------------------------------------------
print("--- Variable Codebook ---")
print(f"{'Variable':<22} {'Type':<12} {'Missing':>8}  Label")
print("-" * 70)
for col in mod6.columns:
    dtype   = str(mod6[col].dtype)
    missing = mod6[col].isna().sum()
    label   = var_labels.get(col, "(no label)")
    print(f"  {col:<20} {dtype:<12} {missing:>8}  {label}")

mod6.to_csv(os.path.join(DATA_PATH, "mod6_documented.csv"), index=False)
