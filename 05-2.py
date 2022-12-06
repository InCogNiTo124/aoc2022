import sys
from collections import deque
from string import ascii_uppercase
import re

UPPER = set(ascii_uppercase)
PATTERN = re.compile(r'move (\d+) from (\d+) to (\d+)')

stacks = []

def parse(match):
    return int(match.group(1)), int(match.group(2))-1, int(match.group(3))-1

# crates parsing
for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    line = line.replace('[', ' ').replace(']', ' ')
    crates = line[1::4]
    if len(stacks) == 0:
        for _ in range(len(crates)):
            stacks.append(deque())
    for i, t in enumerate(crates):
        if t in UPPER:
            stacks[i].appendleft(t)

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    match = PATTERN.match(line)
    count, src, dest = parse(match)
    temp = deque()
    for _ in range(count):
        temp.append(stacks[src].pop())
    while len(temp) > 0:
        stacks[dest].append(temp.pop())

print(''.join(t[-1] for t in stacks))

