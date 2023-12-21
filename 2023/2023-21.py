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
import numpy as np

day = 21
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split('\n')
    
def part1():
    grid = [[c for c in line] for line in data]
    height = len(grid)
    width = len(grid[0])

    for ys, line in enumerate(data):
        if 'S' in line:
            xs = line.index('S')
            grid[ys][xs] = '.'
            break

    prev_pos = set([(xs,ys)])
    new_pos = set()
    for steps in range(64):
        for x,y in prev_pos:
            for dir in ((-1,0),(1,0),(0,1),(0,-1)):
                try:
                    if grid[y+dir[1]][x+dir[0]] != '#':
                        new_pos.add((x+dir[0], y+dir[1]))
                except:
                    continue
        prev_pos, new_pos = new_pos, set()
    return len(prev_pos)
puzzle.answer_a = part1()

def part2():
    grid = [[c for c in line] for line in data]
    height = len(grid)
    width = len(grid[0])

    for ys, line in enumerate(data):
        if 'S' in line:
            xs = line.index('S')
            grid[ys][xs] = '.'
            break

    goal = 26501365

    stepx = []
    stepy = []
    prev_pos = set([(xs,ys)])
    new_pos = set()
    for step in range(1,100000):
        for x,y in prev_pos:
            for dir in ((-1,0),(1,0),(0,1),(0,-1)):
                    if grid[(y+dir[1])%height][(x+dir[0])%width] != '#':
                        new_pos.add((x+dir[0], y+dir[1]))
        prev_pos, new_pos = new_pos, set()
        if step%(height) == goal%(height):
            print(step)
            stepx.append(step)
            stepy.append(len(prev_pos))
            if len(stepx) == 3:
                z = np.polyfit(stepx, stepy,2)
                p = np.poly1d(z)
                res = int(p(goal))
                print(res)
                return res
puzzle.answer_b = part2()

    
        