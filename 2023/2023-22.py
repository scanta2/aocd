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

day = 22
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')

def brick_proj_xy(brick):
    if brick[0][0] == brick[1][0]:
        miny = min(brick[0][1], brick[1][1])
        maxy = max(brick[0][1], brick[1][1])
        pos = [(brick[0][0], y) for y in range(miny, maxy+1)]
    elif brick[0][1] == brick[1][1]:
        minx = min(brick[0][0], brick[1][0])
        maxx = max(brick[0][0], brick[1][0])
        pos = [(x, brick[0][1]) for x in range(minx, maxx+1)]
    else:
        pos = [(brick[0][0], brick[0][1])]
    return pos

def lower_brick(ib, bricks, checkonly=False):
    brick = bricks[ib]
    minzb = brick[0][2]
    if minzb == 1:
        return []

    posb = brick_proj_xy(brick)

    lowz = [1] 
    leanon = [-1]

    for ij, other in enumerate(bricks):
        if ij == ib:
            continue
        maxzj = other[1][2]
        if minzb > maxzj:
            posj = brick_proj_xy(other)
            if len(set.intersection(set(posb),set(posj))):
                lowz.append(maxzj+1)
                leanon.append(ij)
            else:
                lowz.append(1)
                leanon.append(-1)
    
    lowzmax = max(lowz)
    diff = minzb-lowzmax

    leanon = [zz[1] for zz in zip(lowz, leanon) if zz[0] == lowzmax]
    if diff == 0:
        return leanon
    if checkonly == False:
        bricks[ib][0][2] -= diff
        bricks[ib][1][2] -= diff
    return leanon
        
    
def part1():
    bricks = []
    for line in data:
        brickss = line.split('~')
        brick = []
        for be in brickss:
            brick.append([int(x) for x in be.split(',')])
        if brick[0][2] > brick[1][2]:
            brick = brick[::-1]
        bricks.append(brick)
    bricks = list(sorted(bricks, key = lambda x: x[0][2]))

    bricks_leanon = dict()
    for ib in range(len(bricks)):
        leanon = lower_brick(ib, bricks)
        bricks_leanon[ib] = leanon

    
    unsafe = set(b[0] for b in bricks_leanon.values() if len(b) == 1)
    res = len(bricks)-len(unsafe)
    print(res)
    return res

puzzle.answer_a = part1()

def part2():
    bricks = []
    for line in data:
        brickss = line.split('~')
        brick = []
        for be in brickss:
            brick.append([int(x) for x in be.split(',')])
        if brick[0][2] > brick[1][2]:
            brick = brick[::-1]
        bricks.append(brick)
    bricks = list(sorted(bricks, key = lambda x: x[0][2]))

    bricks_leanon = dict()
    for ib in range(len(bricks)):
        leanon = lower_brick(ib, bricks)
        bricks_leanon[ib] = set(leanon)
        if -1 in bricks_leanon[ib]:
            bricks_leanon[ib].remove(-1)

    num_falling = 0
    for ib in range(len(bricks)):
        bricks_falling = {ib}
        for jb in range(ib+1, len(bricks)):
            if len(bricks_leanon[jb]) and bricks_leanon[jb].issubset(bricks_falling):
                num_falling += 1
                bricks_falling.add(jb)
    print(num_falling)
    return num_falling

puzzle.answer_b = part2()

    
        