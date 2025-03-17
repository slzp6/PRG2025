""" p4_19.py """

import pandas as pd

df = pd.read_csv('anscombe_dup.csv')

print(df.head())
print("---")
print(df.duplicated())
