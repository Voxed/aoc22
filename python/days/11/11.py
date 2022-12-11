# Mathy! I've been awake for 29 hours, so I'm going to improve this later.
# Part1: 0:40:50
# Part2: 0:51:08

import numpy as np
import utils as u


def start(inp, lines):  
    data = u.split_list(lines, '')
    monkeys = []
    for d in data:
        m = {
            'items': list(np.array(d[1][18:].split(',')).astype(int)),
            'operation': d[2][19:],
            'test': [int(d[4][29:]), int(d[5][30:]), int(d[3][21:])],
            'inspected': 0
        }
        monkeys.append(m)
    gcd = 1
    for m in monkeys:
        gcd *= m['test'][2]
    for i in range(0,10000):
        for m in monkeys:
            items = m['items']
            m['items'] = []
            for i in items:
                m['inspected'] += 1
                old = i
                worry = eval(m['operation']) % gcd
                mindex = (m['test'][0] if (worry % m['test'][2]) == 0 else m['test'][1])
                monkeys[mindex]['items'].append(worry)
    inspected = []
    for m in monkeys:
        inspected.append(m['inspected'])
    print(np.product(sorted(inspected)[-2:]))    