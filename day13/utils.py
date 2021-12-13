import numpy as np


def read_input(filename: str = "input.txt") -> tuple[np.ndarray, list[tuple[str, int]]]:
    xs = []
    ys = []
    with open(filename, "r") as f:
        for l in f:
            if l == "\n":
                break
            x, y = l.strip().split(",")
            xs.append(int(x))
            ys.append(int(y))

        arr = np.zeros((max(xs)+1, max(ys)+1), dtype=bool)
        for x, y in zip(xs, ys):
            arr[x,y] = True
        folds = []
        for l in f:
            ax, v = l.strip().split()[-1].split("=")
            folds.append((ax, int(v)))

    return arr, folds
