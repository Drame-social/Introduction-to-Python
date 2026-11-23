# =============================================================================
# Phase 10 — Reporting & Export
# Python equivalent of SAS Module 10 (PROC FREQ / MEANS, ODS, PROC EXPORT)
# Data: final_demo.csv and final_clin.csv, linked by patient id
# Libraries: pandas, openpyxl
# =============================================================================
import os
import pandas as pd

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))
demo_clin = final_demo.merge(final_clin, on="id", how="left")

# ----------------------------------------------------------------------------
# 10.1 Frequency tables — equivalent to PROC FREQ
# ----------------------------------------------------------------------------
print(f"N patients: {len(demo_clin)}\n")
for col in ["htype", "hlevel", "hepther"]:
    tbl = demo_clin[col].value_counts(dropna=False).to_frame("n")
    tbl["pct"] = (tbl["n"] / tbl["n"].sum() * 100).round(1)
    print(f"--- {col} ---\n{tbl}\n")

# ----------------------------------------------------------------------------
# 10.2 Descriptive statistics by group — equivalent to PROC MEANS CLASS hlevel
# ----------------------------------------------------------------------------
bleeds_by_level = (demo_clin.groupby("hlevel")["bleeds"]
                   .agg(n="count", mean="mean", sd="std", median="median",
                        min="min", max="max")
                   .round(1))
print("--- Bleeds by hlevel ---")
print(bleeds_by_level, "\n")

# ----------------------------------------------------------------------------
# 10.3 Cross-tabulation — equivalent to PROC FREQ TABLES htype*hlevel
# ----------------------------------------------------------------------------
xtab = pd.crosstab(demo_clin["htype"], demo_clin["hlevel"], margins=True)
xtab_pct = pd.crosstab(demo_clin["htype"], demo_clin["hlevel"],
                       normalize="index").mul(100).round(1)
print("--- htype by hlevel (counts) ---")
print(xtab, "\n")
print("--- htype by hlevel (row %) ---")
print(xtab_pct, "\n")

# ----------------------------------------------------------------------------
# 10.4 Multi-sheet Excel report — equivalent to ODS EXCEL / PROC EXPORT
# ----------------------------------------------------------------------------
summary_tbl = pd.DataFrame({
    "n_patients":     [len(demo_clin)],
    "n_hemophilia_a": [int((demo_clin["htype"] == "Hemophilia A").sum())],
    "n_hemophilia_b": [int((demo_clin["htype"] == "Hemophilia B").sum())],
    "mean_bleeds":    [round(demo_clin["bleeds"].mean(), 1)],
    "median_bleeds":  [demo_clin["bleeds"].median()],
})

xlsx_path = os.path.join(OUTPUTS_PATH, "clinical_cohort_report.xlsx")
with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
    summary_tbl.to_excel(writer, sheet_name="Summary", index=False)
    bleeds_by_level.to_excel(writer, sheet_name="Bleeds by level")
    xtab.to_excel(writer, sheet_name="Type by level")
print(f"Excel report saved to {xlsx_path}")

# ----------------------------------------------------------------------------
# 10.5 CSV export — equivalent to PROC EXPORT DBMS=CSV
# ----------------------------------------------------------------------------
demo_clin.to_csv(os.path.join(OUTPUTS_PATH, "demo_clin_final.csv"), index=False)
print("CSV saved to outputs/demo_clin_final.csv")
