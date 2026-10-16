#!/usr/bin/env pypy
# For this problem, I had to read https://www.redblobgames.com/grids/hexagons

import os

with os.fdopen(0) as f:
    directions = f.read().strip().split(",")

"""
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
"""


deltas = {
    # q, s, r
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}


def cube_distance(q, r, s):
    return (abs(q) + abs(r) + abs(s)) / 2


q, s, r = 0, 0, 0
ans = 0
for direction in directions:
    delta = deltas[direction]

    q += delta[0]
    s += delta[1]
    r += delta[2]

ans = cube_distance(q, s, r)

print(ans)
