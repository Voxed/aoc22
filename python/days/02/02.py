# This code hurts X_X
# Part1: 00:07:17  
# Part2: 00:12:29

import numpy as np
import itertools as it
import utils as u

def start(inp, lin):
    cmds = [f.split(' ') for f in inp.split('\n')]

    scoresum1 = 0
    for c in cmds:
        score = 0;
        o = ''
        if(c[1] == 'X'):
            o =  'A'
        if(c[1] == 'Y'):
            o = 'B'
        if(c[1] == 'Z'):
            o = 'C'

        if((c[0] == 'A' and o == 'B') or (c[0] == 'B' and o == 'C') or (c[0] == 'C' and o == 'A')):
            score += 6
        if((c[0] == 'A' and o == 'A') or (c[0] == 'B' and o == 'B') or (c[0] == 'C' and o == 'C')):
            score += 3
        if(o == 'A'):
            score += 1
        if(o == 'B'):
            score += 2
        if(o == 'C'):
            score += 3
        scoresum1 += score

    scoresum = 0
    for c in cmds:
        score = 0;
        o = ''
        if c[1] == 'X':
            if(c[0] == 'A'):
                o =  'C'
            if(c[0] == 'B'):
                o = 'A'
            if(c[0] == 'C'):
                o = 'B'
        if c[1] == 'Y':
            o = c[0]
        if c[1] == 'Z':
            if(c[0] == 'A'):
                o =  'B'
            if(c[0] == 'B'):
                o = 'C'
            if(c[0] == 'C'):
                o = 'A' 

        if((c[0] == 'A' and o == 'B') or (c[0] == 'B' and o == 'C') or (c[0] == 'C' and o == 'A')):
            score += 6
        if((c[0] == 'A' and o == 'A') or (c[0] == 'B' and o == 'B') or (c[0] == 'C' and o == 'C')):
            score += 3
        if(o == 'A'):
            score += 1
        if(o == 'B'):
            score += 2
        if(o == 'C'):
            score += 3
        scoresum += score

    print(scoresum1, scoresum)
