# Ez pc

def start(line, lines):
    file = [(i, int(f)*811589153) for i, f in enumerate(lines)]
    mixed = file.copy()
    for i in range(0, 10):
        for l in file:
            currIdx = mixed.index(l)
            newIdx = currIdx + l[1]
            del mixed[currIdx]
            if newIdx % len(mixed) == 0:
                mixed.append(l)
            else:
                mixed.insert(newIdx % len(mixed), l)
    unencrypted = [l[1] for l in mixed]

    idx0 = unencrypted.index(0)
    c1, c2, c3 = unencrypted[(idx0 + 1000) % len(unencrypted)], unencrypted[(
        idx0 + 2000) % len(unencrypted)], unencrypted[(idx0 + 3000) % len(unencrypted)],

    print(sum([c1,c2,c3]))
