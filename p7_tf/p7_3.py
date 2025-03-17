""" p7_3.py """

# conda install tensorflow
#   wsl2 "Ubuntu 22.04.5 LTS"
#   tensorflow: 2.17.0
#   keras: 3.5.0

import tensorflow as tf
import keras

print(tf.__version__)

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = keras.models.Sequential([
    keras.layers.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

print(model.summary())
keras.utils.plot_model(model,
                       to_file='p7_3_pm.png',
                       show_shapes=True,
                       show_layer_names=False)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
