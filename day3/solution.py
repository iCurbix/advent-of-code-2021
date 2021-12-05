from utils import read_input

inpt = read_input()

counts = [[0, 0] for _ in range(len(inpt[0]))]

for a in inpt:
    for i, q in enumerate(a):
        counts[i][int(q)] += 1

res = ""
for c in counts:
    if c[0] > c[1]:
        res += "0"
    else:
        res += "1"

print(res, int(res, 2))
res2 = "111011100110"

aa = inpt.copy()
i = 0

while len(aa) != 1:
    c = [0, 0]
    for q in aa:
        c[int(q[i])] += 1
    p = "1"
    if c[0] > c[1]:
        p = "0"
    else:
        p = "1"
    aa = list(filter(lambda x: x[i] == p, aa))
    i += 1

print(aa, int(aa[0], 2))

aaa = inpt.copy()
i = 0

while len(aaa) != 1:
    c = [0, 0]
    for q in aaa:
        c[int(q[i])] += 1
    p = "0"
    if c[0] > c[1]:
        p = "1"
    else:
        p = "0"
    aaa = list(filter(lambda x: x[i] == p, aaa))
    i += 1

print(aaa, int(aaa[0], 2))

