#!/usr/bin/env pypy

import os

from collections import defaultdict, deque

with os.fdopen(0) as f:
    lines = f.read().strip().splitlines()

graph = defaultdict(list)

for line in lines:
    left, right = line.split(" <-> ")
    graph[left] = right.split(", ")

ans = 0
seen = set()
for program in graph:
    if program in seen:
        continue

    q = deque([program])
    while q:
        node = q.popleft()

        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in seen:
                q.append(neighbor)
                seen.add(neighbor)

    ans += 1

print(ans)
