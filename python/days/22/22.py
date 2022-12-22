import utils as u
import numpy as np
import re
import math

# oh god please let me get this right on the first try
# Ps. I didnt :)
face_map = [
    #  01
    #  2
    # 34
    # 5

    [ # 0
        [1, 0], # don't rotate
        [2, 0], # don't rotate
        [3, 2], # 180 rot
        [5, 1], # 90 rot
    ],
    [ # 1
        [4, 2],
        [2, 1],
        [0, 0],
        [5, 0]
    ],
    [ # 2 
        [1, -1],
        [4, 0],
        [3, -1],
        [0, 0]
    ],
    [ # 3
        [4, 0],
        [5, 0],
        [0, 2],
        [2, 1]
    ],
    [ # 4
        [1, 2],
        [5, 1],
        [3, 0],
        [2, 0]
    ],
    [ # 5
        [4, -1],
        [1, 0],
        [0, -1],
        [3, 0]
    ]
]

def get_board_tile(board, at, direction):
    new = at.copy()
    new[1] = (at[1] + direction[1]) % len(board[0])
    new[0] = (at[0] + direction[0]) % len(board)
    new_dir = direction.copy()
    if board[new[0]][new[1]] == ' ':
        fr = math.floor(at[1]/50)
        fc = math.floor(at[0]/50)
        face = 0
        rel_pos = [at[0] - fc*50, at[1] - fr*50]
        match [fr, fc]:
            case [0, 1]:
                face = 0
            case [0, 2]:
                face = 1
            case [1, 1]:
                face = 2
            case [2, 0]:
                face = 3
            case [2, 1]:
                face = 4
            case [3, 0]:
                face = 5
        curr_rot = (round(math.atan2(direction[1], direction[0])/(math.pi/2)) % 4)
        to = face_map[face][curr_rot]
        to_rot = to[1]
        new_rot = (curr_rot + to_rot) % 4
        new_dir = [round(math.cos(new_rot*math.pi/2)), round(math.sin(new_rot*math.pi/2))]
        new_face = to[0]
        face_pos = [0,0]
        match new_face:
            case 0:
                face_pos = [0,1]
            case 1:
                face_pos = [0,2]
            case 2:
                face_pos = [1,1]
            case 3:
                face_pos = [2,0]
            case 4:
                face_pos = [2,1]
            case 5:
                face_pos = [3,0]
        real_face_pos = [face_pos[1]*50, face_pos[0]*50]
        new_rel_pos = [0,0]
        match to_rot:
            case 0:
                if direction[0] == 0:
                    new_rel_pos[0] = rel_pos[0]
                elif direction[0] == 1:
                    new_rel_pos[0] = 0
                elif direction[0] == -1:
                    new_rel_pos[0] = 49

                if direction[1] == 0:
                    new_rel_pos[1] = rel_pos[1]
                elif direction[1] == 1:
                    new_rel_pos[1] = 0
                elif direction[1] == -1:
                    new_rel_pos[1] = 49
            case 1:
                new_rel_pos = [rel_pos[1], rel_pos[0]]
            case -1:
                new_rel_pos = [rel_pos[1], rel_pos[0]]
            case 2:
                new_rel_pos = rel_pos.copy()
                if direction[1] == 0:
                    new_rel_pos[1] = 49 - new_rel_pos[1]
                else:
                    new_rel_pos[0] = 49 - new_rel_pos[0]
        new = [real_face_pos[0] + new_rel_pos[0], real_face_pos[1] + new_rel_pos[1]]

    return new, new_dir
    

def start(line, lines):
    (map, move) = u.split_list(lines, '')
    move = move[0]
    move = move
    map = u.parse_columns(map, 0, 0, 1, ' ')
    dbg_map = map.copy()
    pos = []
    for y in range(0, len(map[0])):
        for x in range(0, len(map)):
            if map[x][y] != ' ':
                pos = [x,y]
                break
        else:
            continue
        break
    rotation = 0
    while match := re.match('^(\\d+|\\D)', move):
        move = move[match.span()[1]:]
        cmd = match.group(0)
        #print(cmd)
        if cmd.isnumeric():
            dir = [round(math.cos(rotation)), round(math.sin(rotation))]
            for i in range(0, int(cmd)):
                p, d = get_board_tile(map, pos, dir)
                if map[p[0], p[1]] != '#':
                    match dir:
                        case [1, 0]:
                            dbg_map[pos[0]][pos[1]] = '>'
                        case [0, 1]:
                            dbg_map[pos[0]][pos[1]] = 'v'
                        case [-1,0]:
                            dbg_map[pos[0]][pos[1]] = '<'
                        case [0, -1]:
                            dbg_map[pos[0]][pos[1]] = '^'
                    dir = d
                    rotation = math.atan2(dir[1], dir[0])
                    pos = p
                else:
                    dbg_map[p[0]][p[1]] = 'X'
                    break
        else:
            if cmd == 'L':
                rotation -= math.pi/2
            elif cmd == 'R':
                rotation += math.pi/2

    c = pos[0]+1
    r = pos[1]+1
    rot = (round(rotation/(math.pi/2)))%4
    
    for faaan in np.array(dbg_map).T:
        print(''.join(faaan))

    print(1000*r + 4*c + rot)
    #print(get_board_tile(map, [2,8], [0,1]))