""" p4_15.py """

import pandas as pd

df1 = pd.DataFrame({'a1':['a','b','c'],\
                    'a2':[10, 20, 30 ]})
df2 = pd.DataFrame({'a1':['a','B','C'],\
                    'b2':[50, 60, 70 ]})

print("--- left")
print(df1)
print("--- right")
print(df2)

print("\n--- concat  axis=0")
df = pd.concat([df1, df2], axis=0)
print(df)

print("\n--- concat  axis=1")
df = pd.concat([df1, df2], axis=1)
print(df)
