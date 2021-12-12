from collections import Counter
from itertools import permutations, product

import numpy as np

from utils import read_input


def do1():
    s = 0
    data = read_input()
    for i in range(100):
        data += 1
        iis, jjs = [], []
        while len(q:=np.argwhere(data>9)):
            for ii, jj in q:
                data[ii,jj] = 0
                iis.append(ii)
                jjs.append(jj)
                s += 1
                for iii, jjj in product([-1,0,1], repeat=2):
                    if ii+iii < 0 or jj + jjj < 0:
                        continue
                    try:
                        data[ii+iii, jj+jjj] += 1
                    except:
                        ...
        data[iis, jjs] = 0

    print(s)


def do2():
    data = read_input()
    for i in range(9999):
        data += 1
        iis, jjs = [], []
        while len(q:=np.argwhere(data>9)):
            for ii, jj in q:
                data[ii,jj] = 0
                iis.append(ii)
                jjs.append(jj)
                for iii, jjj in product([-1,0,1], repeat=2):
                    if ii+iii < 0 or jj + jjj < 0 or (iii == 0 and jjj == 0):
                        continue
                    try:
                        data[ii+iii, jj+jjj] += 1
                    except:
                        ...
        data[iis, jjs] = 0
        if data.sum() == 0:
            print(i+1)
            return


do1()
print()
do2()
