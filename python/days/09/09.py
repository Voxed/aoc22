# Yeah it's ugly, yeah it works
# Part1: 00:26:27
# Part2: 00:42:16
import numpy as np
import utils as u

def start(inp, lines):
    DEBUG = False # Print map in each state or nah?

    head = [0,0]
    tail = [0,0]

    ropes = [[0,0]]*10

    poses0 = [[0,0]]
    poses1 = [[0,0]]

    for m in lines:
        cmd = m.split(' ')
        for i in range(0, int(cmd[1])):
            head = ropes[0]
            match cmd[0]:
                case 'R':
                    head = np.add(head, [1, 0])
                case 'U':
                    head = np.add(head, [0, 1])
                case 'L':
                    head = np.add(head, [-1, 0])
                case 'D':
                    head = np.add(head, [0, -1])
            ropes[0] = list(head)

            for r in range(0, len(ropes)-1):
                head = ropes[r]
                tail = ropes[r+1]

                if list(head) == list(np.add(tail, [2, 0])):
                    tail = np.add(tail, [1, 0])
                elif list(head) == list(np.add(tail, [0, 2])):
                    tail = np.add(tail, [0, 1])
                elif list(head) == list(np.add(tail, [-2, 0])):
                    tail = np.add(tail, [-1, 0])
                elif list(head) == list(np.add(tail, [0, -2])):
                    tail = np.add(tail, [0, -1])

                elif head[0] == tail[0] + 2:
                    if head[1] >= tail[1] + 1:
                        tail = np.add(tail, [1, 1])
                    elif head[1] <= tail[1] - 1:
                        tail = np.add(tail, [1, - 1])
                elif head[0] == tail[0] - 2:
                    if head[1] >= tail[1] + 1:
                        tail = np.add(tail, [-1, 1])
                    elif head[1] <= tail[1] - 1:
                        tail = np.add(tail, [-1, - 1])
                elif head[1] == tail[1] + 2:
                    if head[0] >= tail[0] + 1:
                        tail = np.add(tail, [1, 1])
                    elif head[0] <= tail[0] - 1:
                        tail = np.add(tail, [-1, 1])
                elif head[1] == tail[1] - 2:
                    if head[0] >= tail[0] + 1:
                        tail = np.add(tail, [1, -1])
                    elif head[0] <= tail[0] - 1:
                        tail = np.add(tail, [-1, -1])

                ropes[r] = head
                ropes[r+1] = list(tail)

            if(list(ropes[1]) not in poses0):
                poses0.append(list(ropes[1]))

            if(list(ropes[9]) not in poses1):
                poses1.append(list(ropes[9]))

            if DEBUG:
                print('')
                for i in range(0, 5):
                    for j in range(0, 6):
                        done = False
                        if ropes[0] == [j,4-i]:
                            done = True
                            print("H", end='')
                        if not done:
                            for r in range(1, len(ropes)):
                                if ropes[r] == [j,4-i]:
                                    print(str(r), end='')
                                    done = True
                                    break
                        if not done:
                            print(".", end='')
                    print('')

    print(len(poses0), len(poses1))
