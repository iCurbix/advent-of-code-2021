import numpy as np


def read_input(filename: str = "input.txt") -> list[int]:
    with open(filename, "r") as f:
        for line in f:
            return [int(x) for x in line.split(",")]
