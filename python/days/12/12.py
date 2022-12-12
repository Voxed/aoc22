# Didn't wake up at 6:00 so got no time to brag with :(

import numpy as np
import utils as u
from scipy.sparse import csr_matrix

from scipy.sparse.csgraph import dijkstra


def start(inp, lines):
    grid = [list([ord(o)-97 for o in s]) for s in lines]
    start = 0
    end = 0
    graph = [[0]*(len(grid[0])*len(grid))
             for i in ([0]*(len(grid[0])))*len(grid)]

    a_nodes = []

    for ri, r in enumerate(grid):
        for ci, v in enumerate(r):
            node_index = ri*len(grid[0]) + ci
            if v == -14:
                start = node_index
                grid[ri][ci] = ord('a')-97
            if v == -28:
                end = node_index
                grid[ri][ci] = ord('z')-97
            if grid[ri][ci] == 0:
                a_nodes.append(node_index)

    for ri, r in enumerate(grid):
        for ci, v in enumerate(r):
            node_index = ri*len(grid[0]) + ci
            for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                rj = ri + d[0]
                cj = ci + d[1]
                if rj >= 0 and rj < len(grid) and cj >= 0 and cj < len(grid[0]):
                    if grid[rj][cj] <= v+1:
                        node_index_dest = rj*len(grid[0]) + cj
                        graph[node_index][node_index_dest] = 1

    graph = csr_matrix(graph)
    dist_matrix, predecessors = dijkstra(
        csgraph=graph, indices=a_nodes, directed=True, return_predecessors=True)
    dists = [i[end] for i in dist_matrix]
    print(dist_matrix[a_nodes.index(start)][end], min(dists))
