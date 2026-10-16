#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    content_splitted = f.read().strip().split(",")
    lengths = [int(length.strip()) - 1 for length in content_splitted]


numbers = list(range(256))
n = len(numbers)
curr = 0
skip_size = 0

for length in lengths:
    # reverse
    end = (curr + length) % n

    l, r = curr, end
    count = length
    i = 0
    while i < (count + 1) // 2:
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l = (l + 1) % n
        r = (r - 1) % n
        i += 1

    # move the curr position
    curr = (curr + length + skip_size + 1) % n
    # increase the skip_size
    skip_size += 1

ans = numbers[0] * numbers[1]

print(ans)
