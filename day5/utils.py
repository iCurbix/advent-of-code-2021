import numpy as np


def read_input(filename: str = "input.txt") -> list[tuple[tuple[int, int]]]:
    data = []
    with open(filename, "r") as f:
        for line in f:
            xx = line.split("->")
            a = tuple(int(x) for x in xx[0].split(","))
            b = tuple(int(x) for x in xx[1].split(","))
            data.append((a, b))

    return data
