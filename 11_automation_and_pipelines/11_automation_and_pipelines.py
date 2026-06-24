# =============================================================================
# Phase 11 — Automation & Pipelines
# Python equivalent of SAS Module 11 (Macros)
# Libraries: pandas, functools
# =============================================================================
import pandas as pd
import os

DATA_PATH = "./data"

# ----------------------------------------------------------------------------
# 11.1 Reusable function — equivalent to SAS %MACRO
# ----------------------------------------------------------------------------
def summarize_cohort(df, group_col, outcome_col):
    """Group-level summary: n, mean, sd, missing count."""
    return (df.groupby(group_col)[outcome_col]
              .agg(n="count",
                   mean=lambda x: round(x.mean(), 2),
                   sd=lambda x: round(x.std(), 2),
                   missing=lambda x: x.isna().sum())
              .reset_index())

final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))
final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
demo_clin  = final_demo.merge(final_clin, on="studyid", how="left")

print("--- CD4 by Sex ---")
print(summarize_cohort(demo_clin, "sex", "cd4"))

print("\n--- Viral Load by Sex ---")
print(summarize_cohort(demo_clin, "sex", "vl"))

# ----------------------------------------------------------------------------
# 11.2 Batch process multiple datasets — equivalent to SAS %DO loop
# ----------------------------------------------------------------------------
dataset_names = ["mod3lab", "mod4", "mod6", "mod9"]
dim_report = []
for name in dataset_names:
    df = pd.read_csv(os.path.join(DATA_PATH, f"{name}.csv"))
    dim_report.append({"dataset": name, "rows": len(df), "cols": len(df.columns)})

print("\n--- Dataset Inventory ---")
print(pd.DataFrame(dim_report).to_string(index=False))

# ----------------------------------------------------------------------------
# 11.3 Pipeline function — wrap a full analysis into one callable unit
# ----------------------------------------------------------------------------
def run_vl_pipeline(csv_name):
    df = pd.read_csv(os.path.join(DATA_PATH, csv_name))
    if "vl" not in df.columns:
        return None
    df = df.dropna(subset=["vl"])
    df["suppressed"] = df["vl"] < 200
    return {
        "dataset":  csv_name,
        "n":        len(df),
        "pct_supp": round(df["suppressed"].mean() * 100, 1)
    }

results = [run_vl_pipeline(f) for f in ["mod3lab.csv", "mod9.csv"]]
results = [r for r in results if r]

print("\n--- VL Suppression Pipeline ---")
print(pd.DataFrame(results).to_string(index=False))
