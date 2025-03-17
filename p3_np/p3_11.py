""" p3_11.py """

import numpy as np

a = np.array([8, 4, 3, 2, 1])
print(a)

even_odd = np.where(a % 2 == 0, "even", "odd")
print(even_odd)
