# 99% of the time spent reading >:(
# Part1: 00:05:53
# Part2: 00:06:34
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv
import utils as u


def start(inp, _):
    print(*map(lambda x: list(u.mmap(np.unique, len,
          swv(list(inp), x)) == x).index(1)+x, [4, 14]))
