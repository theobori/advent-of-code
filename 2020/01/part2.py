#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    numbers = [int(line) for line in f.read().splitlines() if len(line) > 0]

n = len(numbers)
ans = 0
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if numbers[a] + numbers[b] + numbers[c] == 2020:
                ans = numbers[a] * numbers[b] * numbers[c]
                break
        else:
            continue
        break
    else:
        continue
    break

print(ans)
