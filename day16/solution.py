from collections import Counter
from itertools import permutations
from typing import Callable

import numpy as np

from utils import read_input


def h2b(s: str) -> str:
    return ''.join(np.binary_repr(int(x, 16), 4) for x in s)


def ver(s: str) -> tuple[int, str]:
    return int(s[:3], 2), s[3:]


def typ(s: str) -> tuple[int, str]:
    return int(s[:3], 2), s[3:]


def t4(s: str) -> tuple[int, str]:
    last = False
    num = ""
    while not last:
        last = not bool(int(s[0]))
        num += s[1:5]
        s = s[5:]
    return int(num, 2), s


def op_typ(s: str) -> tuple[int, str]:
    return int(s[0]), s[1:]


op_tf: dict[int, Callable[[str], tuple[int, str]]] = {
    0: lambda s: (int(s[:15], 2), s[15:]),
    1: lambda s: (int(s[:11], 2), s[11:]),
}

vvv = 0


class Packet:
    version: int
    t: int
    op_t: int
    op_ln: int
    val: int
    subpackets: list['Packet']

    def __init__(self):
        self.subpackets = []

    @classmethod
    def make_packet(cls, s: str) -> tuple['Packet', str]:
        p = Packet()

        v, s = ver(s)
        t, s = typ(s)

        global vvv
        vvv += v

        p.version = v
        p.t = t

        if t == 4:
            p.val, s = t4(s)
        else:
            p.op_t, s = op_typ(s)
            p.op_ln, s = op_tf[p.op_t](s)
            s = p.fill_subpackets(s)

        return p, s

    def fill_subpackets(self, s: str) -> str:
        if self.t == 4:
            return s

        if self.op_t == 0:
            ns = s[:self.op_ln]
            while len(ns) > 0:
                try:
                    p, ns = self.make_packet(ns)
                    self.subpackets.append(p)
                except IndexError:
                    break

            return s[self.op_ln:]

        if self.op_t == 1:
            for _ in range(self.op_ln):
                p, s = self.make_packet(s)
                self.subpackets.append(p)
            return s

    def eval(self) -> int:
        t = self.t
        if t == 4:
            return self.val

        if t == 0:
            return sum(x.eval() for x in self.subpackets)
        if t == 1:
            pro = 1
            for p in self.subpackets:
                pro *= p.eval()
            return pro
        if t == 2:
            return min(x.eval() for x in self.subpackets)
        if t == 3:
            return max(x.eval() for x in self.subpackets)
        if t == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        if t == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        if t == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())

def do1():
    s = h2b(read_input())
    p, s = Packet.make_packet(s)
    print(vvv)



def do2():
    s = h2b(read_input())
    p, s = Packet.make_packet(s)
    print(p.eval())


do1()
print()
do2()
