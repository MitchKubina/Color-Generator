import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Reshape
from keras.utils import to_categorical

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

color = pd.read_csv("colors.csv")
names = color["name"]
maxlen = 25
num_classes = 28

t = Tokenizer(char_level = True)
t.fit_on_texts(names)

def load_model():
    model = Sequential()
    model.add(LSTM(256, return_sequences=True, input_shape=(maxlen, num_classes)))
    model.add(LSTM(128))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(3, activation='sigmoid'))
    model.compile(optimizer='adam', loss='mse', metrics=['acc'])
    
    model.load_weights('model_1.weights.h5')
    return model

def scale(num):
    return int(num * 255)

def predict_color(model, name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    print(tokenized)
    padded =  preprocessing.sequence.pad_sequences(tokenized, maxlen = maxlen)
    one_hot = to_categorical(padded, num_classes=28)

    output = model.predict(np.array(one_hot))[0]
    r,g,b = scale(output[0]), scale(output[1]), scale(output[2])
    print(f"Predicted RGB value: R:{r} G:{g} B:{b}")

    return r,g,b