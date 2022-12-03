# Part1: 00:07:17  
# Part2: 00:12:29

def score(i):
    return (3 if (i[0]-1)%3 != i[1] else 0) + (3 if (i[0]+1)%3 == i[1] else 0) + i[1]+1

def start(inp, lin):
    cmds = [(lambda g: [ord(g[0])-65, ord(g[1])-88])(f.split(' ')) for f in inp.split('\n')]
    print(sum(map(score, cmds)), sum(map(score, map(lambda x: [x[0], (x[0] + x[1] - 1)%3], cmds))))
