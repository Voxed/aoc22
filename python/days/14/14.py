from numpy.lib import stride_tricks as st
import numpy as np


def start(_, lines):
    v = [[[np.array(eval('(' + str(s) + ')'))
           for s in t] for t in st.sliding_window_view(l.split('->'), 2)] for l in lines]
    rocks = []
    for s in v:
        for a in s:
            rocks += [list(r) for r in list(np.linspace(a[0],
                                                        a[1], int(np.linalg.norm(a[0] - a[1])+1)))]
    bound_x = int(np.array(rocks)[:, 0].min()), int(np.array(rocks)[:, 0].max())+1
    bound_y = int(np.array(rocks)[:, 1].min()), int(np.array(rocks)[:, 1].max())+1
    bound_x = min(500, bound_x[0]), max(500, bound_x[1]) # Yikes
    bound_y = min(0, bound_y[0]), max(0, bound_y[1]) # Double yikes
    bound_y = bound_y[0], bound_y[1] + 2
    bound_x = bound_x[0] - 1000, bound_x[1] + 1000 # Haha, I hate myself
    grid = [['.']*int(bound_x[1] - bound_x[0]) for r in range(0, int(bound_y[1] - bound_y[0]))] # Don't use a grid idiot
    for r in rocks:
        grid[int(r[1])-bound_y[0]][int(r[0])-bound_x[0]] = '#'
    src = [500 - bound_x[0], 0 - bound_y[0]]
    sim_running = True
    stayed0 = None
    stayed = 0
    while True:
        sand = src.copy()
        while True:
            moved = False
            oob = False
            for m in [[0,1], [-1,1], [1,1]]:
                next = sand.copy()
                next[0] += m[0]
                next[1] += m[1]
                if(next[0] >= 0 and next[0] < len(grid[0]) and next[1] >= 0 and next[1] < len(grid)):
                    if next[1] == bound_y[1]-2 and stayed0 is None: # Horrible
                        stayed0 = stayed
                    if not next[1] == bound_y[1]-1:
                        if grid[next[1]][next[0]] == '.':
                            sand = next
                            moved = True
                            break
                else:
                    oob = True
            if oob:
                sim_running = False # F
                break
            if not moved:
                stayed += 1
                break
        if not sim_running:
            break

        if(sand[0] >= 0 and sand[0] < len(grid[0]) and sand[1] >= 0 and sand[1] < len(grid)):
            grid[sand[1]][sand[0]] = 'o'

        #grid[src[1]][src[0]] = '+'
        #for r in grid:
        #    print(''.join(r))
        
        if(sand[0] == src[0] and sand[1] == src[1]):
            break
    print(stayed0, stayed) # I guess it works