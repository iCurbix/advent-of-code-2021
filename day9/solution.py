from collections import Counter
from itertools import permutations

import numpy as np

from utils import read_input


def do1():
    data = read_input()
    mins = []
    for i in range(100):
        for j in range(100):
            b = []
            if i > 0:
                b.append(data[i-1, j])
            if j > 0:
                b.append(data[i, j-1])
            if i < 99:
                b.append(data[i+1, j])
            if j < 99:
                b.append(data[i, j+1])
            if np.all((a:=data[i, j]) < np.array(b)):
                mins.append(a + 1)
    print(sum(mins))




def do2():
    data = read_input()
    sizes = []
    mins = []
    for i in range(100):
        for j in range(100):
            b = []
            if i > 0:
                b.append(data[i - 1, j])
            if j > 0:
                b.append(data[i, j - 1])
            if i < 99:
                b.append(data[i + 1, j])
            if j < 99:
                b.append(data[i, j + 1])
            if np.all(data[i, j] < np.array(b)):
                mins.append((i, j))

    for i, j in mins:
        board = np.zeros((100, 100), dtype=bool)
        board2 = np.ones((100, 100), dtype=bool)
        board[i, j] = True

        while np.any(qq := np.logical_and(board, board2) == True):
            for ii, jj in np.argwhere(qq):
                a = data[ii, jj]
                if ii > 0 and a < data[ii - 1, jj] < 9:
                    board[ii - 1, jj] = True
                if jj > 0 and a < data[ii, jj - 1] < 9:
                    board[ii, jj - 1] = True
                if ii < 99 and a < data[ii + 1, jj] < 9:
                    board[ii + 1, jj] = True
                if jj < 99 and a < data[ii, jj + 1] < 9:
                    board[ii, jj + 1] = True

                board2[ii, jj] = False

        sizes.append(np.sum(board))

    aaa = 1
    for a in sorted(sizes)[-3:]:
        aaa *= a

    print(aaa)






do1()
print()
do2()
