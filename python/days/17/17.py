# God damn

from numpy.lib import stride_tricks as st
from scipy.sparse.csgraph import dijkstra

ROCK_SHAPES = [
    ["####"],

    [".#.",
     "###",
     ".#."],

    ["###",
     "..#",
     "..#"],

    ["#",
     "#",
     "#",
     "#"],

    ["##",
     "##"]
]


def start(line, lines):
    floor_height = 0
    rock_pos = (0,0)
    room = [['.']*7]
    gas = list(line)
    gas_index = 0
    effect_index = 0

    repeats = []
    repeat_heights = []

    part2_solution = None
    part1_solution = None

    height_log = []

    for rock_index in range(0,1000000000000):
        if part2_solution is not None and part1_solution is not None:
            break
        rock_shape = ROCK_SHAPES[rock_index % len(ROCK_SHAPES)];
        rock_size = [len(rock_shape[0]), len(rock_shape)]
        rock_pos = [2, floor_height + rock_size[1] + 3]
        if rock_index == 2022:
            part1_solution = floor_height


        height_log.append(floor_height)

        while True:
            old_pos = rock_pos.copy()
            effect_index += 1

            if (effect_index % 2) == 1:
                effect = gas[(gas_index) % len(gas)]
                if part2_solution is None and gas_index > len(gas) and len(height_log) > 10:
                    if [(gas_index) % len(gas), rock_index % len(ROCK_SHAPES)] not in repeats:
                        repeats.append([(gas_index) % len(gas), rock_index % len(ROCK_SHAPES)])
                        repeat_heights.append((rock_index, floor_height, [f-floor_height for f in height_log[-10:]]))
                    else:
                        rep_index = repeats.index([(gas_index) % len(gas), rock_index % len(ROCK_SHAPES)])
                        if rep_index != len(repeats)-1:
                            (ri, pr, log) = repeat_heights[rep_index]
                            until_done = 1000000000000 - rock_index
                            if until_done % (rock_index - ri) == 0:
                                # I'm using the ten previous heights as a unique key for the repetition pattern.
                                # This is necessary because [(gas_index) % len(gas), rock_index % len(ROCK_SHAPES)] is not actually a
                                # reliable delimiter for reptition.
                                # Basic code is just, if the 10 previous heighs have already occured, we have a repetition.
                                if log == [f - floor_height for f in height_log[-10:]]:
                                    part2_solution = floor_height + (floor_height - pr) * (until_done / (rock_index - ri))
                                else:
                                    repeat_heights[rep_index] = (rock_index, floor_height, [f-floor_height for f in height_log[-10:]])
                gas_index += 1

                if effect == '<':
                    rock_pos[0] -= 1
                else:
                    rock_pos[0] += 1          

            else:
                rock_pos[1] -= 1


            blocked = False
            if rock_pos[0] < 0 or rock_pos[0] + rock_size[0] >= 8:
                blocked = True  

            bottom_pos = rock_pos[1] - rock_size[1]
            if bottom_pos < 0:
                blocked = True

            if not blocked:
                for rx, x in enumerate(range(rock_pos[0], rock_pos[0] + rock_size[0])):
                    for ry, y in enumerate(range(rock_pos[1] - rock_size[1], rock_pos[1])):
                        if y < len(room):
                            if rock_shape[ry][rx] == room[y][x] == '#':
                                blocked = True

            if blocked:
                rock_pos = old_pos
                if (effect_index % 2) == 0:
                    break
            
        while rock_pos[1] >= len(room):
            room.append(['.']*7)

        for rx, x in enumerate(range(rock_pos[0], rock_pos[0] + rock_size[0])):
            for ry, y in enumerate(range(rock_pos[1] - rock_size[1], rock_pos[1])):
                if rock_shape[ry][rx] == '#':
                    room[y][x] = '#'
        floor_height = max(floor_height, rock_pos[1])

    print(part1_solution, part2_solution)
