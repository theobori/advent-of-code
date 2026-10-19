#!/usr/bin/env python

import os

from collections import defaultdict

with os.fdopen(0) as f:
    lines = [line for line in f.read().strip().splitlines()]


class VM:
    def __init__(self, lines):
        self.__lines = lines
        self.__n = len(lines)
        self.reset()

    def reset(self):
        self.__registers = defaultdict(int)
        self.__index = 0
        self.mul_counter = 0

    def step(self):
        if self.__index >= self.__n:
            return True

        arr = self.__lines[self.__index].split()
        instruction = arr[0]
        x = arr[1]
        if len(arr) > 2:
            y = arr[2]
        else:
            y = ""

        if not y.lstrip("-").isdigit():
            y = self.__registers[y]

        y = int(y)

        match instruction:
            case "set":
                self.__registers[x] = y
            case "sub":
                self.__registers[x] -= y
            case "mul":
                self.__registers[x] *= y
                self.mul_counter += 1
            case "jnz":
                if x.lstrip("-").isdigit():
                    x = int(x)
                else:
                    x = self.__registers[x]

                if x != 0:
                    self.__index += y
                    return False

        self.__index += 1

        return False

    def run(self, reset=True):
        if reset:
            self.reset()

        while True:
            if self.step():
                break


vm = VM(lines)
vm.run()

ans = vm.mul_counter
print(ans)
