#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    offset = int(f.read().strip())

curr = 1
size = 1
ans = -1
for i in range(1, 50 * 10**6 + 1):
    if curr == 1:
        ans = i - 1
    curr = (curr + offset) % size + 1
    size += 1

print(ans)
