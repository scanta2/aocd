from aocd.models import Puzzle
from itertools import combinations
import math
import string
import re

def part1(INPUT):
    memory = {}
    mask = ""
    mask_and = 0b1
    mask_or = 0b0

    for line in INPUT:
        if 'mask' in line:
            mask = '0b'+line[7:]
            mask_and = int(mask.replace('X','1'),2)
            mask_or = int(mask.replace('X','0'),2)
        else:
            loc, val = [int(x) for x in re.findall(r'\d+',line)]
            memory[loc] = (val & mask_and) | mask_or
    return sum(memory.values())

def part2(INPUT):
    memory = {}
    mask = ''
    factors = []
    for line in INPUT:
        if 'mask' in line:
            mask = line[7:]
            factors = [2**(35-x.start()) for x in re.finditer('X', mask)]   
            factors = [sum(x) for r in range(len(factors)+1) for x in combinations(factors,r)]
        else:
            loc, val = [int(x) for x in re.findall(r'\d+',line)]
            loc = [x for x in '{:36b}'.format(loc).replace(' ','0')]
            for i in range(36):
                if mask[i] == '1':
                    loc[i] = '1'
                elif mask[i] == 'X':
                    loc[i] = '0'
            loc = int(''.join(loc),2)
            for m in factors:
                memory[loc+m] = val

    return sum(memory.values())


PUZZLE = Puzzle(year=2020,day=14)
INPUT = PUZZLE.input_data.splitlines()
PUZZLE.answer_a = part1(INPUT)
PUZZLE.answer_b = part2(INPUT)