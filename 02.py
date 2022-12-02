points = {'X': 1, 'Y': 2, 'Z': 3}

def result(other, me):
    o = ord('A') - ord(other)
    m = ord('X') - ord(me)
    if (m-o) % 3 == 0:
        return 3
    elif (m-o) % 3 == 1:
        return 0
    else:
        return 6

total = 0
with open('02.in') as file:
    score = 0
    for line in file:
        x1, x2 = line.rstrip().split()
        score += points[x2]
        score += result(x1, x2)
        total += score
        score = 0

print(total)
