""" p3_7.py """

import numpy as np

nda_a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(nda_a)
print(nda_a.shape)

print("---")
nda_b = nda_a.reshape(3, 4)
print(nda_b)
print(nda_b.shape)

print("---")
nda_c = nda_a.reshape(2, -1)
print(nda_c)
print(nda_c.shape)
