#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    numbers = [int(line) for line in f.read().splitlines() if len(line) > 0]

n = len(numbers)

prefix_sum = [0] * n
prefix_sum[0] = numbers[0]
candidates = {prefix_sum[0] + 556543474: 0}
for r in range(1, n):
    prefix_sum[r] = prefix_sum[r - 1] + numbers[r]

    pf = prefix_sum[r]
    if pf in candidates:
        l = candidates[pf]
        if r - l + 1 >= 2:
            r = numbers[l + 1 : r + 1]
            ans = min(r) + max(r)
            break

    candidates[pf + 556543474] = r

print(ans)
