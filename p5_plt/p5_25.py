""" p5_25.py """

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 10, 1000)

fig, ax = plt.subplots()
ax.hist(x)
# plt.show()
plt.savefig("p5_25.png")
fig.savefig("test_1.png", dpi=300)
fig.savefig("test_1.pdf", dpi=600)

print("---")
print(plt.gcf().canvas.get_supported_filetypes())
