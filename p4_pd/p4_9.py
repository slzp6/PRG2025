""" p4_9.py """

import pandas as pd

# df = pd.read_json('./sample_data/anscombe.json')
df = pd.read_json('anscombe.json')
print(df.info())
print(df.head())
