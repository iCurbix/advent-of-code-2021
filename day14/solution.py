from collections import Counter
from itertools import permutations

import numpy as np

from utils import read_input


def do1():
    a, d = read_input()
    for i in range(10):
        na = ""
        for l1, l2 in zip(a, a[1:]):
            na += l1 + d[l1+l2]
        a = na + l2
    c = Counter(a)
    q = c.most_common()
    print(q[0][1] - q[-1][1])


def do2():
    a, d = read_input()
    pc = Counter(x+y for x, y in zip(a, a[1:]))
    c = Counter(a)
    for i in range(40):
        npc = Counter()
        for k, v in pc.items():
            ins = d[k]
            npc[k[0]+ins] += v
            npc[ins+k[1]] += v
            c[ins] += v
        pc = npc

    q = c.most_common()
    print(q[0][1] - q[-1][1])

do1()
print()
do2()
