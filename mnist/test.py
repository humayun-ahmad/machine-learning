# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:24:45 2020

@author: acer
"""


import pandas as pd
import numpy as np

np.random.seed(1212)

import keras
from keras.models import Model
from keras.layers import *
from keras import optimizers

df_test = pd.read_csv('mnist_train.csv')
df_train = pd.read_csv('mnist_test.csv')

df_train.head()
