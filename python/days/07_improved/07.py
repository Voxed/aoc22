# Life is fleeting, everything dies, all good things must come to an end. Why 
# are we even here...
# Part1: 00:37:56
# Part2: 00:47:11

import itertools
from collections import defaultdict
import numpy as np

def start(inp, lines):
    dirs = defaultdict(lambda: 0)
    path = ['/']
    for (cmd,*out) in [[y.split(' ') for y in x.strip().split('\n') if not y.startswith('dir')] for x in inp.split('$') if x]:
        match ' '.join(cmd):
            case 'cd ..':
                path.pop()
            case 'cd /':
                path = ['/']
            case 'ls':
                for ((s,_), p) in itertools.product(out, path):
                    dirs[p] += int(s)
            case _:
                path.append(path[-1] + cmd[1] + '/')
    sizes = np.array(list(dirs.values()));
    print(sizes[sizes <= 100000].sum(), sizes[sizes >= (-40000000 + dirs['/'])].min())