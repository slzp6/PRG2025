""" p5_24.py """

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 10, 1000)

fig, ax = plt.subplots()
ax.hist(x)
plt.savefig("p5_24.png")
# plt.show()
