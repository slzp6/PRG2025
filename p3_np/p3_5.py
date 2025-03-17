""" p3_5.py """

import numpy as np

a_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

nda_3d = np.array(a_3d)
print(nda_3d)
print(nda_3d[0, 1, 2])

print('shape:', nda_3d.shape)
print('ndim:', nda_3d.ndim)
print('size:', nda_3d.size)
