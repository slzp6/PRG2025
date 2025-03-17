""" p7_9.py """

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import keras
from keras import layers, models, utils

print(f"tf: {tf.__version__}")
print(f"keras: {keras.__version__}")

(train_images, train_labels), \
(test_images, test_labels) = \
keras.datasets.fashion_mnist.load_data()

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
    'Sneaker', 'Bag', 'Ankle boot'
]

train_images = train_images / 255.0
test_images = test_images / 255.0

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

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

utils.plot_model(model,
                 to_file='p7_9_pm.png',
                 show_shapes=True,
                 show_layer_names=False)

BS = 480
EP = 10

history = model.fit(train_images,
                    train_labels,
                    batch_size=BS,
                    epochs=EP,
                    validation_split=0.2)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)
print('\nTest accuracy:', test_acc)

N = 0
predictions = model.predict(test_images)
print(predictions[N])
print(f"test_image id: {N}")
index_pred = np.argmax(predictions[N])
index_true = test_labels[N]
print(f"PRED class:{index_pred} -> {class_names[index_pred]}")
print(f"TRUE class:{index_true} -> {class_names[index_true]}")

fig, ax = plt.subplots()
ax.plot(range(1, EP + 1), history.history['accuracy'], "-o")
ax.plot(range(1, EP + 1), history.history['val_accuracy'], "-o")
ax.set_title('fashion_mnist')
ax.set_ylabel('accuracy')
ax.set_xlabel('epochs')
ax.set_xlim(0, EP + 1)
ax.set_ylim(0.5, 1.01)
ax.grid()
ax.legend(['accuracy', 'val_accuracy'])
# plt.show()
plt.savefig("p7_9.png")
