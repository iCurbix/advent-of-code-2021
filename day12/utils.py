from collections import defaultdict

import numpy as np


def read_input(filename: str = "input.txt") -> dict[str, list[str]]:
    d = defaultdict(list)
    with open(filename, "r") as f:
        for l in f:
            a, b = l.strip().split("-")
            if a != "end" and b != "start":
                d[a].append(b)
            if a != "start" and b != "end":
                d[b].append(a)
    return d
