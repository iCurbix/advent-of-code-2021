from collections import Counter

import numpy as np

from utils import read_input


def err(data: np.ndarray, pos: int) -> int:
    return np.abs(data - pos).sum()


def err2(data: np.ndarray, pos: int) -> int:
    a = np.abs(data - pos)
    return np.sum(a * (a + 1) / 2)


def do1():
    data = read_input()
    data = np.array(data)
    me = float("inf")
    for i in range(data.min(), data.max()):
        e = err(data, i)
        me = e if e < me else me

    print(me)



def do2():
    data = read_input()
    data = np.array(data)
    me = float("inf")
    for i in range(data.min(), data.max()):
        e = err2(data, i)
        me = e if e < me else me

    print(me)



do1()
print()
do2()
