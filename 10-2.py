import sys

X = 1
add = False
for i in range(0, 250):
    print('#' if abs(i%40 - X) <= 1 else '.', end=('\n' if i%40 == 39 else ''))
    if add:
        X += v
        add = False
    else:
        line = next(sys.stdin).rstrip()
        if line.startswith("addx"):
            _, v = line.split(' ')
            v = int(v)
            add = True
