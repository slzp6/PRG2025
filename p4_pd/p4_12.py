""" p4_12.py """

import pandas as pd

df = pd.read_csv('anscombe_errs.csv')

print(df.head())
print("---")
df1 = df.dropna()
print(df1.head())
