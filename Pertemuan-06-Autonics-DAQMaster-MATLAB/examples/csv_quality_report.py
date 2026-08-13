import argparse
from pathlib import Path
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("csv", type=Path)
a = p.parse_args()
df = pd.read_csv(a.csv)
print("file:", a.csv)
print("rows:", len(df))
print("columns:", list(df.columns))
print("missing_by_column:")
print(df.isna().sum().to_string())
print("numeric_summary:")
print(df.describe(include="all").to_string())
