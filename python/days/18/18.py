# Haha, maybe a recursive function wasn't so smart :P

import itertools
import sys

sys.setrecursionlimit(2000)

def march(cube, cubes, visited=[]):
    visited.append(cube)
    sides = 0
    has_adjacent = False
    for inc in itertools.product(*([[1, -1, 0]]*3)):
        next = [cube[0] + inc[0], cube[1] + inc[1], cube[2] + inc[2]]
        if next in cubes:
            has_adjacent = True
            if inc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                if next in cubes:
                    sides += 1
    if has_adjacent:
        for inc in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            if inc != (0,0,0):
                next = [cube[0] + inc[0], cube[1] + inc[1], cube[2] + inc[2]]
                if next not in visited and next not in cubes:
                    new_sides, visited = march(next, cubes, visited)
                    sides += new_sides
    return sides, visited
              

def start(line, lines):
    cubes = [[int(i) for i in l.split(',')] for l in lines]
    sides = 0
    left_most_cube = None
    for cube in cubes:
        covered = 0
        for inc in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            if [cube[0] + inc[0], cube[1] + inc[1], cube[2] + inc[2]] in cubes:
                covered += 1
        sides += 6 - covered
        if left_most_cube == None or left_most_cube[0] > cube[0]:
            left_most_cube = cube
    if left_most_cube is not None:
        air_cube = [left_most_cube[0] - 1,left_most_cube[1],left_most_cube[2]]
        air_contact, _ = march(air_cube, cubes)
        print(sides, air_contact)
    else:
        print('No left most cube found, 0 input?')