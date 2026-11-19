#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

h = len(lines)
w = len(lines[0])


def get_encountered_trees_amount(dr, dc):
    r = c = 0
    ans = 0
    while r < h:
        ans += lines[r][c] == "#"
        c = (c + dc) % w
        r += dr

    return ans


slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

ans = 1
for dc, dr in slopes:
    ans *= get_encountered_trees_amount(dr, dc)

print(ans)
