""" p5_8.py """

import matplotlib.pyplot as plt

pt_x = [0, 1, 2, 3, 4]
pt_y = [10, 11, 12, 13, 14]

fig, ax = plt.subplots()
ax.plot(pt_x, pt_y, color='green', marker='o', \
         linestyle='dashed',linewidth=3, markersize=12)
# plt.show()
plt.savefig("p5_8.png")
