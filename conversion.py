from __future__ import division
import numpy as np

def convert(celsius):
    np_celsius = np.array(celsius)
    np_fahrenheit = (np_celsius * (9/5)) + 32
    return list(np_fahrenheit)
