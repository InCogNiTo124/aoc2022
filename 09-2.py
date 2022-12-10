import sys

class Position():
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        return

    def tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return str(self.name)

knots = [Position('H' if i == 0 else str(i)) for i in range(10)]
visited = set([knots[-1].tuple()])

def adjust_tail(tail, head):
    dx = abs(tail.x - head.x)
    dy = abs(tail.y - head.y)

    # 23232
    # 31113
    # 21.12
    # 31113
    # 23232
    if dx+dy < 2 or (dx+dy) == 2 and dx*dy != 0:
        # 1) the head is around the tail
        # do nothing as the head and tail touch
        pass
    elif dx + dy == 2 and dx*dy == 0 or dx == 2 and dy == 2:
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
    line = line.rstrip()
    direction, count = line.split(' ')
    count = int(count)
    for _ in range(count):
        match direction:
            case "R":
                knots[0].x += 1
            case "L":
                knots[0].x -= 1
            case "U":
                knots[0].y += 1
            case "D":
                knots[0].y -= 1
        for head, tail in zip(knots, knots[1:]):
            adjust_tail(tail, head)

        # the last one
        visited.add(tail.tuple()) 

print(len(visited))

