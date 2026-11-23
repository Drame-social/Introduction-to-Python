# =============================================================================
# Phase 03 — Data Merging & Subsetting
# Python equivalent of SAS Module 3
# Libraries: pandas
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)


def read_clean(name):
    df = pd.read_csv(os.path.join(DATA_PATH, name))
    df.columns = df.columns.str.strip().str.lower()
    return df


phase2  = read_clean("phase2.csv")
labs    = read_clean("labs.csv")
mod3lab = read_clean("mod3lab.csv")
final_demo = read_clean("final_demo.csv")
final_clin = read_clean("final_clin.csv")

# ----------------------------------------------------------------------------
# 3.1 Merge by ID — equivalent to SAS PROC SORT + DATA ... MERGE ... BY studyid
# ----------------------------------------------------------------------------
p2_labs_all = phase2.merge(labs, on="studyid", how="outer", indicator=True)
print("--- phase2 MERGE labs (all records) ---")
print(p2_labs_all["_merge"].value_counts(), "\n")

# Keep only phase2 records — equivalent to MERGE phase2(IN=A) labs; IF A;
p2_labs = phase2.merge(labs, on="studyid", how="left")
print(f"phase2 records kept: {len(p2_labs)}; with an MTHFR result: "
      f"{p2_labs['mthfr'].notna().sum()}\n")

# ----------------------------------------------------------------------------
# 3.2 Subset rows — equivalent to SAS WHERE / subsetting IF
# ----------------------------------------------------------------------------
females        = mod3lab[mod3lab["sex"] == "female"]
married_smoker = mod3lab[(mod3lab["marital"] == "married") & (mod3lab["smoke"] == 1)]
print(f"mod3lab: {len(mod3lab)} rows; female: {len(females)}; "
      f"married and smoking: {len(married_smoker)}")

# ----------------------------------------------------------------------------
# 3.3 Subset columns — equivalent to SAS KEEP= / DROP=
# ----------------------------------------------------------------------------
lifestyle = mod3lab[["studyid", "sex", "smoke", "sleep", "calorie", "fruit", "vitamin"]]
no_dates  = mod3lab.drop(columns=["bd", "surveydt"])
print(f"KEEP 7 columns: {lifestyle.shape}; DROP 2 columns: {no_dates.shape}\n")

# ----------------------------------------------------------------------------
# 3.4 One-to-one merge of demographic and clinical files on patient ID
# ----------------------------------------------------------------------------
demo_clin = final_demo.merge(final_clin, on="id", how="left", indicator=True)
print("--- final_demo MERGE final_clin ---")
print(demo_clin["_merge"].value_counts())
demo_clin = demo_clin.drop(columns="_merge")

# ----------------------------------------------------------------------------
# 3.5 Anti-join — demographic records with no clinical record
# ----------------------------------------------------------------------------
check = final_demo.merge(final_clin[["id"]], on="id", how="left", indicator=True)
unmatched_demo = check[check["_merge"] == "left_only"].drop(columns="_merge")
print(f"Unmatched demographic records: {len(unmatched_demo)}\n")

# ----------------------------------------------------------------------------
# 3.6 Sort — equivalent to SAS PROC SORT BY htype DESCENDING bleeds
# ----------------------------------------------------------------------------
demo_clin_sorted = demo_clin.sort_values(["htype", "bleeds"], ascending=[True, False])
print(demo_clin_sorted[["id", "htype", "hlevel", "bleeds"]].head(), "\n")

demo_clin.to_csv(os.path.join(OUTPUTS_PATH, "demo_clin_merged.csv"), index=False)
unmatched_demo.to_csv(os.path.join(OUTPUTS_PATH, "unmatched_demo.csv"), index=False)
print("Saved outputs/demo_clin_merged.csv and outputs/unmatched_demo.csv")
