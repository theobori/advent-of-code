#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    digits = f.read().strip()

ans = 0
offset = len(digits) // 2
for i, digit in enumerate(digits):
    prev = digits[i - offset]
    curr = digit

    if curr == prev:
        ans += int(curr)

print(ans)
