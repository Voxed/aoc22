import utils as u
from functools import cmp_to_key

def compare(l, r):
    if [type(l), type(r)] == [int, int]:
        return l - r
    l, r = [[v] if type(v) == int else v for v in (l, r)]
    for i in range(0, min(len(l), len(r))):
        if not (c := compare(l[i], r[i])) == 0:
            return c
    return len(l) - len(r)


def start(_, lines):
    sum = 0
    packets = []
    for i, p in enumerate(u.split_list(lines, '')):
        l, r = eval(p[0]), eval(p[1])
        sum += (i+1)*(compare(l, r) < 0)
        packets += [l, r]
    packets = sorted(packets + [[2], [6]], key=cmp_to_key(compare))
    print(sum, (packets.index([2])+1)*(packets.index([6])+1))
