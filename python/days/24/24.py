import utils as u


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def mod(t1, m):
    return (t1[0] % m[0], t1[1] % m[1])


def process(blizzards, bounds):
    return [(mod(add(b[0], b[1]), bounds), b[1]) for b in blizzards]


def solve(pos, blizzards, bounds, end, start):
    next_positions = set([])
    for d in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
        goto = add(pos, d)
        for b in blizzards:
            if goto == b[0]:
                break
        else:
            if goto[0] >= 0 and goto[0] < bounds[0] and goto[1] >= 0 and goto[1] < bounds[1] or goto == end or goto == start:
                next_positions.add(goto)
    return next_positions


def start(line, lines):
    map = u.parse_columns(lines, 0, 0, 1)
    u.print_transposed(map)
    start = (list(map[:, 0]).index('.')-1, -1)
    end = (list(map[:, -1]).index('.')-1, map.shape[1]-2)
    map = map[1:-1, 1:-1]
    u.print_transposed(map)
    blizzards = []
    for x, c in enumerate(map):
        for y, v in enumerate(c):
            if v != '.':
                blizzards.append(((x, y), {
                    '<': (-1, 0),
                    '>': (1, 0),
                    'v': (0, 1),
                    '^': (0, -1)
                }[v]))
    positions = set([start])
    i = 0
    round1 = 0
    round2 = 0
    reached_end_once = False
    reached_start_again = False
    finished = False
    while True:
        next_positions = set([])
        for p in positions:
            next_positions |= solve(p, blizzards, map.shape, end, start)
        blizzards = process(blizzards, map.shape)
        positions = next_positions

        print('round', i)
        for p in positions:
            if reached_end_once and p == start and not reached_start_again:
                positions = [start]
                reached_start_again = True
                print('Going back to end...')
                break
            if p == end and not reached_end_once:
                    round1 = i
                    reached_end_once = True
                    positions = [end]
                    print('Going back start...')
                    break
            if p == end and reached_start_again:
                    print('Finished!')
                    finished = True
                    round2 = i
                    break
        i += 1
        if finished:
            break
    print(round1, round2)