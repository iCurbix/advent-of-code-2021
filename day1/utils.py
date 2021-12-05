def read_file_numbers(filename: str = "input.txt") -> list[int]:
    with open(filename, "r") as f:
        return [int(x) for x in f]
