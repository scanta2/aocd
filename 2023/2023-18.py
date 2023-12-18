from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import functools

day = 18
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')
    
hex_to_dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

dirs = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

def shoelace(boundary):
    det = 0
    for i in range(len(boundary)-1):
        p1, p2 = boundary[i], boundary[i+1]
        det += (p1[0]*p2[1] - p2[0]*p1[1])
    return abs(det)

def solve(steps):
    boundary = [(0,0)]
    perimeter = 0
    for dir, num in steps:
        perimeter += num
        boundary.append(tuple(boundary[-1][i]+num*dir[i] for i in range(2)))
    inside = shoelace(boundary)
    return (perimeter + inside)//2 + 1

def part1():
    steps = []
    for line in data:
        dirL, num, _ = line.split(' ')
        dir = dirs[dirL]
        num = int(num)
        steps.append((dir, num))
    return solve(steps)

def part2():
    steps = []
    for line in data:
        _, _, instr = line.split(' ')
        instr = instr[2:-1]
        num = int(instr[0:-1],16)
        dirL = hex_to_dir[instr[-1]]
        dir = dirs[dirL]
        steps.append((dir, num))
    return solve(steps)

puzzle.answer_a = part1()
puzzle.answer_b = part2()