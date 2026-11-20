#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

r = c = 0
ds = ((0, 1), (-1, 0), (0, -1), (1, 0))
d = 0

for line in lines:
    action = line[0]
    value = int(line[1:])

    match action:
        case "N":
            r += value
        case "S":
            r -= value
        case "E":
            c += value
        case "W":
            c -= value
        case "L":
            d = (d - (value // 90)) % 4
        case "R":
            d = (d + (value // 90)) % 4
        case "F":
            dr, dc = ds[d]
            r += dr * value
            c += dc * value
        case _:
            raise ValueError()

ans = abs(r) + abs(c)
print(ans)
