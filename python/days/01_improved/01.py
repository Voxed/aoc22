# Part1: 00:03:10
# Part2: 00:05:59

import numpy as np
import itertools as it
import utils as u

def start(inp):
    elfs = np.sort(u.pad_jagged([f.strip().split('\n') for f in inp.split('\n\n')]).astype(int).sum(axis=1))
    print(elfs[-1], elfs[-3:].sum())
