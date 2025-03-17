""" p5_7.py """

import matplotlib.pyplot as plt

pt_x = [0, 1, 2, 3, 4]
pt_y = [10, 11, 12, 13, 14]

fig, ax = plt.subplots()
ax.plot(pt_x, pt_y, marker='o')
# plt.show()
plt.savefig("p5_7.png")
