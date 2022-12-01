import sys

calories = []
with open('01.in', 'r') as file:
    s = 0
    for line in file:
        line = line.strip()
        if line == "":
            calories.append(s)
            s = 0
        else: 
            s += int(line)
calories.sort()
print(sum(calories[-3:]))
