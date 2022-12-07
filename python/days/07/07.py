# Life is fleeting, everything dies, all good things must come to an end. Why 
# are we even here...
# Part1: 00:37:56
# Part2: 00:47:11

import numpy as np
import itertools as it
import utils as u
import re

def start(inp, lines):
    dirs = {'/': 0}
    path = ['/']
    for cmd in list(map(lambda x: list(map(lambda x: x.split(' '), x.strip().split('\n'))), filter(lambda x: x, inp.split('$')))):
        if cmd[0][0] == 'cd':
            if cmd[0][1] == '..':
                path.pop()
            elif cmd[0][1] == '/':
                path = ['/']
            else:
                path.append(''.join(path[-1:] + [cmd[0][1], '/']))
                print(path)
                if path[-1] not in dirs:
                    dirs[path[-1]] = 0
        if cmd[0][0] == 'ls':
            for f in cmd[1:]:
                if f[0] != 'dir':
                    for d in path:
                        print(d)
                        dirs[d] += int(f[0])
    
    whole_sum = 0
    for d in dirs:
        if dirs[d] <= 100000:
            whole_sum += dirs[d]
            
    acceptable = []
    for d in dirs:
        if dirs[d] >= (30000000 - (70000000 - dirs['/'])):
            acceptable.append(dirs[d])

    print(whole_sum, min(acceptable))