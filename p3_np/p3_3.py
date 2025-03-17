""" p3_3.py """

import numpy as np

a = [10, 20, 30, 40, 50]
nda_i = np.array(a, dtype='int8')
print(type(nda_i))
print(nda_i.dtype)
print(nda_i)

print('---')
nda_f = np.array(a, dtype='float64')
print(type(nda_f))
print(nda_f.dtype)
print(nda_f)
