#!/usr/bin/env python

import os

from collections import defaultdict

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]


graph = defaultdict(list)
for line in lines:
    parent, children_str = line.split(" bags contain ")
    for child_str in children_str.split(", "):
        child = child_str.removesuffix(".").removesuffix(" bags").removesuffix(" bag")
        if child == "no other":
            bag_name = None
            amount = 0
        else:
            l, bag_name = child.split(" ", 1)
            amount = int(l)

        graph[parent].append((bag_name, amount))


def dfs(name):
    ans = 1

    children = graph[name]
    for child, amount in children:
        ans += dfs(child) * amount

    return ans


ans = dfs("shiny gold") - 1
print(ans)
