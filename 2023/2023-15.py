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

day = 15
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.example[0].input_data.split('\n')

def computeHash(token):
    current_value = 0
    for t in token:
        current_value += ord(t)
        current_value *= 17
        current_value %= 256
    return current_value

def part1():
    tokens = data[0].split(',')
    return sum(computeHash(t) for t in tokens)

def part2():
    boxes = [[] for i in range(256)]
    for t in data[0].split(','):
        split_char = '-' if '-' in t else '='
        label, fl = t.split(split_char)
        box_idx = computeHash(label)
        lens_idx = [i for i, (lens,_) in enumerate(boxes[box_idx]) if lens == label]
        if split_char == '-' and lens_idx:
            boxes[box_idx] = boxes[box_idx][:lens_idx[0]] + boxes[box_idx][lens_idx[0]+1:]
        elif split_char == '=':
            if lens_idx:
                boxes[box_idx][lens_idx[0]] = (label, fl)
            else:
                boxes[box_idx].append((label,fl))
    return sum( \
        (ib+1)*sum((il+1)*int(fl) for il, (_, fl) in enumerate(box)) \
        for ib, box in enumerate(boxes))

puzzle.answer_a = part1()
puzzle.answer_b = part2()
