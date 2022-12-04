import sys

class Range():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def __contains__(self, other):
        return self.x >= other.x and self.y <= other.y

def rangify(s):
    a, b = s.split('-')
    return Range(int(a), int(b))

total = 0
for line in sys.stdin:
    parts = line.rstrip().split(',')
    r1 = rangify(parts[0])
    r2 = rangify(parts[1])
    total += int(r1 in r2 or r2 in r1)

print(total)

