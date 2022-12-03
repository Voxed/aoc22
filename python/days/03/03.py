# Part1: 00:08:16
# Part2: 00:15:10

import numpy as np
import itertools as it
import utils as u

def prio(lett):
    p = ord(lett)
    if(p >= 97):
        return p -97+1
    else:
        return p -65+27

def start(inp, lin):
    lines = inp.split('\n')
    sum = 0
    for cmd in lines:
        done = []
        midpoint = int(len(cmd)/2)
        h1 = cmd[0:midpoint]
        for lett in cmd[midpoint:]:
            if(lett in h1 and lett not in done):
                done.append(lett)
                sum += prio(lett)

    sum2 = 0
    for i in range(0, int(len(lines)/3)):
        cmd = lines[i*3:i*3+3]
        done = []
        for lett in cmd[0]:
            if(lett in cmd[1] and lett in cmd[2] and lett not in done):
                done.append(lett)
                sum2 += prio(lett)

    print(sum, sum2)