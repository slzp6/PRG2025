""" p4_6.py """

import pandas as pd

fruits = {
    'name': ["apple", "banana", "cranberry", "durian", "elderberry"],
    'quantity': [10, 20, 30, 40, 50],
    'weight': [10.0, 20.0, 30.0, 40.0, 50.0]
}
idx = ["r0", "r1", "r2", "r3", "r4"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("---")
print(df.loc["r1", "weight"])

print("---")
print(df.iloc[2, 0])
