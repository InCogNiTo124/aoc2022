import sys

with open('01.in', 'r') as file:
    M = -float("inf")
    s = 0
    for line in file:
        line = line.strip()
        if line == "":
            if s > M:
                M = s
            s = 0
        else: 
            s += int(line)
print(M)
