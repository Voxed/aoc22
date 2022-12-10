# This one be real nice, I EVEN ADDED COMMENTS
from functools import reduce
import numpy as np


def start(inp, lines):
    # Calculate register delta in each cycle, skip last instruction since the screen is too small anyway
    delta = np.array(inp.replace('addx', '0\n').replace(
        'noop', '0').split('\n')[0:-2]).astype(int)

    # Calculate the register state in each cycle
    state = np.array(reduce(lambda xs, x: xs + [xs[-1]+x], delta, [1]))

    # Multiply every 20th cycle by 20, 60 ... 180, 220 and sum them together. Part 1 done!
    print((state[19::40]*np.arange(20, 240, 40)).sum())

    # Generate a screen index array of what column we are on
    pix = np.array(list(range(0, 40))*6)

    # Check whether the register array in each state is equal to pix-1, pix or pix+1
    image = np.logical_or(np.logical_or(
        state == (pix-1), state == (pix+1)), state == (pix))

    # Composite the image from the image boolean array! Part 2 donzo!
    print("\n".join(["".join(f)
          for f in np.split(np.where(image, '#', '.'), 6)]))
