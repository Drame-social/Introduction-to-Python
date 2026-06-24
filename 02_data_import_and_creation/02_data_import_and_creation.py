# =============================================================================
# Phase 02 — Data Import & Creation
# Python equivalent of SAS Module 2
# Libraries: pandas, openpyxl
# =============================================================================
import pandas as pd
import os

DATA_PATH = "./data"

# ----------------------------------------------------------------------------
# 2.1 Import a CSV file
# ----------------------------------------------------------------------------
phase1 = pd.read_csv(os.path.join(DATA_PATH, "phase1.csv"))
print(f"phase1: {phase1.shape[0]} rows x {phase1.shape[1]} cols")
print(phase1.dtypes, "\n")

# ----------------------------------------------------------------------------
# 2.2 Import an Excel file
# ----------------------------------------------------------------------------
rawdat1 = pd.read_excel(os.path.join(DATA_PATH, "raw", "RAWDAT1.xls"))
print(f"rawdat1: {rawdat1.shape}\n")

# ----------------------------------------------------------------------------
# 2.3 Import a delimited text file
# ----------------------------------------------------------------------------
rawdata_txt = pd.read_csv(os.path.join(DATA_PATH, "raw", "RAWDATA.TXT"), sep="\t")

# ----------------------------------------------------------------------------
# 2.4 Concatenate (stack) datasets — equivalent to SAS DATA SET1 SET2
# ----------------------------------------------------------------------------
cohort1516 = pd.read_csv(os.path.join(DATA_PATH, "cohort1516.csv"))
cohort1617 = pd.read_csv(os.path.join(DATA_PATH, "cohort1617.csv"))

cohort_combined = pd.concat([cohort1516, cohort1617], ignore_index=True)
print(f"Combined cohort rows: {len(cohort_combined)}")

# ----------------------------------------------------------------------------
# 2.5 Merge datasets — equivalent to SAS MERGE BY
# ----------------------------------------------------------------------------
phase2 = pd.read_csv(os.path.join(DATA_PATH, "phase2.csv"))
labs   = pd.read_csv(os.path.join(DATA_PATH, "labs.csv"))

# Outer join (SAS MERGE without IN= check)
merged_full  = phase1.merge(phase2, on="studyid", how="outer")
# Inner join (only matched records)
merged_inner = phase2.merge(labs, on="studyid", how="inner")

print(f"Full merge rows:  {len(merged_full)}")
print(f"Inner join rows:  {len(merged_inner)}")

# Save outputs
cohort_combined.to_csv(os.path.join(DATA_PATH, "cohort_combined.csv"), index=False)
merged_full.to_csv(os.path.join(DATA_PATH, "phase1_phase2_merged.csv"), index=False)
