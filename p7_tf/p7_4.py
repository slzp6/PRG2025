""" p7_4.py """

# conda install tensorflow
#   wsl2 "Ubuntu 22.04.5 LTS"
#   tensorflow: 2.17.0
#   keras: 3.5.0

import pprint
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import keras
from keras import datasets, layers, models, utils

print("tensorflow: ", tf.__version__)
print("keras: ", keras.__version__)

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

print('x_train: ', x_train.shape)
print('y_train: ', y_train.shape)
print('x_test:  ', x_test.shape)
print('y_test:  ', y_test.shape)

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

print('x_train: ', x_train.shape)
print('x_test:  ', x_test.shape)

print('x_train')
print('min:  ', x_train.min())
print('max:  ', x_train.max())
print('x_test')
print('min:  ', x_test.min())
print('max:  ', x_test.max())

x_train = x_train / 255.0
x_test = x_test / 255.0

print('x_train')
print('min:  ', x_train.min())
print('max:  ', x_train.max())
print('x_test')
print('min:  ', x_test.min())
print('max:  ', x_test.max())

fig, ax = plt.subplots()
img = ax.imshow(x_train[0].reshape(28, 28), cmap='gray')
fig.colorbar(img)
# plt.show()
plt.savefig("p7_4_timg.png")

W = 8
H = 4
FC = 10
FR = 4
fig = plt.figure(figsize=(W, H))
for i in range(0, FC * FR):
    img = x_train[i].reshape(28, 28)
    fig.add_subplot(FR, FC, i + 1)
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(y_train[i])
    plt.tight_layout()
# plt.show()
plt.savefig("p7_4_timgs.png")

model = models.Sequential()
model.add(layers.Input(shape=(28, 28, 1)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

print(model.summary())

utils.plot_model(model,
                 to_file='p7_4_pm.png',
                 show_shapes=True,
                 show_layer_names=False)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=1)
print('test_loss: ', test_loss)
print('test_acc:  ', test_acc)

EP = 10
history = model.fit(x_train,
                    y_train,
                    batch_size=480,
                    epochs=EP,
                    validation_split=0.2)

print(history.history.keys())
pprint.pprint(history.history)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('test_loss: ', test_loss)
print('test_acc:  ', test_acc)

N = 1
fig, ax = plt.subplots()
img = ax.imshow(x_test[N].reshape(28, 28), cmap='gray')
fig.colorbar(img)
# plt.show()
plt.savefig("p7_4_timg_bar")

pred = model.predict(x_test[N:N + 1])
print('pred:', pred)
print('pred_argmax:', pred.argmax(axis=1))
print('y_test:', y_test[N])

model.save('p7_4_model.keras')

reconstructed_model = models.load_model('p7_4_model.keras')
np.testing.assert_allclose(model.predict(x_train),
                           reconstructed_model.predict(x_train))

test_loss, test_acc = reconstructed_model.evaluate(x_test, y_test, verbose=1)
print('test_loss: ', test_loss)
print('test_acc:  ', test_acc)
