#!/usr/bin/env pypy

import os
import math

with os.fdopen(0) as f:
    steps = int(f.read().strip())

n = int(math.sqrt(steps)) + 5
grid = [[0] * n for _ in range(n)]

r, c = n // 2, n // 2
start_r, start_c = r, c

step = 1
offset = 1
grid[r][c] = step

while step < steps:
    # go right
    end_step = step + offset
    while step < steps and step < end_step:
        step += 1
        c += 1
        grid[r][c] = step

    # go up
    end_step = step + offset
    while step < steps and step < end_step:
        step += 1
        r -= 1
        grid[r][c] = step

    offset += 1

    # go left
    end_step = step + offset
    while step < steps and step < end_step:
        step += 1
        c -= 1
        grid[r][c] = step

    # go left
    end_step = step + offset
    while step < steps and step < end_step:
        step += 1
        r += 1
        grid[r][c] = step

    offset += 1


def get_manhattan_distance(xb, xa, yb, ya):
    return abs(xb - xa) + abs(yb - ya)


ans = get_manhattan_distance(start_c, c, start_r, r)

print(ans)
