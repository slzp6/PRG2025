""" p4_8.py """

import pandas as pd

# df = pd.read_csv('./sample_data/california_housing_train.csv')
df = pd.read_csv('california_housing_train.csv')

print("--- head ")
print(df.head(3))
print("--- tail")
print(df.tail(3))
