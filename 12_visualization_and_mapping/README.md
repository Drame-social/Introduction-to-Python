# Phase 12 — Visualization & Mapping

## Topics Covered

Stacked proportional bar charts with matplotlib, histograms with reference lines, box plots by group with seaborn, saving figures with plt.savefig(), and a county-level scatter map using AIDSVu lat/lon data.

## Files

| File | Description |
|------|-------------|
| `12_visualization_and_mapping.py` | matplotlib/seaborn charts and county scatter map |

## Datasets Used

final_demo.csv, final_clin.csv, aidsvu_2016_newdx_county.csv

## Key Python Syntax

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot
sns.boxplot(data=df, x="age_group", y="cd4", palette="Blues")
plt.title("CD4 Count by Age Group")
plt.tight_layout()
plt.savefig("outputs/cd4_by_age.png", dpi=150)
plt.close()
```
