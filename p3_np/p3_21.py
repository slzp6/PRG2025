""" p3_21.py """

#
# conda install pooch
#

import imageio
import matplotlib.pyplot as plt
from scipy import datasets
from scipy import ndimage

fig = plt.figure()
plt.gray()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

img = datasets.ascent().astype("int32")
# img = imageio.v3.imread("test.png")

img_gaussian = ndimage.gaussian_filter(img, sigma=6)
img_sobel_h = ndimage.sobel(img, 0)  # horizontal
img_sobel_v = ndimage.sobel(img, 1)  # vertical

imageio.v3.imwrite("test.png", img)
imageio.v3.imwrite("test_gaussian.png", img_gaussian)
imageio.v3.imwrite("test_sobel_h.png", img_sobel_h)
imageio.v3.imwrite("test_sobel_v.png", img_sobel_v)

ax1.imshow(img)
ax2.imshow(img_gaussian)
ax3.imshow(img_sobel_h)
ax4.imshow(img_sobel_v)
# plt.show()
plt.savefig("p3_21.png")
