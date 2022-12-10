import sys

class Position():
    def __init__(self):
        self.x = 0
        self.y = 0
        return

    def tuple(self):
        return (self.x, self.y)

head = Position()
tail = Position()

visited = set([tail.tuple()])

def adjust_tail(tail, head):
    dx = abs(tail.x - head.x)
    dy = abs(tail.y - head.y)

    #  323
    # 31113
    # 21.12
    # 31113
    #  323
    if dx+dy < 2 or (dx+dy) == 2 and dx*dy != 0:
        # 1) the head is around the tail
        # do nothing as the head and tail touch
        pass
    elif dx + dy == 2 and dx*dy == 0:
        # 2) 
        # head moved on the same line. new position is the average of the two
        tail.x = (head.x + tail.x)//2
        tail.y = (head.y + tail.y)//2
    else:
        # 3)
        # the head moved away. tail goes diagonally
        # always one dimension of d=2 and the other one of d=1
        if dx == 2:
            tail.x = (head.x + tail.x)//2
            tail.y = head.y
        else:
            tail.x = head.x
            tail.y = (head.y + tail.y)//2

for line in sys.stdin:
    direction, count = line.rstrip().split(' ')
    count = int(count)
    for _ in range(count):
        match direction:
            case "R":
                head.x += 1
            case "L":
                head.x -= 1
            case "U":
                head.y += 1
            case "D":
                head.y -= 1
        adjust_tail(tail, head)
        visited.add(tail.tuple())

print(len(visited))
