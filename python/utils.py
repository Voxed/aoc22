# Useful stuff collected through the adventure!

import numpy as np
import itertools as it
import sys

def pad_jagged(array):
    return np.array(list(it.zip_longest(*array, fillvalue=0))).T