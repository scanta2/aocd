from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy

day = 8
year = 2023

puzzle = Puzzle(day=day, year=year)
instr, map = puzzle.input_data.split('\n\n')

moves = {'R': 1, 'L': 0}
tree = dict()
for line in map.split('\n'):
    l = line.split(' = ')
    ll, rr = l[1].split(', ')
    ll = ll[1:]
    rr = rr[:-1]
    tree[l[0]] = (ll, rr)

# instr, map = puzzle.examples[0].input_data.split('\n\n')

def part1(instr, first, last=None):
    count = 0
    curr_pos = first
    while (last is not None and curr_pos != last) or curr_pos[-1] != 'Z':
        curr_pos = tree[curr_pos][moves[instr[0]]]
        instr = instr[1:] + instr[:1]
        count += 1
    return count
puzzle.answer_a = part1(instr,'AAA','ZZZ')

def part2(instr): 
    curr_pos = [p for p in tree if p[-1] == 'A']
    return lcm(*(part1(copy(instr), c) for c in curr_pos))
puzzle.answer_b = part2(instr)
