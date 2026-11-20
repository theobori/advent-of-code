#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    grid = [list(line) for line in f.read().splitlines() if len(line) > 0]

w = len(grid[0])
h = len(grid)

adjacent_deltas = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def get_adjacent_occupied_seat_amount(g, r, c):
    count = 0

    # rows
    for rr in range(r - 1, -1, -1):
        if g[rr][c] == "L":
            break
        elif g[rr][c] == "#":
            count += 1
            break
    for rr in range(r + 1, h):
        if g[rr][c] == "L":
            break
        elif g[rr][c] == "#":
            count += 1
            break
    # cols
    for cc in range(c - 1, -1, -1):
        if g[r][cc] == "L":
            break
        elif g[r][cc] == "#":
            count += 1
            break
    for cc in range(c + 1, w):
        if g[r][cc] == "L":
            break
        if g[r][cc] == "#":
            count += 1
            break
    # diag
    rr = r - 1
    cc = c + 1
    while rr >= 0 and cc < w:
        if g[rr][cc] == "L":
            break
        elif g[rr][cc] == "#":
            count += 1
            break
        rr -= 1
        cc += 1
    rr = r + 1
    cc = c - 1
    while rr < h and cc >= 0:
        if g[rr][cc] == "L":
            break
        elif g[rr][cc] == "#":
            count += 1
            break
        rr += 1
        cc -= 1
    # anti diag
    rr = r - 1
    cc = c - 1
    while rr >= 0 and cc >= 0:
        if g[rr][cc] == "L":
            break
        elif g[rr][cc] == "#":
            count += 1
            break
        rr -= 1
        cc -= 1
    rr = r + 1
    cc = c + 1
    while rr < h and cc < w:
        if g[rr][cc] == "L":
            break
        elif g[rr][cc] == "#":
            count += 1
            break
        rr += 1
        cc += 1

    return count


def is_seat_occupied(g, r, c):
    return get_adjacent_occupied_seat_amount(g, r, c) >= 5


prev = [list(line) for line in grid]

while True:
    changes = 0

    for r in range(h):
        for c in range(w):
            cell = grid[r][c]
            match cell:
                case "L":
                    if get_adjacent_occupied_seat_amount(prev, r, c) == 0:
                        grid[r][c] = "#"
                        changes += 1
                case "#":
                    if is_seat_occupied(prev, r, c):
                        grid[r][c] = "L"
                        changes += 1
                case ".":
                    pass
                case _:
                    raise ValueError()

    if changes == 0:
        break
    prev = [list(line) for line in grid]


ans = 0
for r in range(h):
    for c in range(w):
        ans += grid[r][c] == "#"

print(ans)
