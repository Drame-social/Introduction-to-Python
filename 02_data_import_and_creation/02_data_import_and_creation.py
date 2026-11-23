# =============================================================================
# Phase 02 — Data Import & Creation
# Python equivalent of SAS Module 2
# Libraries: pandas, xlrd (for the legacy .xls file)
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)


def read_clean(name):
    """Read a CSV from ./data and standardize column names to lowercase."""
    df = pd.read_csv(os.path.join(DATA_PATH, name))
    df.columns = df.columns.str.strip().str.lower()
    return df


# ----------------------------------------------------------------------------
# 2.1 Import a CSV file — equivalent to SAS PROC IMPORT DBMS=CSV
# ----------------------------------------------------------------------------
phase1 = read_clean("phase1.csv")
print(f"phase1: {phase1.shape[0]} rows x {phase1.shape[1]} cols")
print(phase1.dtypes, "\n")

# ----------------------------------------------------------------------------
# 2.2 Import an Excel file — equivalent to SAS PROC IMPORT DBMS=XLS
# ----------------------------------------------------------------------------
rawdat1 = pd.read_excel(os.path.join(DATA_PATH, "raw", "RAWDAT1.xls"))
rawdat1.columns = rawdat1.columns.str.lower()
print(f"rawdat1 (Excel): {rawdat1.shape}")
print(rawdat1.head(), "\n")

# ----------------------------------------------------------------------------
# 2.3 Import a space-delimited text file — equivalent to SAS INFILE / INPUT
#     The file has no header row: study ID, case/control, age, exposure.
# ----------------------------------------------------------------------------
rawdata_txt = pd.read_csv(
    os.path.join(DATA_PATH, "raw", "RAWDATA.TXT"),
    sep=r"\s+", header=None,
    names=["studyid", "caco", "age", "exposure"],
    dtype={"studyid": str},
)
print(f"rawdata_txt (text): {rawdata_txt.shape}")
print(rawdata_txt.head(), "\n")

# ----------------------------------------------------------------------------
# 2.4 Create a dataset in code — equivalent to SAS DATALINES
# ----------------------------------------------------------------------------
sites = pd.DataFrame({
    "site_id":   [1, 2, 3],
    "site_name": ["Clinic North", "Clinic South", "Clinic East"],
    "enrolled":  [42, 37, 51],
})
print(sites, "\n")

# ----------------------------------------------------------------------------
# 2.5 Concatenate (stack) datasets — equivalent to SAS SET cohort1516 cohort1617
# ----------------------------------------------------------------------------
cohort1516 = read_clean("cohort1516.csv")
cohort1617 = read_clean("cohort1617.csv")
cohort_combined = pd.concat([cohort1516, cohort1617], ignore_index=True)
print(f"cohort1516: {len(cohort1516)}  cohort1617: {len(cohort1617)}  "
      f"combined: {len(cohort_combined)}")
print(cohort_combined["yrenroll"].value_counts().sort_index(), "\n")

# ----------------------------------------------------------------------------
# 2.6 Stack the two study phases with a source flag — SAS SET ... IN=
# ----------------------------------------------------------------------------
phase2 = read_clean("phase2.csv")
phases = pd.concat([phase1.assign(phase=1), phase2.assign(phase=2)],
                   ignore_index=True)
print(f"phase1 + phase2 stacked: {len(phases)} rows")
print(phases.groupby("phase")[["age", "bmi"]].mean().round(1), "\n")

# Save outputs (derived files go to ./outputs so ./data stays as distributed)
cohort_combined.to_csv(os.path.join(OUTPUTS_PATH, "cohort_combined.csv"), index=False)
phases.to_csv(os.path.join(OUTPUTS_PATH, "phase1_phase2_stacked.csv"), index=False)
print("Saved outputs/cohort_combined.csv and outputs/phase1_phase2_stacked.csv")
