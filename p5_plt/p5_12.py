""" p5_12.py """

import matplotlib.pyplot as plt

pt1_x = [0, 1, 2, 3, 4]
pt1_y = [10, 11, 12, 13, 14]

pt2_x = [0, 1, 2, 3, 4]
pt2_y = [20, 21, 22, 23, 24]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(pt1_x, pt1_y, 'go--', linewidth=3, markersize=12)
ax1.set_title("title 1")
ax1.set_xlabel("X1")
ax1.set_ylabel("Y1")

ax2.plot(pt2_x, pt2_y, 'b*--', linewidth=3, markersize=12)
ax2.set_title("title 2")
ax2.set_xlabel("X2")
ax2.set_ylabel("Y2")

plt.tight_layout()
# plt.show()
plt.savefig("p5_12.png")
