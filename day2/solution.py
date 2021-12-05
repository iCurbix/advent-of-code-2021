from utils import read_input

inpt = read_input()

f, d = 0, 0

for a, b in inpt:
    if a == "forward":
        f += b
    elif a == "down":
        d += b
    elif a == "up":
        d -= b
    else:
        print("dupa")
print(f, d, f*d)


f, d, aim = 0, 0, 0

for a, b in inpt:
    if a == "forward":
        f += b
        d += aim * b
    elif a == "down":
        aim += b
    elif a == "up":
        aim -= b
    else:
        print("dupa")


print(f, d, f*d)

