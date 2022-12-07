import sys

line = next(sys.stdin).rstrip()
for i, t in enumerate(zip(line, line[1:], line[2:], line[3:])):
    if len(set(t)) == 4:
        print(i+4)
        break
