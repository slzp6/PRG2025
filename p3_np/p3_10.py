""" p3_10.py """

import numpy as np

a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
b = np.array_split(a, 3)
print(b[0])
print(b[1])
print(b[2])
