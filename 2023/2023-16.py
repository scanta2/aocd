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

day = 16
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')

grid = [[c for c in line] for line in data]
height = len(grid)
width = len(grid[0])

def part1(pos, dir):
    stack = []

    seen = set()
    stack.append((pos, dir))
    while stack:
        pos, dir = stack.pop()
        while True:
            pos = [p+d for p,d in zip(pos,dir)]
            if not (0 <= pos[0] < height and 0 <= pos[1] < width):
                break
            if (tuple(pos),tuple(dir)) in seen:
                break
            else:
                seen.add((tuple(pos),tuple(dir)))

            tile = grid[pos[0]][pos[1]]
            if tile == '.':
                continue

            if tile == '/':
                if dir == [0,1]:
                    dir = [-1,0]
                elif dir == [0,-1]:
                    dir = [1,0]
                elif dir == [1,0]:
                    dir = [0,-1]
                elif dir == [-1,0]:
                    dir = [0,1]
                continue

            if tile == '\\':
                if dir == [0,1]:
                    dir = [1,0]
                elif dir == [0,-1]:
                    dir = [-1,0]
                elif dir == [1,0]:
                    dir = [0,1]
                elif dir == [-1,0]:
                    dir = [0,-1]
                continue

            if tile == '-':
                if dir[0] == 0:
                    continue
                else:
                    stack.append((pos, [0,1]))
                    stack.append((pos, [0,-1]))
                    break

            if tile == '|':
                if dir[1] == 0:
                    continue
                else:
                    stack.append((pos, [1,0]))
                    stack.append((pos, [-1,0]))
                    break
    
    tiles = set(i[0] for i in seen)
    print(len(tiles))
    return len(tiles)

def part2():
    res = []
    for i in range(height):
        res.append(part1([i,-1],[0,1]))
        res.append(part1([i,width],[0,-1]))
    for i in range(width):
        res.append(part1([-1,i],[1,0]))
        res.append(part1([height,i],[-1,0]))
    return max(res)


puzzle.answer_a = part1([0,-1],[0,1])
puzzle.answer_b = part2()
