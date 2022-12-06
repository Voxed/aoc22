# 99% of the time spent reading >:(
# Part1: 00:05:53
# Part2: 00:06:34

def start(inp, lines):
    buff = []
    i = 0
    for c in inp:
        i+= 1
        buff += [c]
        if len(buff) >= 4:
            buff = buff[-4:]
            unique = True
            for c in buff:
                if buff.count(c) > 1:
                    unique = False
            if unique:
                print(f"{i}, ", end='')
                break
    buff = []
    i = 0
    for c in inp:
        i+= 1
        buff += [c]
        if len(buff) >= 14:
            buff = buff[-14:]
            unique = True
            for c in buff:
                if buff.count(c) > 1:
                    unique = False
            if unique:
                print(i)
                break