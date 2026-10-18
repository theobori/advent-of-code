#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    grid = [list(line) for line in f.read().splitlines() if line != ""]


n = len(grid)
m = len(grid[0])
start_r, start_c = 0, None
for c in range(m):
    if grid[0][c] == "|":
        start_c = c
        break

ans = ""
q = deque([(start_r, start_c, "down")])
seen = set()
while q:
    r, c, dir = q.popleft()
    if (r, c, dir) in seen or r < 0 or r >= n or c < 0 or c >= m:
        break

    seen.add((r, c, dir))

    cell = grid[r][c]

    if ord("A") <= ord(cell) <= ord("Z"):
        ans += cell
    elif cell == "+":
        if dir in {"down", "up"}:
            if grid[r][c - 1] == " ":
                dir = "right"
            else:
                dir = "left"
        elif dir in {"left", "right"}:
            if grid[r - 1][c] == " ":
                dir = "down"
            else:
                dir = "up"

    if dir == "down":
        r += 1
    elif dir == "up":
        r -= 1
    elif dir == "left":
        c -= 1
    elif dir == "right":
        c += 1

    q.append((r, c, dir))

print(ans)
