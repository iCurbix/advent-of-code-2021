import numpy as np


def read_input(filename: str = "input.txt") -> np.ndarray:
    with open(filename, "r") as f:
        out = np.zeros((100,100))
        for i, line in enumerate(f):
            out[i] = [int(x) for x in line if x != "\n"]
    return out
