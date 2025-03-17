""" p5_15.py """

import matplotlib.pyplot as plt

pt_x = [0, 1, 2, 3, 4]
pt1_y = [10, 11, 12, 13, 14]
pt2_y = [20, 21, 22, 23, 24]

fig, axs = plt.subplots(3, 3)
axs[0, 0].set_facecolor("lightgreen")
axs[0, 0].plot(pt_x, pt1_y, 'ro--', linewidth=1, markersize=3)
axs[2, 2].set_facecolor("lightskyblue")
axs[2, 2].plot(pt_x, pt2_y, 'b*--', linewidth=1, markersize=10)

plt.tight_layout()
plt.savefig("p5_15.png")
# plt.show()
