#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [lines for lines in f.read().splitlines() if len(lines) > 0]

ans = float("-inf")

for line in lines:
    row_seq = line[0:7]
    l = 0
    r = 127
    for ch in row_seq:
        mid = (l + r) // 2
        if ch == "F":
            r = mid - 1
        elif ch == "B":
            l = mid + 1
        else:
            raise ValueError()
    row = l

    col_seq = line[-3:]
    l = 0
    r = 7
    for ch in col_seq:
        mid = (l + r) // 2
        if ch == "L":
            r = mid - 1
        elif ch == "R":
            l = mid + 1
        else:
            raise ValueError()
    col = l

    ans = max(ans, row * 8 + col)

print(ans)
