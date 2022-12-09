# Short stuff 
import numpy as np
from functools import reduce


def start(inp, lines):
    ropes = [[[0, 0]]*10]*2
    for cmd in [l.split(' ') for l in lines]:
        for i in range(0, int(cmd[1])):
            ropes[-1][0] = list(np.add(ropes[-2][0], {'R': [1, 0], 'U': [
                0, 1], 'L': [-1, 0], 'D': [0, -1]}[cmd[0]]))
            ropes[-1] = reduce(lambda rs, r: rs + [
                list(np.add(r, np.sign(np.divide(diff, norm)))) if (
                    norm := np.linalg.norm(diff := np.subtract(rs[-1], r))) >= 2 else r
            ], ropes[-1][1:], [ropes[-1][0]])
            ropes.append(ropes[-1])
    print(*[np.unique(col, axis=0).shape[0]
          for col in [np.array(ropes[:-1])[:, 1], np.array(ropes[:-1])[:, 9]]])
