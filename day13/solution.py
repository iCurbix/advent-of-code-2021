from collections import Counter
from itertools import permutations

import numpy as np
import matplotlib.pyplot as plt

from utils import read_input


def fold_x(a: np.ndarray, x: int) -> np.ndarray:
    q = a[:x, :]
    b = np.flip(a[x+1:,:], 0)
    if len(b) < len(q):
        q[-len(b):, :] += b
        return q
    else:
        b[-len(q):, :] += q
        return b


def fold_y(a: np.ndarray, y: int) -> np.ndarray:
    q = a[:, :y]
    b = np.flip(a[:,y+1:], 1)
    if len(b[0]) < len(q[0]):
        q[:, -len(b[0]):] += b
        return q
    else:
        b[:, -len(q[0]):] += q
        return b


def fold(a: np.ndarray, ax: str, val: int) -> np.ndarray:
    if ax == "x":
        return fold_x(a, val)
    return fold_y(a, val)


def do1():
    board, folds = read_input()
    print(fold(board, *folds[0]).sum())


def do2():
    board, folds = read_input()
    for ax, v in folds:
        board = fold(board, ax, v)
    plt.imshow(board.transpose())
    plt.show()


do1()
print()
do2()
