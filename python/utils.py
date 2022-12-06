# Useful stuff collected through the adventure!

import numpy as np
import itertools as it
import sys
import re

# Pads out a jagged array into an even matrix by inserting zeros
def pad_jagged(array):
    return np.array(list(it.zip_longest(*array, fillvalue=0))).T

# Returns true if array1 is a subset of array2
def subset_of(array1, array2):
    return all(map(lambda x: x in array2, array1))

# Calls a bivariate function twice with the inputs symmetrized, returns the 
# two results in an array[2]
def symmetry(func, v1, v2 = None):
    if v2 is None:
        v2 = v1[1]
        v1 = v1[0]
    return np.array([func(v1,v2), func(v2,v1)])

# Inclusive range, self explanatory!
def irange(a, b = None):
    if b is None:
        l = np.array(a, dtype=int)
        b = l[1]
        a = l[0]
    return np.array(range(a,b+1))

# Parse columns from file, start on text-column 'start', read in 'elem_size' 
# characters, move by sep, repeat... Transposes final result so the columns are 
# rows, so the bottom element constitutes as first element in each row.
def parse_columns(inp, start, sep, elem_size = 1):
    rows = []
    for l in inp:
        l = l[start:]
        cells = []
        while(True):
            cells.append(l[0:elem_size])
            l = l[elem_size:]
            if(len(l) > sep + elem_size):
                l = l[sep:]
            else:
                break
        rows.append(cells)
    return np.array(rows).T

# Split a list by a delimiter, perfect for splitting up the input file!
def split_list(list, delim):
    final = []
    curr = []
    for l in list:
        if l == delim:
            final.append(curr)
            curr = []
        else:
            curr.append(l)
    final.append(curr)
    return final

# Parse any ol' numbers on the line, discard words!
def parse_nums(l, delim = ' '):
    nums = []
    for p in l.split(delim):
        try:
            nums.append(int(p))
        except:
            pass
    return nums

def super_map(funcs, inp):
    l = inp
    for f in funcs:
        l = map(f, l)
    return list(l)