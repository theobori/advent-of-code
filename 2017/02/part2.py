#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

ans = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                hi = numbers[i]
                lo = numbers[j]
            else:
                hi = numbers[j]
                lo = numbers[i]

            if hi % lo == 0:
                ans += hi // lo
                break
        else:
            continue
        break

print(ans)
