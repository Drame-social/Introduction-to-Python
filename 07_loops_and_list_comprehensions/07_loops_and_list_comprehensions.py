# =============================================================================
# Phase 07 — Loops & List Comprehensions
# Python equivalent of SAS Module 8 (Arrays)
# Libraries: pandas, numpy
# =============================================================================
import os
import numpy as np
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

mod8_a = pd.read_csv(os.path.join(DATA_PATH, "mod8_a.csv"))
mod8_b = pd.read_csv(os.path.join(DATA_PATH, "mod8_b.csv"))
mod8_c = pd.read_csv(os.path.join(DATA_PATH, "mod8_c.csv"))
mod8_d = pd.read_csv(os.path.join(DATA_PATH, "mod8_d.csv"))

# ----------------------------------------------------------------------------
# 7.1 Recode a missing-value code across many columns
#     SAS: ARRAY blanks{15} var1-var15; DO i=1 TO 15; IF blanks{i}=9 THEN .
# ----------------------------------------------------------------------------
var_cols = [f"var{i}" for i in range(1, 16)]
before = (mod8_a[var_cols] == 9).sum().sum()
for col in var_cols:                                  # explicit loop
    mod8_a[col] = mod8_a[col].replace(9, np.nan)
print(f"Values coded 9 recoded to missing: {before}")

# Same result with one vectorized statement
check = pd.read_csv(os.path.join(DATA_PATH, "mod8_a.csv"))
check[var_cols] = check[var_cols].mask(check[var_cols] == 9)
print("Loop and vectorized versions agree:", mod8_a.equals(check), "\n")

# ----------------------------------------------------------------------------
# 7.2 Score across columns, missing if any item is missing (SAS Example 2)
# ----------------------------------------------------------------------------
tests = ["TEST1", "TEST2", "TEST3"]
mod8_b["score"] = mod8_b[tests].sum(axis=1, min_count=len(tests))
print("--- Score (0-3) ---")
print(mod8_b["score"].value_counts(dropna=False).sort_index(), "\n")

# ----------------------------------------------------------------------------
# 7.3 Flag if any column holds a target code (SAS Example 3)
#     LOC = 1 if any LOCATN1-10 is in (1, 2, 6, 7); FAMHIS = RELTCLOT and LOC
# ----------------------------------------------------------------------------
loc_cols = [f"LOCATN{i}" for i in range(1, 11)]
mod8_c["LOC"] = mod8_c[loc_cols].isin([1, 2, 6, 7]).any(axis=1).astype(int)
mod8_c["FAMHIS"] = ((mod8_c["RELTCLOT"] == 1) & (mod8_c["LOC"] == 1)).astype(int)
print(mod8_c.groupby(["RELTCLOT", "LOC", "FAMHIS"]).size().rename("n"), "\n")

# ----------------------------------------------------------------------------
# 7.4 Count non-missing entries across 21 columns (SAS Example 4)
# ----------------------------------------------------------------------------
drug_cols = [c for c in mod8_d.columns if c.startswith("DRUG")]
mod8_d["DRUGS"] = mod8_d[drug_cols].notna().sum(axis=1)
print("--- Number of drug entries per person ---")
print(mod8_d["DRUGS"].value_counts().sort_index(), "\n")

# ----------------------------------------------------------------------------
# 7.5 Dictionary comprehension and a loop over files
# ----------------------------------------------------------------------------
col_missing = {c: int(mod8_a[c].isna().sum()) for c in var_cols}
print("Missing per column:", col_missing, "\n")

for name in ["flbygroup.csv", "screener_data.csv", "survey.csv"]:
    df = pd.read_csv(os.path.join(DATA_PATH, name))
    print(f"  {name:<20} {df.shape[0]} rows x {df.shape[1]} cols")

mod8_a.to_csv(os.path.join(OUTPUTS_PATH, "mod8_a_recoded.csv"), index=False)
print("\nSaved outputs/mod8_a_recoded.csv")
