#!/usr/bin/env python

import os

from collections import defaultdict

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if line != ""]

registers = defaultdict(int)

for line in lines:
    register, op_code, op_code_arg, _if, cond_op_left, cond_op, cond_op_right = (
        line.split()
    )

    cond_op_res: bool
    cond_op_left_register = registers[cond_op_left]
    cond_op_right_value = int(cond_op_right)
    match cond_op:
        case "<":
            cond_op_res = cond_op_left_register < cond_op_right_value
        case "<=":
            cond_op_res = cond_op_left_register <= cond_op_right_value
        case ">":
            cond_op_res = cond_op_left_register > cond_op_right_value
        case ">=":
            cond_op_res = cond_op_left_register >= cond_op_right_value
        case "==":
            cond_op_res = cond_op_left_register == cond_op_right_value
        case "!=":
            cond_op_res = cond_op_left_register != cond_op_right_value
        case _:
            raise ValueError("Invalid conditional operator")

    if cond_op_res:
        match op_code:
            case "inc":
                registers[register] += int(op_code_arg)
            case "dec":
                registers[register] -= int(op_code_arg)
            case _:
                raise ValueError("Invalid register operator")

ans = max(registers.values())

print(ans)
