import sys

def prio(c):
    c = ord(c)
    if ord('a') <= c <= ord('z'):
        return 1+c-ord('a')
    else:
        return 27 + c - ord('A')

total = 0
for line in sys.stdin:
    line = line.lstrip()
    n = len(line)//2
    s = set(line[:n]) & set(line[n:])
    c = s.pop()
    p = prio(c)
    total += p
print(total)
