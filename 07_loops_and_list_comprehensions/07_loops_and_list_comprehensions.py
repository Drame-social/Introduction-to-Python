# =============================================================================
# Phase 07 — Loops & List Comprehensions
# Python equivalent of SAS Module 8 (Arrays)
# Libraries: pandas, numpy
# =============================================================================
import pandas as pd
import numpy as np
import os

DATA_PATH = "./data"

mod8_a = pd.read_csv(os.path.join(DATA_PATH, "mod8_a.csv"))

# ----------------------------------------------------------------------------
# 7.1 for loop over columns — equivalent to SAS ARRAY / DO loop
# ----------------------------------------------------------------------------
print("--- Column Summaries ---")
numeric_cols = mod8_a.select_dtypes(include="number").columns.tolist()
for col in numeric_cols:
    print(f"  {col:<20}  mean={mod8_a[col].mean():.2f}  "
          f"missing={mod8_a[col].isna().sum()}")

# ----------------------------------------------------------------------------
# 7.2 List comprehension — Pythonic loop equivalent
# ----------------------------------------------------------------------------
col_means = {col: round(mod8_a[col].mean(), 2) for col in numeric_cols}
print("\n--- Column Means (list comprehension) ---")
for k, v in col_means.items():
    print(f"  {k}: {v}")

# ----------------------------------------------------------------------------
# 7.3 Read multiple datasets in a loop
# ----------------------------------------------------------------------------
dataset_names = ["flbygroup.csv", "screener_data.csv", "survey.csv"]
datasets = {}
for name in dataset_names:
    key = name.replace(".csv", "")
    datasets[key] = pd.read_csv(os.path.join(DATA_PATH, name))
    print(f"  {key:<20}  {datasets[key].shape[0]} rows x {datasets[key].shape[1]} cols")

# ----------------------------------------------------------------------------
# 7.4 Apply function to all numeric columns — equivalent to SAS ARRAY processing
# ----------------------------------------------------------------------------
mod8_a[numeric_cols] = mod8_a[numeric_cols].round(2)

mod8_a.to_csv(os.path.join(DATA_PATH, "mod8_a_processed.csv"), index=False)
