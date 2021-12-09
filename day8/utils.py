import numpy as np


def read_input(filename: str = "input.txt") -> list[tuple[list[str], list[str]]]:
    out = []
    with open(filename, "r") as f:
        for line in f:
            a, b = line.split("|")
            out.append((a.split(), b.split()))
    return out
