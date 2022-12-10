# I'm chillin
# Part1: 00:16:56
# Part2: 00:32:09

def cycle(img, c, x):
    if (c-1)%40 in [x, x-1, x+1]:
        img[c-1] = "#" 
    if (c-20)%40 == 0:
        return c*x
    return 0

def start(inp, lines):
    cycles = 0
    X = 1
    res = 0
    image = ['.']*40*6
    for c in lines:
        cmd = c.split(' ')
        cycles += 1
        res += cycle(image, cycles, X)
        if cmd[0] == 'addx':
            cycles += 1
            res += cycle(image, cycles, X)
            X += int(cmd[1])
    print(res)
    for r in range(0,6):
        for c in range(0,40):
            print(image[r*40 + c], end='')
        print('')
        