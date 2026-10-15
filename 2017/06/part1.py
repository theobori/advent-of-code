#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    bank = [int(line) for line in f.read().strip().split()]

n = len(bank)
seen = set()
ans = 0

while True:
    t_bank = tuple(bank)
    if t_bank in seen:
        break
    seen.add(t_bank)

    # find max blocks
    max_blocks_value = float("-inf")
    max_blocks_index = float("-inf")
    for i, blocks in enumerate(bank):
        if blocks > max_blocks_value:
            max_blocks_value = blocks
            max_blocks_index = i

    # set to zero
    bank[max_blocks_index] = 0

    i = (max_blocks_index + 1) % n
    # rearrange
    while max_blocks_value > 0:
        bank[i] += 1
        max_blocks_value -= 1

        i = (i + 1) % n

    ans += 1

print(ans)
