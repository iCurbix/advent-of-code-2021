from collections import Counter
from itertools import permutations

import numpy as np

from utils import read_input


def do1():
    data = read_input()
    s = 0
    for _, a in data:
        s += len([x for x in a if len(x) in [2,3,4,7]])
    print(s)


class Lookup:
    def __init__(self):
        self.l = {}

    def put(self, k, v):
        self.l[frozenset(k)] = set(v)

    def get(self, k):
        return self.l[frozenset(k)]


def do2():
    snum = 0

    ll = Lookup()
    ll.put("abcefg", '0')
    ll.put("cf", '1')
    ll.put("acdeg", '2')
    ll.put("acdfg", '3')
    ll.put("bcdf", '4')
    ll.put("abdfg", '5')
    ll.put("abdefg", '6')
    ll.put("acf", '7')
    ll.put("abcdefg", '8')
    ll.put("abcdfg", '9')

    data = read_input()
    for a, bb in data:
        l = Lookup()
        l2 = Lookup()
        al = a + bb
        for x in al:
            if len(x) == 2:
                l2.put("cf", x)
            elif len(x) == 3:
                l2.put("acf", x)
            elif len(x) == 4:
                l2.put("bcdf", x)

        q = (l2.get("acf") - l2.get("cf")).pop()
        l.put(q, "a")
        l2.put("a", q)

        q = (l2.get("bdcf") - l2.get("cf"))
        l2.put("bd", q)

        q = (set("abcdefg") - l2.get("bdcf") - l2.get("a"))
        l2.put("eg", q)

        for x in al:
            if len(x) == 5:
                xx = set(x)
                q = l2.get("eg")
                if len(q.union(xx)) == len(xx):
                    xx -= q
                    xx -= l2.get("a")
                    c = xx - l2.get("bd")
                    d = xx - l2.get("cf")
                    b = l2.get("bd") - d
                    f = l2.get("cf") - c
                    l.put(b, "b")
                    l.put(c, "c")
                    l.put(d, "d")
                    l.put(f, "f")
                    l2.put("b", b)
                    l2.put("c", c)
                    l2.put("d", d)
                    l2.put("f", f)
                    break

        for x in al:
            if len(x) == 6:
                xx = set(x)
                q = l2.get("cf").union(l2.get("bd").union(l2.get("a")))
                if len(q.union(xx)) == len(xx):
                    g = xx - q
                    e = l2.get("eg") - g
                    l.put(e, "e")
                    l.put(g, "g")
                    break

        num = 0
        for i, d in enumerate(reversed(bb)):
            aa = set()
            for x in d:
                aa = aa.union(l.get(x))
            num += int(next(iter(ll.get(aa)))) * 10 ** i
        snum += num

    print(snum)


do1()
print()
do2()
