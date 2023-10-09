#import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

data = pd.read_csv(r"D:\Coding\Mini Project\train.csv", index_col=0)
X = data.copy()
y = X.pop('SalePrice')

impute = SimpleImputer(strategy="most_frequent")
X = impute.fit_transform(X)
X = pd.DataFrame(X)

preprocessor = make_column_transformer(
    (StandardScaler(),
     make_column_selector(dtype_include=np.number)),
    (OneHotEncoder(sparse_output=False),
     make_column_selector(dtype_include=object)),
)

X = preprocessor.fit_transform(X)
y = np.log(y)
input_shape = [X.shape[1]]

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=input_shape),
    layers.Dense(128, activation='relu'),    
    layers.Dense(64, activation='relu'),
    layers.Dense(1),
])

model.compile(
    optimizer='adam',
    loss = 'mae'
)


history = model.fit(X, y,
          batch_size=100,
          epochs=100)

history_df = pd.DataFrame(history.history)
# Start the plot at epoch 5. You can change this to get a different view.
history_df.loc[5:, ['loss']].plot()
plt.show()
