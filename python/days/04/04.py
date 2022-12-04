# Part1: 00:05:55
# Part2: 00:09:27

import numpy as np
import itertools as it
import utils as u

def start(inp, lin):
    count = 0
    count2 = 0
    for line in lin:
        ranges = line.split(',')
        r1 = ranges[0].split('-')
        r2 = ranges[1].split('-')
        
        if (int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[1])) or (int(r1[0]) >= int(r2[0]) and int(r1[1]) <= int(r2[1])):
            count += 1

        if ((int(r1[0]) >= int(r2[0]) and int(r1[0]) <= int(r2[1])) or (int(r1[1]) >= int(r2[0]) and int(r1[1]) <= int(r2[1])) or
            (int(r2[0]) >= int(r1[0]) and int(r2[0]) <= int(r1[1])) or (int(r2[1]) >= int(r1[0]) and int(r2[1]) <= int(r1[1]))):
            count2 += 1

    print(count, count2)