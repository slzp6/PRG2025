""" p5_16.py """

import matplotlib.pyplot as plt

pt_x = [8, 4, 3, 2, 1]
pt_y = [4, 3, 5, 7, 9]

fig, ax = plt.subplots()
ax.scatter(pt_x, pt_y)
ax.set_title("title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
# plt.show()
plt.savefig("p5_16.png")
