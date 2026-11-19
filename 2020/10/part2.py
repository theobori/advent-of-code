#!/usr/bin/env python

import os

from collections import defaultdict
from functools import cache

with os.fdopen(0) as f:
    adapters = [int(line) for line in f.read().splitlines() if len(line) > 0]

adapters.append(0)
end = max(adapters) + 3
adapters.append(end)
adapters.sort()

graph = defaultdict(list)
n = len(adapters)
for i in range(n):
    a = adapters[i]

    for j in range(i + 1, min(i + 4, n)):
        b = adapters[j]
        if b - a <= 3:
            graph[a].append(b)


@cache
def dp(adapter):
    ans = 0
    if adapter == end:
        return 1

    children = graph[adapter]
    for child in children:
        ans += dp(child)

    return ans


ans = dp(0)
print(ans)
