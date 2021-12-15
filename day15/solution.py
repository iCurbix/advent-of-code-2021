from collections import Counter
from itertools import permutations

import numpy as np

from utils import read_input


def check_and_fill(board, dists, dis, pos, x, y):
    if (q := (dis + board[x, y])) < dists[x, y]:
        dists[x, y] = q
        pos.append((x, y))

def do1():
    board = read_input()
    dists = np.full_like(board, 99999)
    dists[0, 0] = 0
    pos = [(0, 0)]
    maxx = len(board[0]) - 1
    maxy = len(board) - 1
    while pos:
        npos = []
        for x, y in pos:
            dis = dists[x, y]
            if x > 0:
                check_and_fill(board, dists, dis, npos, x-1, y)
            if y > 0:
                check_and_fill(board, dists, dis, npos, x, y-1)
            if x < maxx:
                check_and_fill(board, dists, dis, npos, x+1, y)
            if y < maxy:
                check_and_fill(board, dists, dis, npos, x, y+1)
        pos = npos
    print(dists)



def do2():
    data = read_input()
    dimx, dimy = data.shape
    board = np.zeros((dimx * 5, dimy * 5))
    for i in range(5):
        for j in range(5):
            ins = data.copy()
            for q in range(i+j):
                ins = (ins + 1) % 10
                ins[ins==0] = 1
            board[i*dimx:(i+1)*dimx, j*dimy:(j+1)*dimy] = ins

    dists = np.full_like(board, 99999)
    dists[0, 0] = 0
    pos = [(0, 0)]
    maxx = len(board[0]) - 1
    maxy = len(board) - 1
    while pos:
        npos = []
        for x, y in pos:
            dis = dists[x, y]
            if x > 0:
                check_and_fill(board, dists, dis, npos, x - 1, y)
            if y > 0:
                check_and_fill(board, dists, dis, npos, x, y - 1)
            if x < maxx:
                check_and_fill(board, dists, dis, npos, x + 1, y)
            if y < maxy:
                check_and_fill(board, dists, dis, npos, x, y + 1)
        pos = npos
    print(dists)

do1()
print()
do2()
