#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    content = f.read().strip()


n = len(content)
i = 0
groups = 0
garbage = 0
ans = 0
while i < n:
    ch = content[i]

    match ch:
        case "<":
            garbage += 1
        case ">":
            garbage = 0
        case "{":
            if garbage == 0:
                groups += 1
        case "}":
            if garbage == 0:
                ans += groups
                groups -= 1
        case "!":
            i += 1
    i += 1

print(ans)
