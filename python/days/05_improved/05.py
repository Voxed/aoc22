# Aight, imma call it with the one-liners.
# Time for some beauty code :)
# Part1: 00:11:26
# Part2: 00:14:47

import numpy as np
import utils as u
import copy


def start(_, lines):
    (crates, cmds) = u.split_list(lines, '')
    stacks9000 = [[u for u in f if u != ' ']
                  for f in u.parse_columns(crates[:-1], 1, 3)]
    stacks9001 = copy.deepcopy(stacks9000)
    for (c, s1, s2) in [np.array(u.parse_nums(c))-[0, 1, 1] for c in cmds]:
        stacks9001[s2] = stacks9001[s1][:c] + stacks9001[s2]
        stacks9001[s1] = stacks9001[s1][c:]
        for _ in range(0, c):
            stacks9000[s2].insert(0, stacks9000[s1].pop(0))
    print(''.join([e[0] for e in stacks9000]),
          ''.join([e[0] for e in stacks9001]))
