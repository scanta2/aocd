from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import networkx as nx

day = 11
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

height = len(data)
width = len(data[0])
galaxies = [(i,j) for i,j in product(range(height), range(width))\
            if data[i][j] == '#']

def solve(mult):
    vert_mult = [mult if set(line) == {'.'} else 1 for line in data]
    horz_mult = [mult if set(line) == {'.'} else 1 for line in zip(*data)]
    res = 0
    for i, gal in enumerate(galaxies):
        for other in galaxies[i+1:]:
            minv, maxv = min(gal[0], other[0]), max(gal[0], other[0])
            res += sum(vert_mult[minv+1:maxv+1])
            minh, maxh = min(gal[1], other[1]), max(gal[1], other[1])
            res += sum(horz_mult[minh+1:maxh+1])
    return res
puzzle.answer_a = solve(2)
puzzle.answer_b = solve(1000000)