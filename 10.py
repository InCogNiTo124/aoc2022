import sys

X = 1
add = False
s = 0
for i in range(1, 221):
    if i in range(20, 221, 40):
        s += X*i
    if add:
        X += v
        add = False
    else:
        line = next(sys.stdin).rstrip()
        if line.startswith("addx"):
            _, v = line.split(' ')
            v = int(v)
            add = True

print(s)
