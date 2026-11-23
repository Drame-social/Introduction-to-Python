# Phase 12 — Visualization & Mapping

## Topics Covered

Grouped bar charts, histograms, and box plots with matplotlib and seaborn, and county-level HIV new-diagnosis rates for Georgia (AIDSVu, 2016). Negative values in the AIDSVu file are suppression codes and are set to missing. The file has no county boundaries, so counties are ranked in a bar chart rather than mapped.

## Files

| File | Description |
|------|-------------|
| `12_visualization_and_mapping.py` | matplotlib/seaborn charts and county ranking |

## Datasets Used

final_demo.csv, final_clin.csv, aidsvu_2016_newdx_county.csv

Derived files are written to `./outputs/`.

## Key Python Syntax

```python
sns.boxplot(data=demo_clin, x="hlevel", y="bleeds", order=["Mild", "Moderate", "Severe"])

aidsvu.loc[aidsvu["newdx_rate"] < 0, "newdx_rate"] = pd.NA   # suppression codes
top = aidsvu.dropna(subset=["newdx_rate"]).nlargest(15, "newdx_rate")
```
