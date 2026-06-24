# =============================================================================
# Phase 03 — Data Merging & Subsetting
# Python equivalent of SAS Module 3
# Libraries: pandas
# =============================================================================
import pandas as pd
import os

DATA_PATH = "./data"

mod3lab    = pd.read_csv(os.path.join(DATA_PATH, "mod3lab.csv"))
final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))

# ----------------------------------------------------------------------------
# 3.1 Subset rows — equivalent to SAS WHERE / IF
# ----------------------------------------------------------------------------
hiv_positive  = mod3lab[mod3lab["hivstatus"] == 1]
adults_hiv    = mod3lab[(mod3lab["hivstatus"] == 1) & (mod3lab["age"] >= 18)]
print(f"HIV-positive records: {len(hiv_positive)}")

# ----------------------------------------------------------------------------
# 3.2 Subset columns — equivalent to SAS KEEP=
# ----------------------------------------------------------------------------
demo_slim = final_demo[["studyid", "age", "sex", "race"]]

# ----------------------------------------------------------------------------
# 3.3 Left and inner merges — equivalent to SAS MERGE with IN=
# ----------------------------------------------------------------------------
demo_clin_left  = final_demo.merge(final_clin, on="studyid", how="left")
demo_clin_inner = final_demo.merge(final_clin, on="studyid", how="inner")

print(f"Left merge rows:  {len(demo_clin_left)}")
print(f"Inner merge rows: {len(demo_clin_inner)}")

# ----------------------------------------------------------------------------
# 3.4 Anti-join — records in demo NOT matched in clinical
# ----------------------------------------------------------------------------
merged_indicator = final_demo.merge(
    final_clin[["studyid"]], on="studyid", how="left", indicator=True)
unmatched_demo = merged_indicator[merged_indicator["_merge"] == "left_only"].drop(
    columns="_merge")
print(f"Unmatched demo records: {len(unmatched_demo)}")

# ----------------------------------------------------------------------------
# 3.5 Sort a dataset — equivalent to SAS PROC SORT
# ----------------------------------------------------------------------------
mod3_sorted = mod3lab.sort_values(["studyid", "visitdate"], ascending=[True, False])

demo_clin_left.to_csv(os.path.join(DATA_PATH, "demo_clin_merged.csv"), index=False)
unmatched_demo.to_csv(os.path.join(DATA_PATH, "unmatched_demo.csv"), index=False)
