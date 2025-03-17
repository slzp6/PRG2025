""" p4_16.py """

import pandas as pd

df1 = pd.DataFrame({'a1':['a','b','c'],\
                    'a2':[10, 20, 30 ]})
df2 = pd.DataFrame({'a1':['a','B','C'],\
                    'b2':[50, 60, 70 ]})

print("- df1 -")
print(df1)

print("- df2 -")
print(df2)

print("\n-- left")
dfl = df1.merge(df2, how='left')
print(dfl)

print("\n--- right")
dfr = df1.merge(df2, how='right')
print(dfr)

print("\n--- inner")
dfi = df1.merge(df2, how='inner')
print(dfi)

print("\n--- outer")
dfo = df1.merge(df2, how='outer')
print(dfo)

print("\n--- cross")
dfc = df1.merge(df2, how='cross')
print(dfc)
