#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    offset = int(f.read().strip())

circular_buffer = [0]
curr = 0
for i in range(1, 2017 + 1):
    # apply offset
    curr = (curr + offset) % len(circular_buffer) + 1
    # insert
    circular_buffer.insert(curr, i)

ans = circular_buffer[(curr + 1) % len(circular_buffer)]
print(ans)
