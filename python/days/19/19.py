# Not fast :(

import numpy as np
import re

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
MAX_ROBOTS = 4


def craft(blueprint, resources=np.array([0, 0, 0, 0], dtype=int), robots=np.array([1, 0, 0, 0], dtype=int), minutes=24, goal=None, best_so_far=None):
    if best_so_far is None:  # Create best of counter if it does not yet exist.
        best_so_far = [0]
    # Cull states which can never reach best of
    if ((minutes-1)*(minutes)/2 + robots[GEODE]*minutes + resources[GEODE]) < best_so_far:
        return -1
    # Track best amount of geodes so far
    best_so_far[0] = max(resources[3], best_so_far[0])
    if minutes <= 1:
        return (resources + np.multiply(robots, minutes))[3]
    if goal is None:  # If no goal, branch onto new goals.
        best_result = 0
        for goal in [0, 1, 2, 3]:
            # Is the goal necessary?
            if robots[goal] < blueprint[MAX_ROBOTS][goal] or blueprint[MAX_ROBOTS][goal] == -1:
                # Can we reach the goal?
                if (((robots > 0) & (blueprint[goal] > 0)) == (blueprint[goal] > 0)).all():
                    best_result = max(best_result, craft(
                        blueprint, resources, robots, minutes, goal, best_so_far))
        return best_result
    # Work towards goal
    if ((resources - blueprint[goal]) >= 0).all():
        resources = resources - blueprint[goal]
        resources = resources + robots  # Get does resources
        robots = np.ndarray.copy(robots)
        robots[goal] += 1
        goal = None
    else:
        resources = resources + robots  # Get does resources
    return craft(blueprint, resources, robots, minutes-1, goal, best_so_far)


def start(line, lines):
    blueprints = []
    arr = [int(f.replace(' ', ''))
           for f in re.sub('[^0-9]*', ' ', line).split('  ') if f != '']
    for b in np.reshape(arr, (-1, 7)):
        bp = np.zeros((5, 4), dtype=int)
        bp[ORE] = [b[1], 0, 0, 0]
        bp[CLAY] = [b[2], 0, 0, 0]
        bp[OBSIDIAN] = [b[3], b[4], 0, 0]
        bp[GEODE] = [b[5], 0, b[6], 0]
        # Max robots usable for each type
        bp[MAX_ROBOTS] = [max([b[1], b[2], b[3]]), b[4], b[6], -1]
        blueprints.append(bp)

    quality_sum = 0
    for id, bp in enumerate(blueprints):
        qual = craft(bp)
        quality_sum += (id+1)*qual

    quality_prod = 1
    for id, bp in enumerate(blueprints[0:3]):
        qual = craft(bp, minutes=32)
        quality_prod *= qual
    print(quality_sum, quality_prod)