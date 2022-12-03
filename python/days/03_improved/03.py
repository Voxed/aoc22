# Part1: 00:08:16
# Part2: 00:15:10
import numpy as np
from functools import reduce

def start(inp, lin):
    print([sum([sum(map(lambda x: (x-int(x/26 > 1)*6+26) % 52+1, reduce(np.intersect1d, l).view(np.int32)-65)) for l in m]) for m in [
        [np.split(np.array(list(f)), 2) for f in lin],                    # p.1
        [map(list, f) for f in np.split(np.array(lin), int(len(lin)/3))]  # p.2
    ]])
