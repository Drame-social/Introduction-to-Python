# =============================================================================
# Phase 11 — Automation & Pipelines
# Python equivalent of SAS Module 11 (Macros)
# Libraries: pandas
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

# ----------------------------------------------------------------------------
# 11.1 Reusable function — equivalent to a parameterized SAS %MACRO
# ----------------------------------------------------------------------------
def summarize_by(df, group_col, outcome_col):
    """Group-level n, mean, SD, and missing count for one numeric outcome."""
    g = df.groupby(group_col, dropna=False)[outcome_col]
    return pd.DataFrame({
        "n":       g.count(),
        "mean":    g.mean().round(2),
        "sd":      g.std().round(2),
        "missing": g.apply(lambda x: int(x.isna().sum())),
    }).reset_index()


final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))
demo_clin = final_demo.merge(final_clin, on="id", how="left")

# Call the "macro" with different parameters
for group_col, outcome_col in [("hlevel", "bleeds"),
                               ("htype", "bleeds"),
                               ("htype", "weightkg")]:
    print(f"--- {outcome_col} by {group_col} ---")
    print(summarize_by(demo_clin, group_col, outcome_col).to_string(index=False), "\n")

# ----------------------------------------------------------------------------
# 11.2 Loop over datasets — equivalent to a SAS %DO loop
# ----------------------------------------------------------------------------
inventory = []
for name in ["mod3lab", "mod4", "mod6", "mod9", "patients", "final_clin"]:
    df = pd.read_csv(os.path.join(DATA_PATH, f"{name}.csv"))
    inventory.append({
        "dataset":      name,
        "rows":         len(df),
        "cols":         df.shape[1],
        "pct_missing":  round(df.isna().mean().mean() * 100, 2),
    })
inventory = pd.DataFrame(inventory)
print("--- Dataset inventory ---")
print(inventory.to_string(index=False), "\n")

# ----------------------------------------------------------------------------
# 11.3 Pipeline — one function that reads, cleans, summarizes, and saves
# ----------------------------------------------------------------------------
def run_screening_pipeline(csv_name, out_name):
    df = pd.read_csv(os.path.join(DATA_PATH, csv_name))
    df["Vdatesub"] = pd.to_datetime(df["Vdatesub"], errors="coerce")
    df["month"] = df["Vdatesub"].dt.to_period("M").astype(str)
    summary = (df.groupby(["SITE", "month"])
                 .agg(screened=("id", "count"),
                      complete=("Vstatus", lambda s: int((s == "Complete").sum())),
                      eligible=("elig", lambda s: int((s == 1).sum())),
                      elig_missing=("elig", lambda s: int(s.isna().sum())))
                 .reset_index())
    summary.to_csv(os.path.join(OUTPUTS_PATH, out_name), index=False)
    return summary

screening = run_screening_pipeline("screener_data.csv", "screening_by_site_month.csv")
print("--- Screening by site and month ---")
print(screening.to_string(index=False))
inventory.to_csv(os.path.join(OUTPUTS_PATH, "dataset_inventory.csv"), index=False)
print("\nSaved outputs/screening_by_site_month.csv and outputs/dataset_inventory.csv")
