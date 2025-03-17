""" p3_17.py """

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
rnbs = rng.normal(size=100000, scale=1)

print(rnbs.mean())
print(rnbs.std())

plt.hist(rnbs, bins=100)
# plt.show()
plt.savefig("p3_17.png")
