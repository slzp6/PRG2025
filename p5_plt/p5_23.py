""" p5_23.py """

import matplotlib.pyplot as plt
import numpy as np

l = np.array(["a", "b", "c", "d", "e"])
v = np.array([8, 4, 3, 2, 2])

fig, ax = plt.subplots()
ax.bar(l, v, color="Green", width=0.5)
# plt.show()
plt.savefig("p5_23.png")
