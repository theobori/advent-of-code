#!/usr/bin/env pypy

import os

from collections import defaultdict, deque

with os.fdopen(0) as f:
    lines = f.read().strip().splitlines()

graph = defaultdict(list)

for line in lines:
    left, right = line.split(" <-> ")
    graph[left] = right.split(", ")

q = deque(["0"])
seen = {"0"}
while q:
    node = q.popleft()

    neighbors = graph[node]
    for neighbor in neighbors:
        if neighbor not in seen:
            q.append(neighbor)
            seen.add(neighbor)


ans = len(seen)
print(ans)
