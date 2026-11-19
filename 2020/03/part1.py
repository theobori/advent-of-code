#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

r = c = 0
h = len(lines)
w = len(lines[0])

ans = 0
while r < h:
    ans += lines[r][c] == "#"
    c = (c + 3) % w
    r += 1

print(ans)
