import sys

line = next(sys.stdin).rstrip()
for i, t in enumerate(zip(
    line,
    line[1:],
    line[2:],
    line[3:],
    line[4:],
    line[5:],
    line[6:],
    line[7:],
    line[8:],
    line[9:],
    line[10:],
    line[11:],
    line[12:],
    line[13:],
    )):
    if len(set(t)) == 14:
        print(i+14)
        break
