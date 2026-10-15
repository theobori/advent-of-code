#!/usr/bin/env pypy

import os
import math

with os.fdopen(0) as f:
    steps = int(f.read().strip())

n = int(math.sqrt(steps)) + 5
grid = [[0] * n for _ in range(n)]


def compute_cell_value(grid, r, c):
    return (
        grid[r - 1][c]
        + grid[r + 1][c]
        + grid[r][c - 1]
        + grid[r][c + 1]
        + grid[r + 1][c + 1]
        + grid[r - 1][c - 1]
        + grid[r + 1][c - 1]
        + grid[r - 1][c + 1]
    )


def solve():
    step = 1
    offset = 1
    r, c = n // 2, n // 2
    grid[r][c] = step

    while True:
        # go right
        end_step = step + offset
        while step < end_step:
            step += 1
            c += 1
            grid[r][c] = compute_cell_value(grid, r, c)
            if grid[r][c] > steps:
                return grid[r][c]

        # go up
        end_step = step + offset
        while step < end_step:
            step += 1
            r -= 1
            grid[r][c] = compute_cell_value(grid, r, c)
            if grid[r][c] > steps:
                return grid[r][c]

        offset += 1

        # go left
        end_step = step + offset
        while step < end_step:
            step += 1
            c -= 1
            grid[r][c] = compute_cell_value(grid, r, c)
            if grid[r][c] > steps:
                return grid[r][c]

        # go left
        end_step = step + offset
        while step < end_step:
            step += 1
            r += 1
            grid[r][c] = compute_cell_value(grid, r, c)
            if grid[r][c] > steps:
                return grid[r][c]

        offset += 1


ans = solve()
print(ans)
