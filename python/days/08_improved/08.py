# I'm sorry for this
# Part1: 00:08:55
# Part2: 00:16:42
import numpy as np

def raycast(m, zx, y, d):
    for l in range(1, max(m.shape)+1):
        if not ((p := np.add(zx, np.multiply(d, l)))[0] in range(0, m.shape[0]) and p[1] in range(0, m.shape[1])):
            return [l-1, 0]
        if m[p[0], p[1]] >= y:
            return [l, 1]

def start(inp, lines):
    m = np.array([list(f) for f in lines]).astype(int)
    r = np.array([[raycast(m, i, m[i[0], i[1]], d) for d in [
                 [0, 1], [0, -1], [1, 0], [-1, 0]]] for i in np.ndindex(m.shape)])
    print((visible := r[(r[:, :, 1] == 0).any(axis=1)]
           ).shape[0], visible[:, :, 0:2].prod(axis=1).max())
