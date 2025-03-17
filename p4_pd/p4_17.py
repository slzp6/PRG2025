""" p4_17.py """

import pandas as pd

DF1 = pd.DataFrame({'a1':['a','b','c'],\
                    'a2':[10, 20, 30 ]}).set_index('a1')
DF2 = pd.DataFrame({'a1':['a','B','C'],\
                    'b2':[50, 60, 70 ]}).set_index('a1')

print("--- left")
print(DF1)
print("--- right")
print(DF2)

print("\n--- join")
df = DF1.join(DF2)
print(df)
