""" p3_4.py """

import numpy as np

a_2d = [[10, 20, 30, 40], [50, 60, 70, 80]]

nda_2d = np.array(a_2d)
print(nda_2d)
print(nda_2d[1, 2])

print('shape:', nda_2d.shape)
print('ndim:', nda_2d.ndim)
print('size:', nda_2d.size)
