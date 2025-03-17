""" p7_8.py """

import matplotlib.pyplot as plt
import tensorflow as tf
import keras

print("tensorflow: ", tf.__version__)
print("keras: ", keras.__version__)

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
    'Sneaker', 'Bag', 'Ankle boot'
]

(train_images, train_labels), \
(test_images, test_labels) = \
keras.datasets.fashion_mnist.load_data()

plt.figure(figsize=(15, 15))
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    # plt.imshow(train_images[i], cmap='binary')
    plt.imshow(train_images[i], cmap='gray')
    plt.xlabel(class_names[train_labels[i]])
# plt.show()
plt.savefig("p7_8.png")
