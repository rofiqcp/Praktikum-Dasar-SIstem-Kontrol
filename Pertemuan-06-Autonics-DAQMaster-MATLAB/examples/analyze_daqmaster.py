import sys
from pathlib import Path
import pandas as pd

if len(sys.argv) != 2:
    raise SystemExit('usage: python script.py file.csv')
p = Path(sys.argv[1])
df = pd.read_csv(p)
print('rows:', len(df))
print('columns:', list(df.columns))
print(df.describe(include='all').to_string())
