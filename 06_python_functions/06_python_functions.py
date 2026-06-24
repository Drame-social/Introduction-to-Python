# =============================================================================
# Phase 06 — Python Functions
# Python equivalent of SAS Module 7 (SAS Functions)
# Libraries: pandas, numpy
# =============================================================================
import pandas as pd
import numpy as np
import os

DATA_PATH = "./data"

patients = pd.read_csv(os.path.join(DATA_PATH, "patients.csv"))

# ----------------------------------------------------------------------------
# 6.1 String functions — equivalent to SAS UPCASE, SUBSTR, INDEX, TRIM
# ----------------------------------------------------------------------------
patients["name_upper"]   = patients["name"].str.upper()
patients["name_lower"]   = patients["name"].str.lower()
patients["first3"]       = patients["name"].str[:3]
patients["name_trimmed"] = patients["name"].str.strip()
patients["has_dr"]       = patients["name"].str.match(r"^Dr\.", na=False)

# ----------------------------------------------------------------------------
# 6.2 Numeric functions — equivalent to SAS ROUND, ABS, SQRT, INT
# ----------------------------------------------------------------------------
patients["age_rounded"] = patients["age"].round(0)
patients["age_sqrt"]    = np.sqrt(patients["age"])
patients["age_floor"]   = np.floor(patients["age"])
patients["age_dist40"]  = (patients["age"] - 40).abs()

# ----------------------------------------------------------------------------
# 6.3 Statistical summary — equivalent to SAS PROC MEANS
# ----------------------------------------------------------------------------
print("--- Age Summary ---")
print(patients["age"].describe().round(2))

# ----------------------------------------------------------------------------
# 6.4 Custom function — equivalent to SAS macro or user-defined format
# ----------------------------------------------------------------------------
def bmi_category(bmi):
    if pd.isna(bmi):   return np.nan
    elif bmi < 18.5:   return "Underweight"
    elif bmi < 25.0:   return "Normal"
    elif bmi < 30.0:   return "Overweight"
    else:              return "Obese"

patients["bmi_cat"] = patients["bmi"].apply(bmi_category)

print("\n--- BMI Category Distribution ---")
print(patients["bmi_cat"].value_counts())

patients.to_csv(os.path.join(DATA_PATH, "patients_functions.csv"), index=False)
