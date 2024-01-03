from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt

day = 9
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')
# data = puzzle.examples[0].input_data.split('\n')

def solve(flip_input):
    def solve_line(line):
        seq = [list(map(int,line.split()))]
        if flip_input:
            seq[0] = seq[0][::-1]
        while set(seq[-1]) != {0}:
            seq.append([a-b for (a,b) in zip(seq[-1][1:], seq[-1][:-1])])
        return sum(s[-1] for s in seq)
    return sum(solve_line(line) for line in data)

puzzle.answer_a = solve(False)
puzzle.answer_b = solve(True)
