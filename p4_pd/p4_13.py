""" p4_13.py """

import pandas as pd

df = pd.read_csv('anscombe_errs.csv')

print(df.head())
print("---")

ym = df['Y'].mean()
val = {'Y': ym}
df1 = df.fillna(value=val)
print(df1.head())
