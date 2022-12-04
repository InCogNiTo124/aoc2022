import sys
from functools import reduce

def prio(c):
    c = ord(c)
    if ord('a') <= c <= ord('z'):
        return 1+c-ord('a')
    else:
        return 27 + c - ord('A')

total = 0
ii = iter(sys.stdin)  # input iterator
for line in ii:
    lines = [line.rstrip(), next(ii).rstrip(), next(ii).rstrip()]
    s = reduce(set.intersection, map(set, lines))
    c = s.pop()
    p = prio(c)
    total += p
print(total)
