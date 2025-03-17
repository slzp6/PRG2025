""" p5_19.py """

import matplotlib.pyplot as plt
import numpy as np

pt1_x = np.random.rand(30)
pt1_y = np.random.rand(30)
pt2_x = np.random.rand(50)
pt2_y = np.random.rand(50)

fig, ax = plt.subplots()
ax.scatter(pt1_x, pt1_y, s=100, color="Blue", marker="o")
ax.scatter(pt2_x, pt2_y, s=80, color="Green", marker="*")
ax.set_title("title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.grid(True)
plt.savefig("p5_19.png")
# plt.show()
