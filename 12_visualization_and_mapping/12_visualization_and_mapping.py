# =============================================================================
# Phase 12 — Visualization & Mapping
# Python equivalent of SAS Module 12 (SGPLOT and county-level HIV data)
# Libraries: pandas, matplotlib, seaborn
# =============================================================================
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_PATH = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)
sns.set_theme(style="whitegrid", font_scale=1.0)

final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))
aidsvu = pd.read_csv(os.path.join(DATA_PATH, "aidsvu_2016_newdx_county.csv"))
demo_clin = final_demo.merge(final_clin, on="id", how="left")
level_order = ["Mild", "Moderate", "Severe"]

# ----------------------------------------------------------------------------
# 12.1 Grouped bar chart — hlevel by htype (SGPLOT VBAR / GROUP=)
# ----------------------------------------------------------------------------
counts = pd.crosstab(demo_clin["hlevel"], demo_clin["htype"]).reindex(level_order)
ax = counts.plot(kind="bar", figsize=(6, 4), rot=0)
ax.set_title("Patients by hlevel and htype")
ax.set_xlabel("hlevel"); ax.set_ylabel("Patients")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "hlevel_by_htype.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.2 Histogram — bleeds (SGPLOT HISTOGRAM)
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(demo_clin["bleeds"].dropna(), bins=30, edgecolor="white")
ax.set_title("Distribution of bleeds")
ax.set_xlabel("Bleeds"); ax.set_ylabel("Patients")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "bleeds_histogram.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.3 Box plot — bleeds by hlevel (SGPLOT VBOX / CATEGORY=)
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(data=demo_clin.dropna(subset=["hlevel", "bleeds"]),
            x="hlevel", y="bleeds", order=level_order, ax=ax)
ax.set_title("Bleeds by hlevel")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "bleeds_by_hlevel.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.4 County-level HIV new diagnoses, Georgia 2016 (AIDSVu)
#      Negative values are suppression codes, not rates, so they are set to
#      missing before plotting. The file has no county boundaries, so this
#      section ranks counties instead of drawing a choropleth map.
# ----------------------------------------------------------------------------
aidsvu = aidsvu.dropna(subset=["county_name"]).copy()   # drop the blank last row
for col in ["newdx_rate", "newdx_cases"]:
    aidsvu.loc[aidsvu[col] < 0, col] = pd.NA
reported = aidsvu.dropna(subset=["newdx_rate"])
print(f"Counties: {len(aidsvu)}; with a reported rate: {len(reported)}; "
      f"suppressed: {len(aidsvu) - len(reported)}")

top = reported.nlargest(15, "newdx_rate").sort_values("newdx_rate")
fig, ax = plt.subplots(figsize=(7, 6))
ax.barh(top["county_name"], top["newdx_rate"])
ax.set_title("Highest reported HIV new-diagnosis rates\nGeorgia counties, 2016")
ax.set_xlabel("Rate per 100,000 (as reported)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "ga_county_newdx_top15.png"), dpi=150)
plt.close()

print("Plots saved to outputs/")
