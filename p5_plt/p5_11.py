""" p5_11.py """

import matplotlib.pyplot as plt

pt_x = [0, 1, 2, 3, 4]
pt_y = [10, 11, 12, 13, 14]

fig, ax = plt.subplots()
ax.plot(pt_x, pt_y, 'go--', linewidth=3, markersize=12)
ax.set_title("title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
# plt.show()
plt.savefig("p5_11.png")
