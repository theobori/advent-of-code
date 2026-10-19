#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

h = {}
n = len(lines)
m = len(lines[0])
for r in range(n):
    for c in range(m):
        h[(r, c)] = lines[r][c] == "#"

r, c = n // 2, m // 2
dir = 0
#           ^       >       v        <
deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 0
for _ in range(10000):
    if not (r, c) in h:
        h[(r, c)] = False

    state = h[(r, c)]
    if state is True:
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

    if state is False:
        h[(r, c)] = True
        ans += 1
    else:
        h[(r, c)] = False

    dr, dc = deltas[dir]
    r += dr
    c += dc

print(ans)
