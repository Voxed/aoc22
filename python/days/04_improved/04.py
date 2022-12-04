# Part1: 00:05:55
# Part2: 00:09:27

import numpy as np
import utils as u

def start(inp, lin):
    print((sum([u.symmetry(u.subset_of, [u.irange(l.split('-')) for l in l.split(',')]).any() for l in lin])),
          sum([len(np.intersect1d(*[u.irange(l.split('-')) for l in l.split(',')])) > 0 for l in lin]))