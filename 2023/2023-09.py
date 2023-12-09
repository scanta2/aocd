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
        seq = []
        new_line = [int(i) for i in line.split(' ')]
        if flip_input:
            new_line = new_line[::-1]
        seq.append(new_line)
        while any(i != 0 for i in seq[-1]):
            seq.append([seq[-1][j]-seq[-1][j-1] for j in range(1,len(seq[-1]))])
        return sum(seq[-i-1][-1] for i in range(1,len(seq)))
    return sum(solve_line(line) for line in data)

puzzle.answer_a = solve(False)
puzzle.answer_b = solve(True)
