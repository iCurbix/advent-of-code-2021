from collections import Counter
from itertools import permutations
from typing import Callable

import numpy as np

from utils import read_input


def do1():
    print(75*76/2)


def do2():
    (minx, maxx), (miny, maxy) = read_input()
    c = 0
    for x in range(maxx+1):
        for y in range(miny, -miny+1):
            xx, yy = 0, 0
            i = 0
            while xx < maxx + 1 and yy > miny - 1:
                xx += x - i if x - i > 0 else 0
                yy += y - i
                if minx <= xx <= maxx and miny <= yy <= maxy:
                    # print(x, y)
                    c += 1
                    break
                i += 1
    print(c)


do1()
print()
do2()
