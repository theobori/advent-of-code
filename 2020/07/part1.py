#!/usr/bin/env python

import os

from collections import defaultdict, deque

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]


# parent graph
graph = defaultdict(list)
for line in lines:
    parent, children_str = line.split(" bags contain ")
    for child_str in children_str.split(", "):
        child = child_str.removesuffix(".").removesuffix(" bags").removesuffix(" bag")
        if child == "no other":
            bag_name = None
        else:
            _, bag_name = child.split(" ", 1)

        graph[bag_name].append(parent)

ans = 0
q = deque(["shiny gold"])
seen = set(["shiny gold"])
while q:
    p = q.popleft()

    parents = graph[p]
    for parent in parents:
        if parent not in seen:
            q.append(parent)
            seen.add(parent)
            ans += 1

print(ans)
