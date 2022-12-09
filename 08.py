import sys
import copy

grid = [list(map(int, line.rstrip())) for line in sys.stdin]
N, M = len(grid), len(grid[0])

def column(a, column, start=0, end=None):
    if end == None:
        end = len(a)
    return [grid[i][column] for i in range(start, end)]

def is_visible(grid, i, j):
    #   U
    #  LxR
    #   D
    #
    item = grid[i][j]

    # L
    if max(grid[i][:j], default=-float('inf')) < item:
        return True
    # R
    if max(grid[i][j+1:], default=-float('inf')) < item:
        return True
    # U
    if max(column(grid, j, end=i), default=-float('inf')) < item:
        return True
    # D
    if max(column(grid, j, start=i+1), default=-float('inf')) < item:
        return True

total = 0
for i in range(N):
    for j in range(M):
        if is_visible(grid, i, j):
            total += 1
print(total)
