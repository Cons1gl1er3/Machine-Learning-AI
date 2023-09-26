import tensorflow as tf
from tensorflow import keras
from keras import layers

shape = 1
model = keras.Sequential([
    layers.Dense(units = 1, input_shape = [shape])
])
w, b = model.weights

X = tf.linspace(1, 3, 10000)
y =  model.predict(X)

import matplotlib.pyplot as plt
plt.plot(X, y, 'ro')
plt.show()