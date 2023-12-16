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
    hash = 0
    for t in token:
        hash += ord(t)
        hash *= 17
        hash %= 256
    return hash

def part1():
    tokens = data[0].split(',')
    return sum(map(computeHash, tokens))

def part2():
    boxes = [[] for i in range(256)]
    for t in data[0].split(','):
        split_char = '-' if '-' in t else '='
        label, fl = t.split(split_char)
        box_idx = computeHash(label)
        lens_idx = [i for i, (lens,_) in enumerate(boxes[box_idx]) if lens == label]
        if split_char == '-' and lens_idx:
            boxes[box_idx].pop(lens_idx[0])
        elif split_char == '=':
            if lens_idx:
                boxes[box_idx][lens_idx[0]] = (label, fl)
            else:
                boxes[box_idx].append((label,fl))
    return sum( \
        ib*sum(il*int(fl) for il, (_, fl) in enumerate(box,start=1)) \
        for ib, box in enumerate(boxes,start=1))

puzzle.answer_a = part1()
puzzle.answer_b = part2()
