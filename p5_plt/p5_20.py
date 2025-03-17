""" p5_20.py """

import matplotlib.pyplot as plt
import numpy as np

pt_x = np.random.rand(300)
pt_y = np.random.rand(300)
pt_val = np.random.rand(300)

fig, ax = plt.subplots()
im = ax.scatter(pt_x, pt_y, c=pt_val, cmap='viridis')
plt.colorbar(im)
ax.set_title("title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.grid(True)
plt.savefig("p5_20.png")
# plt.show()
