""" p5_14.py """

import matplotlib.pyplot as plt

pt_x = [0, 1, 2, 3, 4]
pt1_y = [10, 11, 12, 13, 14]
pt2_y = [20, 21, 22, 23, 24]
pt3_y = [30, 31, 32, 33, 34]
pt4_y = [40, 41, 42, 43, 44]
pt5_y = [50, 51, 52, 53, 54]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(pt_x, pt1_y, 'ro--', linewidth=3, markersize=12)
ax1.set_title("title 1")

ax2.plot(pt_x, pt2_y, 'g*--', linewidth=3, markersize=12)
ax2.set_title("title 2")

ax3.plot(pt_x, pt3_y, 'bo--', linewidth=3, markersize=12)
ax3.set_title("title 3")

ax4.plot(pt_x, pt4_y, 'c*--', linewidth=3, markersize=12)
ax4.set_title("title 4")

plt.tight_layout()
# plt.show()
plt.savefig("p5_14.png")
