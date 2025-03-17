""" p4_10.py """

import pandas as pd

# Google colab
# df = pd.read_json('./sample_data/anscombe.json')

df = pd.read_json('anscombe.json')

print(df.info())
df.to_csv("anscombe.csv", columns=['Series', 'X', 'Y'], index=False)
