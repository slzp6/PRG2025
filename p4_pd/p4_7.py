""" p4_7.py """

import pandas as pd

fruits = {
    'name': ["apple", "banana", "cranberry", "durian", "elderberry"],
    'quantity': [10, 20, 30, 40, 50],
    'weight': [10.0, 20.0, 30.0, 40.0, 50.0]
}
idx = ["r0", "r1", "r2", "r3", "r4"]

df = pd.DataFrame(fruits, index=idx)
print(df)

print("--- loc")
print(df.loc["r0":"r2", ["name", "weight"]])

print("--- iloc")
print(df.iloc[0:2, [0, 2]])
