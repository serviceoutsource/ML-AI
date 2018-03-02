from sklearn.metrics import mean_squared_error
import numpy as np
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout
from keras.layers.recurrent import LSTM


class Lstm_model(object):
    def __init__(self, model):
        self.model = model

    def build_model(self):
        model = Sequential()
        # first layers
        model.add(LSTM(units=256,
                       input_shape=(),
                       activation='tanh'))
        model.add(Dropout(0.2))

        # second layers
        model.add(Dense(units=128,
                        activation='relu'))
        model.add(Dropout(0.2))

        # third layers
        model.add(Dense(units=1,
                        activation='relu'))

        model.summary()
        model.compile(loss='mse',
                      optimizer='adam',
                      metrics=[mean_squared_error])
        return model

    def train_model(self, batch_size=64, val_split=0.2, epoches=50, model=None):
        """

        :param batch_size:
        :param val_split:
        :param epoches:
        :param model:
        :return:
        """
        if model is None:
            model = self.build_model()
        return

    def load_lstm_model(self):
        pass

    def recommend(self):
        pass
