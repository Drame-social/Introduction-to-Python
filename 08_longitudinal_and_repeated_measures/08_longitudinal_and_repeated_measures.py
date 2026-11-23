# =============================================================================
# Phase 08 — Longitudinal & Repeated Measures
# Python equivalent of SAS Module 9
# Data: patients.csv has one row per visit and several visits per patient.
# Libraries: pandas
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

patients = pd.read_csv(os.path.join(DATA_PATH, "patients.csv"))
patients["visdate"] = pd.to_datetime(patients["visdate"], errors="coerce")

# ----------------------------------------------------------------------------
# 8.1 Visits per patient — SAS PROC SUMMARY CLASS id; SUM of VISIT=1
# ----------------------------------------------------------------------------
totvisit = patients.groupby("id").size().rename("totvisit")
print(f"Patients: {patients['id'].nunique()}  Visits: {len(patients)}")
print("--- Visits per patient ---")
print(totvisit.value_counts().sort_index(), "\n")

# ----------------------------------------------------------------------------
# 8.2 First visit per patient — SAS BY id; IF FIRST.id
# ----------------------------------------------------------------------------
patients = patients.sort_values(["id", "visdate"]).reset_index(drop=True)
first_visit = patients.groupby("id").head(1)
print("--- Full-time employment at baseline (empft) ---")
print(first_visit["empft"].value_counts(dropna=False), "\n")

# ----------------------------------------------------------------------------
# 8.3 Visit number, lag and change — SAS RETAIN / LAG within BY group
# ----------------------------------------------------------------------------
patients["visit_number"] = patients.groupby("id").cumcount() + 1
patients["prev_weight"]  = patients.groupby("id")["weight"].shift(1)
patients["weight_change"] = patients["weight"] - patients["prev_weight"]
patients["days_since_prev"] = patients.groupby("id")["visdate"].diff().dt.days
print(patients[["id", "visdate", "visit_number", "weight",
                "weight_change", "days_since_prev"]].head(6), "\n")

# ----------------------------------------------------------------------------
# 8.4 Per-patient summaries merged back to baseline — SAS PROC SUMMARY + MERGE
# ----------------------------------------------------------------------------
per_patient = patients.groupby("id").agg(
    totvisit   = ("visdate", "count"),
    avgblds    = ("allblds", "mean"),
    avgjtblds  = ("jtblds", "mean"),
    everempft  = ("empft", "max"),
).reset_index()
baseline = first_visit.merge(per_patient, on="id", how="left")
print("--- Average bleeds per visit, per patient ---")
print(per_patient["avgblds"].describe().round(2), "\n")

# ----------------------------------------------------------------------------
# 8.5 Wide to long — SAS PROC TRANSPOSE (clot locations in mod8_c)
# ----------------------------------------------------------------------------
mod8_c = pd.read_csv(os.path.join(DATA_PATH, "mod8_c.csv"))
loc_cols = [c for c in mod8_c.columns if c.startswith("LOCATN")]
mod8_c_long = (mod8_c.melt(id_vars=["STUDYID", "RELTCLOT"], value_vars=loc_cols,
                           var_name="position", value_name="location")
                     .dropna(subset=["location"])
                     .sort_values(["STUDYID", "position"]))
print(f"mod8_c wide: {mod8_c.shape} -> long (non-missing): {mod8_c_long.shape}")

# Long back to wide
mod8_c_wide = mod8_c_long.pivot(index="STUDYID", columns="position",
                                values="location").reset_index()
print(f"Back to wide: {mod8_c_wide.shape}\n")

baseline.to_csv(os.path.join(OUTPUTS_PATH, "patient_baseline_summary.csv"), index=False)
mod8_c_long.to_csv(os.path.join(OUTPUTS_PATH, "mod8_c_long.csv"), index=False)
print("Saved outputs/patient_baseline_summary.csv and outputs/mod8_c_long.csv")
