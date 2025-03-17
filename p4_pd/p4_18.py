""" p4_18.py """

import pandas as pd

# df = pd.read_json('./sample_data/anscombe.json')
df = pd.read_json('anscombe.json')

df1 = df[df['Series'] == 'I']
df2 = df[df['Series'] == 'II']
df3 = pd.concat([df1, df2, df1])

print(df1.head())
print(df2.head())
print(df3.head())

print(df3.info())
df3.to_csv("anscombe_dup.csv", columns=['Series', 'X', 'Y'], index=False)
