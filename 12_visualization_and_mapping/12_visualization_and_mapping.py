# =============================================================================
# Phase 12 — Visualization & Mapping
# Python equivalent of SAS Module 12
# Libraries: pandas, matplotlib, seaborn, (optional: plotly, geopandas)
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

DATA_PATH    = "./data"
OUTPUTS_PATH = "./outputs"
os.makedirs(OUTPUTS_PATH, exist_ok=True)

sns.set_theme(style="whitegrid", font_scale=1.1)

final_demo = pd.read_csv(os.path.join(DATA_PATH, "final_demo.csv"))
final_clin = pd.read_csv(os.path.join(DATA_PATH, "final_clin.csv"))
aidsvu     = pd.read_csv(os.path.join(DATA_PATH, "aidsvu_2016_newdx_county.csv"))

demo_clin = final_demo.merge(final_clin, on="studyid", how="left")
demo_clin["suppressed"] = demo_clin["vl"] < 200
demo_clin["sex_label"]  = demo_clin["sex"].map({1: "Male", 2: "Female"})
demo_clin["age_group"]  = pd.cut(
    demo_clin["age"],
    bins   = [0, 24, 34, 44, 54, np.inf],
    labels = ["<25", "25-34", "35-44", "45-54", "55+"]
)

# ----------------------------------------------------------------------------
# 12.1 Stacked bar — VL suppression by sex
# ----------------------------------------------------------------------------
supp_sex = (demo_clin.dropna(subset=["sex_label", "suppressed"])
              .groupby(["sex_label", "suppressed"])
              .size().unstack(fill_value=0))
supp_sex_pct = supp_sex.div(supp_sex.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(6, 4))
supp_sex_pct.plot(kind="bar", stacked=True,
                  color=["#d9534f", "#5cb85c"], ax=ax)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.set_title("Viral Load Suppression by Sex")
ax.set_xlabel("Sex"); ax.set_ylabel("Proportion")
ax.legend(["Not Suppressed", "Suppressed"], loc="upper right")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "vl_suppression_by_sex.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.2 Histogram — CD4 count distribution
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))
cd4_data = demo_clin["cd4"].dropna()
ax.hist(cd4_data, bins=30, color="#337ab7", edgecolor="white")
ax.axvline(200, color="red", linestyle="--", linewidth=1.5)
ax.text(215, ax.get_ylim()[1] * 0.85, "CD4=200", color="red", fontsize=9)
ax.set_title("CD4 Count Distribution")
ax.set_xlabel("CD4 Count (cells/mm³)"); ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "cd4_distribution.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.3 Box plot — CD4 by age group
# ----------------------------------------------------------------------------
plot_data = demo_clin.dropna(subset=["cd4", "age_group"])
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=plot_data, x="age_group", y="cd4",
            palette="Blues", ax=ax)
ax.set_title("CD4 Count by Age Group")
ax.set_xlabel("Age Group"); ax.set_ylabel("CD4 Count (cells/mm³)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUTS_PATH, "cd4_by_age_group.png"), dpi=150)
plt.close()

# ----------------------------------------------------------------------------
# 12.4 County-level scatter map — AIDSVu new diagnoses (lat/lon proxy)
# ----------------------------------------------------------------------------
aidsvu.columns = aidsvu.columns.str.lower()
if "lat" in aidsvu.columns and "lon" in aidsvu.columns:
    fig, ax = plt.subplots(figsize=(9, 5))
    sc = ax.scatter(aidsvu["lon"], aidsvu["lat"],
                    c=aidsvu["rate"], cmap="magma_r",
                    s=20, alpha=0.7)
    plt.colorbar(sc, ax=ax, label="Rate per 100,000")
    ax.set_title("HIV New Diagnoses by County (2016)")
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUTS_PATH, "hiv_new_dx_county_map.png"), dpi=150)
    plt.close()
    print("Map saved.")
else:
    print("Note: lat/lon columns not found in aidsvu data — map skipped.")

print("All plots saved to outputs/")
