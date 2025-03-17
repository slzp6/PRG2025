""" p3_15.py """

import random
import numpy as np

N = 40
rnbs_std = [random.randint(0, 1) for i in range(N)]
print("std", rnbs_std)

rnbs_np = [np.random.randint(0, 1) for i in range(N)]
print("np", rnbs_np)
