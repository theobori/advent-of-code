#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

h = {}
n = len(lines)
m = len(lines[0])
for r in range(n):
    for c in range(m):
        h[(r, c)] = 2 if lines[r][c] == "#" else 0

r, c = n // 2, m // 2
dir = 0
#           ^       >       v        <
deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 0
for _ in range(10000000):
    if not (r, c) in h:
        h[(r, c)] = 0

    state = h[(r, c)]

    if state == 0:
        dir = (dir - 1) % 4
    elif state == 1:
        ans += 1
    elif state == 2:
        dir = (dir + 1) % 4
    elif state == 3:
        dir = (dir + 2) % 4

    h[(r, c)] = (state + 1) % 4

    dr, dc = deltas[dir]
    r += dr
    c += dc

print(ans)
