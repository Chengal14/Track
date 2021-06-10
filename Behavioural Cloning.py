import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
import cv2
import pandas as pd
import random

import os

datadir='track'
columns=['center','left','right','throttle','steering','reverse','speed']
data=pd.read_csv(datadir,'driving_log.csv',names=columns)
data.head()