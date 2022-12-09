import sys
import copy
import itertools as it

grid = [list(map(int, line.rstrip())) for line in sys.stdin]
N, M = len(grid), len(grid[0])
def scenic_score(grid, i, j):
    #   U
    #  LxR
    #   D
    #
    item = grid[i][j]
    N, M = len(grid), len(grid[0])
    total = 1

    # D
    ii = 1
    for ii in range(1, N-i):
        if grid[i+ii][j] >= item:
            break
    total *= ii

    # U
    ii = 1
    for ii in range(1, i+1):
        if grid[i-ii][j] >= item:
            break
    total *= ii

    # L
    jj = 1
    for jj in range(1, j+1):
        if grid[i][j-jj] >= item:
            break
    total *= jj

    # R
    jj = 1
    for jj in range(1, M-j):
        if grid[i][j+jj] >= item:
            break
    total *= jj

    return total

print(max(scenic_score(grid, i, j) for i, j in it.product(range(1, N), range(1, M))))
