from collections import Counter

from utils import read_input

from itertools import permutations

import numpy as np

data = read_input()


def hh(cp: list[str], cur: str) -> int:
    s = 0
    for q in data[cur]:
        if q == "end":
            s += 1
            continue
        if q.islower():
            if q in cp:
                continue
        cp.append(q)
        s += hh(cp, q)
        cp.pop()
    return s


def hh2(cp: list[str], cur: str, can_twice: bool) -> int:
    s = 0
    for q in data[cur]:
        ct = can_twice
        if q == "end":
            s += 1
            continue
        if q.islower():
            if q in cp:
                if not can_twice:
                    continue
                ct = False
        cp.append(q)
        s += hh2(cp, q, ct)
        cp.pop()
    return s


def do1():
    cur = "start"
    cp = ["start"]
    print(hh(cp, cur))


def do2():
    cur = "start"
    cp = ["start"]
    print(hh2(cp, cur, True))


do1()
print()
do2()
