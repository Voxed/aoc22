# Useful stuff collected through the adventure!

import numpy as np
import itertools as it
import sys

def pad_jagged(array):
    return np.array(list(it.zip_longest(*array, fillvalue=0))).T

def subset_of(array1, array2):
    return all(map(lambda x: x in array2, array1))

def symmetry(func, v1, v2 = None):
    if v2 is None:
        v2 = v1[1]
        v1 = v1[0]
    return np.array([func(v1,v2), func(v2,v1)])

def irange(a, b = None):
    if b is None:
        l = np.array(a, dtype=int)
        b = l[1]
        a = l[0]
    return np.array(range(a,b+1))