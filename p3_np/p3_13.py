""" p3_13.py """

import numpy as np

print("---")
a = np.zeros((2, 3))
print(a)

print("---")
b = np.ones((3, 4))
print(b)

print("---")
c = np.full((2, 3), 8.0)
print(c)

print("---")
d = np.vstack((a, c))
print(d)
