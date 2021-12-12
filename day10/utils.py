import numpy as np


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f]
