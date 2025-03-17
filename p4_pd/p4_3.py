""" p4_3.py """

import pandas as pd

a = [100, 200, 300]
ps = pd.Series(a, index=['a', 'b', 'c'])
print(ps)
print(ps['b'])
