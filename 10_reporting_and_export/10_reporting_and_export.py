# =============================================================================
# Phase 10 — Reporting & Export
# Python equivalent of SAS Module 10
# Libraries: pandas, openpyxl
# =============================================================================
import pandas as pd
import os

DATA_PATH    = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))

demo_clin = final_demo.merge(final_clin, on="studyid", how="left")
demo_clin["suppressed"] = (demo_clin["vl"] < 200)

# ----------------------------------------------------------------------------
# 10.1 Descriptive summary — equivalent to SAS PROC FREQ + PROC MEANS
# ----------------------------------------------------------------------------
print("--- Descriptive Summary ---")
print(f"N: {len(demo_clin)}\n")
print("Age:\n", demo_clin["age"].describe().round(2))
print("\nSex distribution (%):\n",
      demo_clin["sex"].value_counts(normalize=True).mul(100).round(1))
print("\nViral Load Suppression:\n",
      demo_clin["suppressed"].value_counts())

# ----------------------------------------------------------------------------
# 10.2 Cross-tabulation — equivalent to SAS PROC FREQ TABLES sex*suppressed
# ----------------------------------------------------------------------------
print("\n--- Suppression by Sex (cross-tab) ---")
print(pd.crosstab(demo_clin["sex"], demo_clin["suppressed"],
                  margins=True, normalize="index").round(3))

# ----------------------------------------------------------------------------
# 10.3 Export to multi-sheet Excel — equivalent to SAS ODS EXCEL
# ----------------------------------------------------------------------------
summary_tbl = pd.DataFrame({
    "N":              [len(demo_clin)],
    "Mean Age":       [round(demo_clin["age"].mean(), 1)],
    "Pct Suppressed": [round(demo_clin["suppressed"].mean() * 100, 1)]
})

with pd.ExcelWriter(
        os.path.join(OUTPUTS_PATH, "hiv_cohort_report.xlsx"),
        engine="openpyxl") as writer:
    final_demo.to_excel(writer, sheet_name="Demographics", index=False)
    final_clin.to_excel(writer, sheet_name="Clinical",     index=False)
    summary_tbl.to_excel(writer, sheet_name="Summary",     index=False)

print("\nExcel report saved to outputs/hiv_cohort_report.xlsx")

# ----------------------------------------------------------------------------
# 10.4 Export to CSV — equivalent to SAS PROC EXPORT DBMS=CSV
# ----------------------------------------------------------------------------
demo_clin.to_csv(os.path.join(OUTPUTS_PATH, "demo_clin_final.csv"), index=False)
print("CSV saved to outputs/demo_clin_final.csv")
