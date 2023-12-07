from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain, product
from collections import defaultdict
from copy import deepcopy

day = 3
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split('\n')

digits = string.digits

not_symbols = digits+'.'

# number_pos = defaultdict(set)

def part1():
    summation = 0

    for i, line in enumerate(data):
        iter = re.finditer(r'[0-9]+', line)
        indices = ((m.start(0), m.end(0)) for m in iter)
        for index in indices:

            xx = range(max(i-1,0),min(i+2,len(data)))
            y = (max(index[0]-1,0),min(index[1]+1,len(data)))
            check = ''
            for x in xx:
                check += data[x][y[0]:y[1]]
            if any(c not in not_symbols for c in check):
                summation += int(line[index[0]:index[1]])
    return summation

def part2():
    
    gear_ratios = defaultdict(list)

    for i, line in enumerate(data):
        iter = re.finditer(r'[0-9]+', line)
        indices = ((m.start(0), m.end(0)) for m in iter)
        for index in indices:
            number = int(line[index[0]:index[1]])
            xx = range(max(i-1,0),min(i+2,len(data)))
            y = (max(index[0]-1,0),min(index[1]+1,len(data)))
            for x in xx:
                check = data[x][y[0]:y[1]]
                if '*' in check:
                    star_locs = [i for i, e in enumerate(data[x][y[0]:y[1]]) if e == '*']
                    for sl in star_locs:
                        gear_ratios[(x,sl+y[0])].append(number)

    summation = 0
    for gr in gear_ratios.values():
        if len(gr) == 2:
            summation += prod(gr)
    print(summation)
    return summation

part2()






