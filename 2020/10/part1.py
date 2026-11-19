#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    adapters = [int(line) for line in f.read().splitlines() if len(line) > 0]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

diffs = {}
n = len(adapters)
for i in range(1, n):
    diff = adapters[i] - adapters[i - 1]
    diffs[diff] = diffs.get(diff, 0) + 1

ans = diffs[1] * diffs[3]
print(ans)
