# Phase 03 — Data Merging & Subsetting

## Topics Covered

Filtering rows with boolean indexing, selecting columns by name, left/inner/anti-joins using merge() with indicator=True, and sorting with sort_values().

## Files

| File | Description |
|------|-------------|
| `03_data_merging_and_subsetting.py` | Merge, filter, and sort datasets |

## Datasets Used

mod3lab.csv, final_demo.csv, final_clin.csv

## Key Python Syntax

```python
# Filter rows
hiv_pos = mod3lab[mod3lab["hivstatus"] == 1]

# Anti-join — unmatched records
merged = final_demo.merge(final_clin[["studyid"]], on="studyid",
                          how="left", indicator=True)
unmatched = merged[merged["_merge"] == "left_only"]

# Sort
sorted_df = mod3lab.sort_values(["studyid", "visitdate"],
                                 ascending=[True, False])
```
