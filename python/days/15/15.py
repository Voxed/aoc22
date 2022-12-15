# answer to part1 is wrong since I don't feel like refining the solution to work
# for both

from numpy.lib import stride_tricks as st
import numpy as np
import re
import inspect

def start(_, lines):
    df = []
    df_sensors = []
    bound_x = (999999,-999999)
    bound_y = (999999,-999999)
    beacons = []
    for l in lines:
        e = re.split('=|,|:', l)
        (sx, sy, bx, by) = int(e[1]), int(e[3]), int(e[5]), int(e[7])
        dist = abs(bx-sx) + abs(by-sy)
        bound_x = (min(bound_x[0], sx-dist), max(bound_x[1], sx+dist+1))
        bound_y = (min(bound_y[0], sy-dist), max(bound_y[1], sy+dist+1))
        df.append(lambda x,y,sx=sx,sy=sy,dist=dist: abs(x-sx) + abs(y-sy) - dist)
        beacons.append((bx, by))
        df_sensors.append((sx, sy, dist))
    print(bound_x, bound_y)
    sum1 = 0

    pos = (0,0)
    done = False
    for y in range(0, 4000001):
        c = 0#bound_x[0] - 20000
        if done:
            break
        counted = []
        print(y)
        for b in beacons:
            if b[1] == y and b[1] not in counted:
                counted.append(b[1])
                sum1 -= 1
        while c <= 4000000: #bound_x[1] + 20000:
            min_dist = 9999999
            for i, f in enumerate(df):
                if (d := f(c, y)) <= 0:
                    s = df_sensors[i]
                    end = s[0]+s[2] - abs(s[1]-y)+1
                    sum1 += abs(c - end)
                    c = end
                    break
                else:
                    min_dist = min(min_dist, d)
            else:
                pos = (c,y)
                done = True
                c += min_dist
    for f in df:
        if f(*pos) <= 0:
            print("BAD")
            break
    print(sum1, pos)