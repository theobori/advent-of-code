#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

ans = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    ans += max(numbers) - min(numbers)

print(ans)
