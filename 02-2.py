choices = ['A', 'B', 'C']
points = {'A': 1, 'B': 2, 'C': 3}

total = 0
with open('02.in') as file:
    score = 0
    for line in file:
        x1, x2 = line.rstrip().split()
        r = choices[
            (choices.index(x1) + (-1 if x2 == 'X' else 0 if x2 == 'Y' else 1))%3
        ]
        score += points[r]
        score += 0 if x2 == 'X' else 3 if x2 == 'Y' else 6
        total += score
        score = 0

print(total)
