""" p4_14.py """

import pandas as pd

print("--- org")
df = pd.read_csv('anscombe_errs.csv')
print(df.head())

print("\n--- query")
low_vals = df.query('X < 0')
print(low_vals)

print("\n--- mask")
df['X'] = df['X'].mask(df['X'] < 0, 1)
print(df.head())
