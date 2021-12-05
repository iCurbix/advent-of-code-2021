import numpy as np

from utils import read_input


def do1():
    data = read_input()
    board = np.zeros((1000, 1000))
    for x in data:
        if x[0][0] == x[1][0]:
            mi, ma = (x[0][1], x[1][1]) if x[0][1] < x[1][1] else (x[1][1], x[0][1])
            for y in range(mi, ma+1):
                board[x[0][0],y] += 1
        elif x[0][1] == x[1][1]:
            mi, ma = (x[0][0], x[1][0]) if x[0][0] < x[1][0] else (x[1][0], x[0][0])
            for xx in range(mi, ma + 1):
                board[xx, x[0][1]] += 1
        else:
            continue
    print(board[board>1].size)


def do2():
    data = read_input()
    board = np.zeros((1000, 1000))
    for x in data:
        if x[0][0] == x[1][0]:
            mi, ma = (x[0][1], x[1][1]) if x[0][1] < x[1][1] else (x[1][1], x[0][1])
            for y in range(mi, ma + 1):
                board[x[0][0], y] += 1
        elif x[0][1] == x[1][1]:
            mi, ma = (x[0][0], x[1][0]) if x[0][0] < x[1][0] else (x[1][0], x[0][0])
            for xx in range(mi, ma + 1):
                board[xx, x[0][1]] += 1
        else:
            dx = x[0][0] - x[1][0]
            dy = x[0][1] - x[1][1]
            if abs(dx) == abs(dy):
                minx, maxx = (x[0][0], x[1][0]) if x[0][0] < x[1][0] else (x[1][0], x[0][0])
                miny, maxy = (x[0][1], x[1][1]) if x[0][1] < x[1][1] else (x[1][1], x[0][1])
                for i in range(abs(dx) + 1):
                    xx = minx + i
                    y = miny + i if dy * dx > 0 else maxy - i
                    board[xx,y] += 1

    print(board[board > 1].size)


do1()
print()
do2()