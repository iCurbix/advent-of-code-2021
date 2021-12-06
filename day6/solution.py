from collections import Counter

import numpy as np

from utils import read_input


def do1():
    data = read_input()
    c = Counter(data)
    for j in range(80):
        c2 = Counter()
        c2[8] = c[0]
        c2[6] = c[0]
        for i in range(1, 9):
            c2[i - 1] += c[i]
        c = c2

    print(sum(c.values()))


def do2():
    data = read_input()
    c = Counter(data)
    for j in range(256):
        c2 = Counter()
        c2[8] = c[0]
        c2[6] = c[0]
        for i in range(1, 9):
            c2[i - 1] += c[i]
        c = c2

    print(sum(c.values()))


do1()
print()
do2()
