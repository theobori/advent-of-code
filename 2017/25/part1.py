#!/usr/bin/env python

import os

with os.fdopen(0) as f:
    blocks = [line for line in f.read().split("\n\n") if line != ""]

block1 = blocks[0].split("\n")
curr_state = block1[0].rstrip(".").split()[-1]
steps = int(block1[1].split()[-2])
blocks = blocks[1:]
# state -> [(write_value, next_move, next_state), if zero
# (write_value, next_move, next_state)]  if one
rules = {}
for block in blocks:
    lines = block.splitlines()

    state = lines[0].rstrip(":")[-1]
    # if zero
    if_zero_write_value = int(lines[2][-2])
    if_zero_move = 1 if lines[3].rstrip(".").split()[-1] == "right" else -1
    if_zero_continue_state = lines[4][-2]
    # if one
    if_one_write_value = int(lines[6][-2])
    if_one_move = 1 if lines[7].rstrip(".").split()[-1] == "right" else -1
    if_one_continue_state = lines[8][-2]

    rules[state] = [
        (if_zero_write_value, if_zero_move, if_zero_continue_state),
        (if_one_write_value, if_one_move, if_one_continue_state),
    ]

tape = {}
cursor = 0
for step in range(steps):
    # 0 or 1
    # the needed rule
    curr_rule = rules[curr_state][tape.get(cursor, 0)]
    # turing machine context update
    tape[cursor] = curr_rule[0]
    cursor += curr_rule[1]
    curr_state = curr_rule[2]

ans = 0
for cell in tape.values():
    ans += cell

print(ans)
