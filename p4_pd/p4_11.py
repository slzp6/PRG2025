""" p4_11.py """

import pandas as pd

# Google colab
# df = pd.read_json('./sample_data/anscombe.json')

df = pd.read_json('anscombe.json')

df.loc[1, 'Y'] = None
df.loc[3, 'Y'] = None
df.loc[4, 'X'] = -999999
print(df.head())
print(df.info())

df.to_csv("anscombe_errs.csv", columns=['Series', 'X', 'Y'], index=False)
