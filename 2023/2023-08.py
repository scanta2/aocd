from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt

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

def part1(instr, first, end_fn):
    count = 0
    curr_pos = first
    stack = [curr_pos]
    while not end_fn(curr_pos):
        curr_pos = tree[curr_pos][moves[instr[0]]]
        stack.append(curr_pos)
        instr = instr[1:] + instr[:1]
        count += 1
    return count, stack
puzzle.answer_a, _ = part1(instr,'AAA', lambda x: x == 'ZZZ')

def part2(instr): 
    curr_pos = [p for p in tree if p[-1] == 'A']
    rems = []
    mods = []
    for c in curr_pos:
        count, stack = part1(copy(instr), c, lambda x: x[-1] == 'Z')
        next_pos = tree[stack[-1]][moves[instr[(count+1)%len(instr)]]]
        rems.append(stack.index(next_pos))
        mods.append(len(stack)-rems[-1])
    return crt(mods,rems)[-1]
puzzle.answer_b = part2(instr)
