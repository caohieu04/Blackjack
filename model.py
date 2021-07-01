from tensorflow.keras import *
from tensorflow.keras.layers import *
import numpy as np

class MyModel():
  Sequential = None

  def __init__(self):
    super(MyModel, self).__init__()
    self.Sequential = Sequential([
        Input(52),
        # Dense(512, activation='relu'),
        # Dense(256, activation='relu'),
        # Dense(256, activation='relu'),
        # Dense(128, activation='relu'),
        # Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1)
    ])