from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain, product
from collections import defaultdict
from copy import deepcopy

day = 6
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

# data=puzzle.examples[0].input_data.split('\n')

def part1():
    res = 1
    times = [int(s) for s in re.findall(r'\d+',data[0])]
    distances = [int(s) for s in re.findall(r'\d+',data[1])]
    for time, dist in zip(times, distances):
        res *= sum(1 for hold in range(0,time+1) if (time-hold)*hold > dist)
    print(res)
    return res
                
# part1()
puzzle.answer_a = part1()

def part2():
    time = int(''.join(re.findall(r'\d+',data[0])))
    dist = int(''.join(re.findall(r'\d+',data[1])))
    res = sum(1 for hold in range(0,time+1) if (time-hold)*hold > dist)
    print(res)
    return res

#  part2()
puzzle.answer_b = part2()
