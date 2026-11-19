#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    numbers = [int(line) for line in f.read().splitlines() if len(line) > 0]

n = len(numbers)

sums = {}
for i in range(25):
    for j in range(i + 1, 25):
        s = numbers[i] + numbers[j]
        sums[s] = sums.get(s, 0) + 1

ans = 0

for i in range(25, n):
    if sums.get(numbers[i], 0) == 0:
        ans = numbers[i]
        break

    l = i - 25
    for j in range(l + 1, i):
        s = numbers[l] + numbers[j]
        sums[s] -= 1
        s = numbers[i] + numbers[j]
        sums[s] = sums.get(s, 0) + 1

print(ans)
