from collections import Counter
from itertools import permutations

import numpy as np

from utils import read_input

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
scores2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def do1():
    s = 0
    data = read_input()
    for line in data:
        c = []
        for ch in line:
            if ch in "([{<":
                c.append(ch)
                continue
            q = c.pop()
            if ch == ")" and q != "(":
                s += scores[ch]
                break
            if ch == "]" and q != "[":
                s += scores[ch]
                break
            if ch == "}" and q != "{":
                s += scores[ch]
                break
            if ch == ">" and q != "<":
                s += scores[ch]
                break

    print(s)


def do2():
    s = []
    data = read_input()
    for line in data:
        c = []
        bad = False
        for ch in line:
            if ch in "([{<":
                c.append(ch)
                continue
            q = c.pop()
            bad = True
            if ch == ")" and q != "(":
                break
            if ch == "]" and q != "[":
                break
            if ch == "}" and q != "{":
                break
            if ch == ">" and q != "<":
                break
            bad = False

        if not bad:
            ss = 0
            for ch in reversed(c):
                ss = ss * 5 + scores2[ch]
            s.append(ss)

    s.sort()
    print(s[len(s) // 2])

do1()
print()
do2()
