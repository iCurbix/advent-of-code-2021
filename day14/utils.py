import numpy as np


def read_input(filename: str = "input.txt") -> tuple[str, dict[str, str]]:
    with open(filename, "r") as f:
        q = f.readline().strip()
        f.readline()
        d = {}
        for l in f:
            k, v = l.strip().split("->")
            d[k.strip()] = v.strip()
        return q, d
