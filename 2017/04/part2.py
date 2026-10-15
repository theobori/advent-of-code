#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

ans = 0
for line in lines:
    anagrams = set()
    words = line.split()

    freq_seen = set()
    for word in words:
        freq = [0] * 26
        for ch in word:
            freq[97 - ord(ch)] += 1

        static_freq = tuple(freq)
        if static_freq in freq_seen:
            break

        freq_seen.add(static_freq)
    else:
        ans += 1

print(ans)
