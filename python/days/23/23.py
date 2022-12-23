# Changed solution a bit, so part1 is not present atm

import utils as u

def start(line, lines):
    map = u.parse_columns(lines, 0, 0, 1, ' ')
    elves = []
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == '#':
                elves.append((x,y))

    directions = [[0,-1],[0,1],[-1,0],[1,0]]
    final_round = 0
    for round in range(0,10000):
        proposals = []
        for x,y in elves:
            any_adj = False
            for j in range(-1,2):
                for i in range(-1,2):
                    if i != 0 or j != 0:
                        check = (x+i, y+j)
                        if check in elves:
                            any_adj = True
                            break
                else:
                    continue
                break
            proposed = False
            if any_adj:
                for d in directions:
                    check = []
                    for i in range(-1,2):
                        if d[1] == 0:
                            check = (x+d[0], y+i)
                        else:
                            check = (x+i, y+d[1])
                        if check in elves:
                            break
                    else:
                        proposals.append((x+d[0], y+d[1]))
                        proposed = True
                        break
            if not proposed:
                proposals.append(None)
        move = False
        moves = 0
        for i,(x,y) in enumerate(elves):
            if proposals[i] is not None:
                p = proposals[i]
                count = proposals.count(p)
                if count == 1:
                    elves[i] = (p[0], p[1])
                    move = True
                    moves += 1
        if not move:
            final_round = round+1
            break
        else:
            print(moves)

        directions.append(directions.pop(0))

    print(final_round)