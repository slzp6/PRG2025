""" p7_6.py """

import tensorflow as tf
import keras

print("tensorflow: ", tf.__version__)
print("keras: ", keras.__version__)

(train_images, train_labels), \
(test_images, test_labels) = \
keras.datasets.fashion_mnist.load_data()

N = 100
img = train_images[N]
print(img.shape)
print(type(img))
for i in range(28):
    row = img[i].tolist()
    for j in row:
        print(f"{j:3}", end=" ")
    print("")
