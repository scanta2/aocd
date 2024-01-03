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
import grid

day = 14
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')

def roll(grid):
    height = len(grid)
    width = len(grid[0])
    for c in range(width):
        for h in range(-height,0,1):
            if grid[h][c] == 'O':
                hh = h
                while hh > -height:
                    if grid[hh-1][c] == '.':
                        grid[hh-1][c], grid[hh][c] = grid[hh][c], grid[hh-1][c]
                        hh -= 1
                    else:
                        break
    return grid

def score(grid):
    return sum(-h*sum(c == 'O' for c in grid[h]) for h in range(-len(grid),0,1))

def part1():
    grid = []
    for line in data:
        grid.append([c for c in line])
    grid = roll(grid)
    return score(grid)
    
puzzle.answer_a = part1()

def part2():
    cycles = ['N','W','S','E']

    grid = []
    for line in data:
        grid.append([c for c in line])

    states = {}

    for c in range(1000000000):
        hash = ''.join((''.join(line) for line in grid))
        if hash in states:
            break
        roll_cycle = cycles[c%4]
        if roll_cycle == 'N':
            grid = roll(grid)
        elif roll_cycle == 'S':
            grid = roll(grid[::-1])
            grid = grid[::-1]
        elif roll_cycle == 'W':
            grid = list(zip(*grid[::-1]))
            grid = [list(c) for c in grid]
            grid = roll(grid)
            grid = list(zip(*grid))
            grid = [list(c) for c in grid[::-1]]
        else:
            grid = list(zip(*grid))
            grid = [list(c) for c in grid[::-1]]
            grid = roll(grid)
            grid = list(zip(*grid[::-1]))
            grid = [list(c) for c in grid]
        
        # for line in grid:
        #     print(''.join(line))
        # print('\n')
        states[hash] = (c+1,score(grid))
    first = states[hash][0]
    rep = c+1 - states[hash][0]
    rot = first+(4000000000-first)%rep
    ans = [state[1] for state in states.values() if state[0] == rot]
    return ans[0]

puzzle.answer_b = part2()


