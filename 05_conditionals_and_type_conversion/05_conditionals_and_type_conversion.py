# =============================================================================
# Phase 05 — Conditionals & Type Conversion
# Python equivalent of SAS Module 5
# Libraries: pandas, numpy
# =============================================================================
import pandas as pd
import numpy as np
import os

DATA_PATH = "./data"

final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))

# ----------------------------------------------------------------------------
# 5.1 Multi-condition logic — equivalent to SAS IF-THEN-ELSE / SELECT
# ----------------------------------------------------------------------------
conditions = [
    final_clin["vl"] < 200,
    final_clin["vl"] < 1000,
    final_clin["vl"] < 100000
]
choices = ["Suppressed", "Low", "Moderate"]
final_clin["vl_category"] = np.select(conditions, choices, default="High")

# ----------------------------------------------------------------------------
# 5.2 Binary indicator — equivalent to SAS IF x THEN y = 1
# ----------------------------------------------------------------------------
final_clin["suppressed"]   = (final_clin["vl"] < 200).astype(int)
final_clin["on_art"]       = final_clin["art_start_date"].notna().astype(int)
final_clin["missing_cd4"]  = final_clin["cd4"].isna().astype(int)

# ----------------------------------------------------------------------------
# 5.3 Type conversion — equivalent to SAS INPUT() and PUT()
# ----------------------------------------------------------------------------
final_clin["studyid_str"]  = final_clin["studyid"].astype(str)
final_clin["art_date_dt"]  = pd.to_datetime(final_clin["art_start_date"], errors="coerce")

# ----------------------------------------------------------------------------
# 5.4 Handling missing values
# ----------------------------------------------------------------------------
print(f"Missing CD4 count: {final_clin['cd4'].isna().sum()}")
final_clin_nomiss = final_clin.dropna(subset=["cd4"])
print(f"After dropping missing CD4: {len(final_clin_nomiss)}")

mean_cd4 = final_clin["cd4"].mean()
final_clin["cd4_imputed"] = final_clin["cd4"].fillna(mean_cd4)

final_clin.to_csv(os.path.join(DATA_PATH, "final_clin_processed.csv"), index=False)
