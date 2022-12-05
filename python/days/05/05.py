# This calls for some new utility functions!!!
# Part1: 00:11:26
# Part2: 00:14:47

import numpy as np
import itertools as it
import utils as u
import re

def start(inp, lin):
    # Haha i orginally hardcoded the stacks in this solution, gotta change this
    # before github 
    # stacks = [
    #     ['S','L','F','Z','D','B','R','H'],
    #     ['R','Z','M','B','T'],
    #     ['S','N','H','C','L','Z'],
    #     ['J','F','C','S'],
    #     ['B','Z','R','W','H','G','P'],
    #     ['T','M','N','D','G','Z','J','V'],
    #     ['O','P','S','F','W','N','L','G'],
    #     ['R','Z','M'],
    #     ['T','R','V','G','L','C','M']
    # ]
    stacks = []
    for s in lin[0:lin.index('')-1]:
        stacks.append(re.sub('    ', ' ', s).replace(']', '').replace('[', '').split(' '))
    stacks = [[f for f in d if f] for d in np.array(stacks).T]
    stacks2 = [x[:] for x in stacks]

    for l in lin[lin.index('')+1:]:
        cmd = []
        for let in l.split(' '):
            try:
                cmd.append(int(let))
            except:
                pass
        move = []
        for i in range(0, cmd[0]):
            move.append(stacks[cmd[1]-1].pop(0))
            stacks2[cmd[2]-1].insert(0, stacks2[cmd[1]-1].pop(0))
        stacks[cmd[2]-1] = move + stacks[cmd[2]-1]

    for s in stacks2:
        print(s[0], end='')
    print(', ', end = '')
    for s in stacks:
        print(s[0], end='')
    print('')