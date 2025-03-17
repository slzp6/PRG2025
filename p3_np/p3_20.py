""" p3_20.py """

#
# conda install pooch
#

from scipy import datasets
import matplotlib.pyplot as plt

fig = plt.figure()
plt.gray()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ascent = datasets.ascent()
face = datasets.face()
ax1.imshow(ascent)
ax2.imshow(face)
# plt.show()
plt.savefig("p3_20.png")
