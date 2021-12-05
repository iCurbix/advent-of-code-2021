import numpy as np


def read_input(filename: str = "input.txt") -> tuple[list[int], list[np.ndarray]]:
    with open(filename, "r") as f:
        nums = [int(x) for x in f.readline().split(',')]
        arrs = []
        i = 0
        for x in f:
            for j, num in enumerate(int(a) for a in x.split()):
                arr[i][j] = num
            i += 1
            if x == '\n':
                try:
                    arrs.append(arr)
                except:
                    ...
                i = 0
                arr = np.zeros((5, 5))

    return nums, arrs
