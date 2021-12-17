import numpy as np


def read_input(filename: str = "input.txt") -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


def read_ndarray2(filename: str = "input.txt") -> np.ndarray:
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                out = np.zeros((len(line)-1, len(line)-1))
            out[i] = [int(x) for x in line if x != "\n"]
    return out


def read_ndarray(filename: str = "input.txt") -> np.ndarray:
    with open(filename, "r") as f:
        out = np.zeros((10, 10))
        for i, line in enumerate(f):
            out[i] = [int(x) for x in line if x != "\n"]
    return out
