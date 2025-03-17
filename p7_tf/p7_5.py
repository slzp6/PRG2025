""" p7_5.py """

import matplotlib.pyplot as plt
import tensorflow as tf
import keras

print("tensorflow: ", tf.__version__)
print("keras: ", keras.__version__)

(train_images, train_labels), \
(test_images, test_labels) = \
keras.datasets.fashion_mnist.load_data()

print('train_image.shape: ', train_images.shape)
print('len(train_labels): ', len(train_labels))
print('train_labels: ', train_labels)
print('---')
print('test_images.shape: ', test_images.shape)
print('len(test_labels): ', len(test_labels))
print('test_labels: ', test_labels)

print('---')
N = 100
print('item_id: ', N)

plt.figure()
plt.imshow(train_images[N], cmap='gray')
plt.colorbar()
plt.grid(False)
# plt.show()
plt.savefig("p7_5.png")
