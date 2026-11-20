#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

wr = 1
wc = 10
r = c = 0

for line in lines:
    action = line[0]
    value = int(line[1:])

    match action:
        case "N":
            wr += value
        case "S":
            wr -= value
        case "E":
            wc += value
        case "W":
            wc -= value
        case "L":
            for i in range(value // 90):
                wr, wc = wc, -wr
        case "R":
            for i in range(value // 90):
                wr, wc = -wc, wr
        case "F":
            r += value * wr
            c += value * wc
        case _:
            raise ValueError()

ans = abs(r) + abs(c)
print(ans)
