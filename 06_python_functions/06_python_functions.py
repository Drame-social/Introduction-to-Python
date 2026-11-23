# =============================================================================
# Phase 06 — Python Functions
# Python equivalent of SAS Module 7 (SAS Functions)
# Libraries: pandas, numpy
# =============================================================================
import os
import numpy as np
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

mock = pd.read_csv(os.path.join(DATA_PATH, "mock_data.csv"))
# Credentials-style field is not needed for any exercise
mock = mock.drop(columns=["password"])

# ----------------------------------------------------------------------------
# 6.1 Character functions — SAS COMPRESS, UPCASE, PROPCASE, SUBSTR, SCAN, INDEX
# ----------------------------------------------------------------------------
mock["phone_digits"]  = mock["phone_num"].str.replace(r"\D", "", regex=True)   # COMPRESS
mock["supervisor_uc"] = mock["supervisor"].str.upper()                          # UPCASE
mock["last_name"]     = mock["supervisor"].str.split().str[-1]                  # SCAN(x,-1)
mock["email_domain"]  = mock["email"].str.split("@").str[1]                     # SCAN(x,2,'@')
mock["area_code"]     = mock["phone_digits"].str[:3]                            # SUBSTR
mock["has_red"]       = mock["colors"].str.contains("red", na=False)            # INDEX > 0
mock["n_colors"]      = mock["colors"].str.split(",").str.len()                 # COUNTW
mock["zip5"]          = mock["zipcode"].astype("Int64").astype(str).str.zfill(5)  # PUT(z, z5.)
print(mock[["phone_num", "phone_digits", "supervisor", "last_name",
            "email_domain", "zip5"]].head(), "\n")

# ----------------------------------------------------------------------------
# 6.2 Numeric functions — SAS MEAN, SUM, N, ROUND, ABS, SQRT, INT
# ----------------------------------------------------------------------------
score_cols = [f"score{i}" for i in range(1, 6)]
mock["score_mean"] = mock[score_cols].mean(axis=1).round(2)    # MEAN(of score1-score5)
mock["score_sum"]  = mock[score_cols].sum(axis=1, min_count=1) # SUM(of ...)
mock["score_n"]    = mock[score_cols].notna().sum(axis=1)      # N(of ...)
mock["value_abs"]  = mock["value"].abs()                       # ABS
mock["value_int"]  = np.trunc(mock["value"])                   # INT
mock["value_sqrt"] = np.sqrt(mock["value_abs"]).round(3)       # SQRT
print(mock[["value", "value_abs", "value_int", "value_sqrt"]].head(), "\n")

# ----------------------------------------------------------------------------
# 6.3 Date functions — SAS YEAR, MONTH, INTCK
# ----------------------------------------------------------------------------
mock["date"]  = pd.to_datetime(mock["date"], errors="coerce")
mock["year"]  = mock["date"].dt.year
mock["month"] = mock["date"].dt.month
mock["days_to_2018"] = (pd.Timestamp("2018-01-01") - mock["date"]).dt.days

# ----------------------------------------------------------------------------
# 6.4 Summary statistics — equivalent to PROC MEANS
# ----------------------------------------------------------------------------
print("--- Mean score per record ---")
print(mock["score_mean"].describe().round(2), "\n")

# ----------------------------------------------------------------------------
# 6.5 User-defined function — reusable categorization
# ----------------------------------------------------------------------------
def score_band(x):
    if pd.isna(x):
        return np.nan
    if x < 4:
        return "Low"
    if x < 7:
        return "Medium"
    return "High"

mock["score_band"] = mock["score_mean"].apply(score_band)
print(mock["score_band"].value_counts(dropna=False), "\n")

mock.to_csv(os.path.join(OUTPUTS_PATH, "mock_data_functions.csv"), index=False)
print("Saved outputs/mock_data_functions.csv")
