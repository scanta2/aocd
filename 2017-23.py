from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict
import queue
puzzle = Puzzle(year=2017,day=23)
lines = puzzle.input_data.split('\n')

registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
jump = 0
mul = 0

def solve(part):
    registers = defaultdict(int)
    registers['a'] = part - 1
    interpret = lambda val: registers[val] if val.isalpha() else int(val)
    i = 0
    while i < 11:
        op, reg, val = lines[i].split()
        if op == 'set':
            registers[reg] = interpret(val)
        elif op == 'sub':
            registers[reg] -= interpret(val)
        elif op == 'mul':
            registers[reg] *= interpret(val)
        elif op == 'jnz':
            if interpret(reg) != 0:
                i += interpret(val)
                continue
        i += 1

    if part == 1:
        return (registers['b'] - registers['e']) * (registers['b'] - registers['d'])
    else:
        nonprimes = 0
        for b in range(registers['b'], registers['c']+1, 17):
            if any(b % d == 0 for d in range(2, int(b**0.5))):
                nonprimes += 1
        return nonprimes

print(solve(part=2))