#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    print(
        sum(
            len(set(block.strip().replace("\n", "")))
            for block in f.read().split("\n\n")
            if len(block) > 0
        )
    )
