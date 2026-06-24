# =============================================================================
# Phase 08 — Longitudinal & Repeated Measures
# Python equivalent of SAS Module 9
# Libraries: pandas
# =============================================================================
import pandas as pd
import os

DATA_PATH = "./data"

mod9   = pd.read_csv(os.path.join(DATA_PATH, "mod9.csv"))
mod8_c = pd.read_csv(os.path.join(DATA_PATH, "mod8_c.csv"))

# ----------------------------------------------------------------------------
# 8.1 Sort and lag — equivalent to SAS LAG() / RETAIN
# ----------------------------------------------------------------------------
mod9 = mod9.sort_values(["studyid", "visitdate"]).reset_index(drop=True)
mod9["prev_vl"]     = mod9.groupby("studyid")["vl"].shift(1)
mod9["vl_change"]   = mod9["vl"] - mod9["prev_vl"]
mod9["visit_number"]= mod9.groupby("studyid").cumcount() + 1

# ----------------------------------------------------------------------------
# 8.2 Group-level summaries — equivalent to PROC MEANS / PROC SUMMARY BY
# ----------------------------------------------------------------------------
patient_summary = mod9.groupby("studyid").agg(
    n_visits        = ("visitdate", "count"),
    first_visit     = ("visitdate", "min"),
    last_visit      = ("visitdate", "max"),
    mean_vl         = ("vl",        lambda x: round(x.mean(), 1)),
    min_cd4         = ("cd4",       "min"),
    max_cd4         = ("cd4",       "max"),
    ever_suppressed = ("vl",        lambda x: (x < 200).any())
).reset_index()

print(f"Patients summarized: {len(patient_summary)}")

# ----------------------------------------------------------------------------
# 8.3 Wide ↔ Long reshape — equivalent to SAS PROC TRANSPOSE
# ----------------------------------------------------------------------------
visit_cols = [c for c in mod8_c.columns if c.startswith("visit")]
id_cols    = [c for c in mod8_c.columns if not c.startswith("visit")]

# Wide → Long
mod8_c_long = mod8_c.melt(id_vars=id_cols, value_vars=visit_cols,
                           var_name="visit_num", value_name="result")

# Long → Wide
mod8_c_wide = mod8_c_long.pivot_table(index=id_cols, columns="visit_num",
                                       values="result").reset_index()

# ----------------------------------------------------------------------------
# 8.4 First and last visit per subject
# ----------------------------------------------------------------------------
first_visits = mod9.sort_values("visitdate").groupby("studyid").first().reset_index()
last_visits  = mod9.sort_values("visitdate").groupby("studyid").last().reset_index()

patient_summary.to_csv(os.path.join(DATA_PATH, "patient_longitudinal_summary.csv"), index=False)
mod8_c_long.to_csv(os.path.join(DATA_PATH, "mod8_c_long.csv"), index=False)
