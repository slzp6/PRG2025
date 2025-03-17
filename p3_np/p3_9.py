""" p3_9.py """

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 5], [6, 7]])
c = np.concatenate((a, b), axis=0)
print(c)
print(c.shape)

print("---")
a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 5], [6, 7]])
d = np.concatenate((a, b), axis=1)
print(d)
print(d.shape)
