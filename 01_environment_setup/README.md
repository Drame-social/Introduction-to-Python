# Phase 01 — Environment Setup

## Topics Covered

Installing Python and pip, creating virtual environments with venv, installing packages (pandas, numpy, matplotlib, seaborn, openpyxl), using Jupyter notebooks or a script editor, and setting working paths.

## Files

| File | Description |
|------|-------------|
| `README.md` | This file |

## Datasets Used

None

## Key Python Syntax

```python
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install required packages
pip install pandas numpy matplotlib seaborn openpyxl

# Verify
import pandas as pd
print(pd.__version__)
```
