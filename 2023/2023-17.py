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

day = 17
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    # data = puzzle.examples[0].input_data.split('\n')
    data = """111111111111
999999999991
999999999991
999999999991
999999999991""".split('\n')

tiles = [[int(c) for c in line] for line in data]
width = len(tiles[0])
height = len(tiles)

def valid_pos(x,y):
    return 0 <= x < width and 0 <= y < height

def get_best_heat(min_step, max_step):
    dijkstra = defaultdict(list)
    dijkstra[0].append((0,0,0,1,0)) # key: cost, value: position, direction number of straight steps
    dijkstra[0].append((0,0,1,0,0)) # key: cost, value: position, direction number of straight steps

    best_heats = defaultdict(lambda: 1000000000000000000)

    def is_best_heat(x,y,dx,dy,cost,num_straight_steps):
        key = x,y,dx,dy,num_straight_steps
        cur_best = best_heats[key]
        if cost < cur_best:
            best_heats[key] = cost
            return True
        return False

    while dijkstra:
        cost = list(sorted(dijkstra.keys()))[0]
        if not dijkstra[cost]:
            dijkstra.pop(cost)
            continue
        x,y,dx,dy,num_str_steps = dijkstra[cost].pop()

        if (x,y) == (width-1,height-1) and num_str_steps >= min_step:
            print(cost)
            return cost
        
        dirs = []
        if num_str_steps >= min_step:
            dirs.extend(((dy,-dx),(-dy,dx)))
        if num_str_steps < max_step:
            dirs.append((dx,dy))

        for ndx, ndy in dirs:
            nx, ny = x+ndx, y+ndy
            if valid_pos(nx,ny):
                nr_str_step_next = num_str_steps + 1 if ndx == dx and ndy == dy else 1
                next_cost = tiles[ny][nx]
                if is_best_heat(nx,ny,ndx,ndy,cost + next_cost,nr_str_step_next):
                    dijkstra[cost + next_cost].append((nx,ny,ndx,ndy,nr_str_step_next))

puzzle.answer_a = get_best_heat(1, 3)
puzzle.answer_b = get_best_heat(4, 10)