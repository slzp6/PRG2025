""" p5_5.py """

import matplotlib.pyplot as plt
import numpy as np

pt_x = np.array([0, 2, 4])
pt_y = np.array([10, 12, 14])

fig, ax = plt.subplots()
ax.plot(pt_x, pt_y)
# plt.show()
plt.savefig("p5_5.png")
