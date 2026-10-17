#!/usr/bin/env python

import os

from collections import deque

with os.fdopen(0) as f:
    base_key = f.read().strip()


def compute_knot_hash(bytes_arr):
    lengths = [ord(byte) - 1 for byte in bytes_arr] + [16, 30, 72, 46, 22]

    numbers = list(range(256))
    n = len(numbers)
    curr = 0
    skip_size = 0

    for _ in range(64):
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

    ans = ""
    for i in range(0, 256, 16):
        number = numbers[i]
        for j in range(i + 1, i + 16):
            number ^= numbers[j]

        ans += f"{number:02x}"

    return ans


grid = []
for i in range(128):
    key = base_key + "-" + str(i)

    knot_hash = compute_knot_hash(key)
    bits = ""
    for one_digit_hex in knot_hash:
        binary_repr = bin(int(one_digit_hex, 16))[2:]
        n = len(binary_repr)
        if n < 4:
            binary_repr = ("0" * (4 - n)) + binary_repr

        bits += binary_repr

    grid.append(list(bits))

ans = 0
n = m = len(grid)
# instead I could save every "1" positions in a list to avoid to have a time complexity of O(n*m) -> O(n^2)
# But I dont' care for the moment
for r in range(n):
    for c in range(m):
        if grid[r][c] != "1":
            continue

        grid[r][c] = "#"
        st = deque([(r, c)])
        while st:
            rr, cc = st.pop()
            for dr, dc in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ):
                nr, nc = rr + dr, cc + dc

                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue

                if grid[nr][nc] == "1":
                    st.append((nr, nc))
                    grid[nr][nc] = "#"

        ans += 1

print(ans)
