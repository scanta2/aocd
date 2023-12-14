from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations, starmap
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import networkx as nx
import functools

day = 13
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n\n')
else:
    data = puzzle.example[0].input_data.split('\n\n')

def score(grid, smudges):
    res = 0
    right = list(map(''.join, zip(*grid)))
    left = []
    while len(right) > 1:
        left.insert(0, right.pop(0))
        num_diffs = sum(sum(a != b for a,b in zip(aa,bb)) for aa,bb in zip(left, right))
        if num_diffs == smudges:
            res += len(left)

    bottom = list(map(''.join, grid))
    top = []
    while len(bottom) > 1:
        top.insert(0, bottom.pop(0))
        num_diffs = sum(sum(a != b for a,b in zip(aa,bb)) for aa,bb in zip(top, bottom))
        if num_diffs == smudges:
            res += len(top) * 100
    return res

def solve(smudges):
    grids = [[[c for c in line] for line in grid.splitlines()] for grid in data]
    return sum(score(grid, smudges) for grid in grids)

puzzle.answer_a = solve(0)
puzzle.answer_b = solve(1)
