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
    for dr, dc in adjacent_deltas:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue

        count += g[nr][nc] == "#"

    return count


def is_seat_occupied(g, r, c):
    return get_adjacent_occupied_seat_amount(g, r, c) >= 4


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
