#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    numbers = [int(line) for line in f.read().splitlines() if len(line) > 0]

c = {}
ans = 0
for number in numbers:
    c[2020 - number] = number
    if number in c:
        ans = c[number] * number
        break

print(ans)
