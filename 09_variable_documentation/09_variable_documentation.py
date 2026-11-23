# =============================================================================
# Phase 09 — Variable Documentation
# Python equivalent of SAS Module 6 (labels, formats, codebook)
# Libraries: pandas
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

mod6 = pd.read_csv(os.path.join(DATA_PATH, "mod6.csv"))
mod6.columns = mod6.columns.str.lower().str.strip()

# ----------------------------------------------------------------------------
# 9.1 Variable labels as a metadata dictionary — equivalent to SAS LABEL
#     Labels below come from how each variable is derived or labeled in the
#     SAS version of this module. Variables without a documented meaning are
#     left unlabeled rather than guessed.
# ----------------------------------------------------------------------------
var_labels = {
    "studyid":  "Participant identifier",
    "sex1":     "Gender (numeric code)",
    "wt3lev":   "Weight category (3 levels)",
    "wt2lev":   "Weight category (2 levels)",
    "bd":       "Birth date (SAS date value)",
    "surveydt": "Survey date",
    "weight":   "Weight (lb)",
    "heightft": "Height, feet component",
    "heightin": "Height, inches component",
    "birthlb":  "Birth weight, pounds component",
    "birthoz":  "Birth weight, ounces component",
    "bw_oz":    "Birth weight (oz)",
    "bw_gm":    "Birth weight (g)",
    "bw_gm1":   "Low birth weight (<=2500 g)",
    "ht_in":    "Height (in)",
    "weightkg": "Weight (kg)",
    "heightm":  "Height (m)",
    "bmi":      "Body mass index (kg/m2)",
    "calc_age": "Exact age at survey (years)",
    "entryage": "Participant age at enrollment",
    "kids":     "Total number of kids in household",
}

# ----------------------------------------------------------------------------
# 9.2 Value labels — equivalent to SAS PROC FORMAT
# ----------------------------------------------------------------------------
yesno = {0: "No", 1: "Yes"}
for col in ["smoke", "plane", "vitamin"]:
    mod6[f"{col}_label"] = mod6[col].map(yesno)

mod6["age_group"] = pd.cut(mod6["entryage"], bins=[14, 24, 29, 100],
                           labels=["<25", "25-29", "30+"])

print("--- Smoking by weight category (formatted) ---")
print(pd.crosstab(mod6["smoke_label"], mod6["wt3lev"]), "\n")
print("--- Age group by smoking ---")
print(pd.crosstab(mod6["age_group"], mod6["smoke_label"]), "\n")

# ----------------------------------------------------------------------------
# 9.3 Codebook — equivalent to SAS PROC CONTENTS
# ----------------------------------------------------------------------------
codebook = pd.DataFrame({
    "variable": mod6.columns,
    "type":     [str(mod6[c].dtype) for c in mod6.columns],
    "n_missing": [int(mod6[c].isna().sum()) for c in mod6.columns],
    "n_unique": [int(mod6[c].nunique()) for c in mod6.columns],
    "label":    [var_labels.get(c, "") for c in mod6.columns],
})
print(codebook.to_string(index=False))

codebook.to_csv(os.path.join(OUTPUTS_PATH, "mod6_codebook.csv"), index=False)
mod6.to_csv(os.path.join(OUTPUTS_PATH, "mod6_documented.csv"), index=False)
print("\nSaved outputs/mod6_codebook.csv and outputs/mod6_documented.csv")
