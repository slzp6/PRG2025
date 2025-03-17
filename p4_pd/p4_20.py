""" p4_20.py """

import pandas as pd

df = pd.read_csv('anscombe_dup.csv')

print(df.info())
print("---")
df2 = df.drop_duplicates()
print(df2.info())
print(df2.duplicated())
