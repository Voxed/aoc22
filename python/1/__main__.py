import numpy as np
import itertools as it
elfs = np.sort(np.array(list(it.zip_longest(*[f.strip().split('\n') for f in open('input.txt').read().split('\n\n')], fillvalue=0))).T.astype(int).sum(axis=1))
print(elfs[-1], elfs[-3:].sum())
