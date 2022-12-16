# Brrrrr 10 minute solution

from numpy.lib import stride_tricks as st
import numpy as np
import re
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import multiprocessing as mp
import time

def best(min, loc, oth, map, open, dist_matrix, node_mapping, hist):
    if min == 0:
        return [hist]
    # All valves are open
    for m in map:
        if not m in open:
            break
    else:
        return [hist]

    best_score = []
    for m in map:
        if m not in open:
            arrival1 = min-dist_matrix[node_mapping.index(loc)][node_mapping.index(m)]
            if arrival1 > 1:
                best_score += best(arrival1-1,
                                    m, oth, map, open + [m], dist_matrix, node_mapping, hist + [[arrival1-1, m]])
    if best_score == []:
        return [hist]
    return best_score

def get_score(hist, map):
    sum = 0
    for a in hist:
        sum += a[0]*map[a[1]]['rate']
    return sum

def get_score2(hist, hist2, map):
    scores = {}
    for a in hist:
        scores[a[1]] = a[0]*map[a[1]]['rate']
    for a in hist2:
        if a[1] in scores:
            scores[a[1]] = max(scores[a[1]], a[0]*map[a[1]]['rate'])
        else:
            scores[a[1]] = a[0]*map[a[1]]['rate']
    sum = 0
    for s in scores:
        sum += scores[s]
    return sum

def worker(paths1, paths2, v, map, prog):
    local = 0
    for p in paths1:
        for p2 in paths2:
            res = int(get_score2(p, p2, map))
            local = max(res, local)
        with prog.get_lock():
            prog.value += len(paths2)
    with v.get_lock():
        v.value = max(v.value, local)

def progress(p, v):
    while True:
        time.sleep(0.1)
        print(p.value/v)

def start(_, lines):
    map = {}
    node_mapping = []
    for l in lines:
        l = re.split('=|;| ', l.replace(',', ''))
        loc = l[1]
        rate = int(l[5])
        paths = dict([(p, 1) for p in l[11:]])
        map[loc] = {
            'rate': rate,
            'paths': paths
        }
    for l in map.copy():
        p = map[l]
        if l != 'AA':
            if(p['rate'] == 0):
                del map[l]
                for m in map:
                    if l in map[m]['paths']:
                        for path in p['paths']:
                            if path != m:
                                if path in map[m]['paths']:
                                    map[m]['paths'][path] = min(map[m]['paths'][path], map[m]['paths'][l] + p['paths'][path])
                                else:
                                    map[m]['paths'][path] = map[m]['paths'][l] + p['paths'][path]
                        del map[m]['paths'][l]
    for m in map:
        node_mapping.append(m)
    st = [[0]*len(map) for _ in range(0, len(map))]
    for l in map:
        ix = node_mapping.index(l)
        for p in map[l]['paths']:
            st[ix][node_mapping.index(p)] = map[l]['paths'][p]
    for i, r in enumerate(st):
        print(node_mapping[i], r)
    graph = csr_matrix(st)
    dist_matrix = dijkstra(csgraph=graph, directed=True)
    paths = best(26, 'AA', (26, 'AA'), map, [a for a in map if map[a]
          ['rate'] == 0], dist_matrix, node_mapping, [])
    
    scoresq = mp.Queue()
    processes = []
    res = mp.Value('i', 0)
    pr = mp.Value('i', 0)
    for c in range(0,12):
        p = mp.Process(target=worker, args=(paths[int(c*(len(paths)/12)):int((c+1)*(len(paths)/12))], paths, res, map, pr))
        p.start()
        processes.append(p)
        
    prog = mp.Process(target=progress, args=(pr, len(paths)*len(paths)))
    prog.start()

    for p in processes:
        p.join()

    prog.kill()
    
    print(res.value)
