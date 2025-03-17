""" p7_11.py """

# pylint: disable=pointless-string-statement

import imageio
import keras
import numpy as np
from scipy import datasets
import tensorflow as tf

print("tensorflow:", tf.__version__)
print("keras:", keras.__version__)

img = datasets.face()
print(img.shape)
imageio.v3.imwrite("face.png", img)

# for keras 2.0
'''
model = tf.keras.applications.resnet50.ResNet50(weights="imagenet")
IMG = "face.png"
img = tf.keras.utils.load_img(IMG, target_size=(224, 224))
x = tf.keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = tf.keras.applications.resnet50.preprocess_input(x)
preds = model.predict(x)
print('predicted:')
print(f"{tf.keras.applications.resnet50.decode_predictions(preds, top=5)[0]}")
'''

# for keras 3.0
model = keras.applications.resnet50.ResNet50(weights="imagenet")
IMG = "face.png"
img = keras.utils.load_img(IMG, target_size=(224, 224))
x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = keras.applications.resnet50.preprocess_input(x)
preds = model.predict(x)
print('predicted:')
print(f"{keras.applications.resnet50.decode_predictions(preds, top=5)[0]}")
