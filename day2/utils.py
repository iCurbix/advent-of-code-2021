def read_input(filename: str = "input.txt"):
    out = []
    with open(filename, "r") as f:
        for x in f:
            a = x.split()
            out.append([a[0], int(a[1])])
    return out
