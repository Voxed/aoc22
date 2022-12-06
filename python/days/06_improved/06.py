# 99% of the time spent reading >:(
# Part1: 00:05:53
# Part2: 00:06:34
import numpy as np
from numpy.lib import stride_tricks as st
import utils as u

def start(inp, _):
    print((u.super_map([np.unique, len, lambda x: x < 4], st.sliding_window_view(list(inp), 4))).index(False)+4)
    print((u.super_map([np.unique, len, lambda x: x < 14], st.sliding_window_view(list(inp), 14))).index(False)+14)
