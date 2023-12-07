from types import prepare_class
from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=9)
from copy import deepcopy
import re
import itertools
import collections

height_map = [[int(i) for i in row] for row in puzzle.input_data.split('\n')]
num_col = len(height_map[0])
num_row = len(height_map)

def is_min(x,y):
    choices = (-1, +1)
    xn = tuple(x+i for i in choices if x+i >= 0 and x+i < num_col)
    yn = tuple(y+i for i in choices if y+i >= 0 and y+i < num_row)
    return all(height_map[yy][x] > height_map[y][x] for yy in yn) and all(height_map[y][xx] > height_map[y][x] for xx in xn)

def part1():
    risk = sum(height_map[y][x]+1 for x,y in itertools.product(range(num_col),range(num_row)) if is_min(x,y))
    return risk

puzzle.answer_a = part1()

def part2():
    basin = []
    visited = set()

    def fill_basin(x,y,visited):
        if x < 0 or x >= num_col or y < 0 or y >= num_row or (x,y) in visited:
            return 0
        visited.add((x,y))
        if height_map[y][x] != 9:
            return 1 + fill_basin(x-1,y,visited) + fill_basin(x+1,y,visited) + fill_basin(x,y+1,visited) + fill_basin(x,y-1,visited)
        else:
            return 0
        
    
    for x,y in itertools.product(range(num_col),range(num_row)):
        if (x,y) not in visited:
            basin.append(fill_basin(x,y,visited))

    basin = list(reversed(sorted(basin)))
    return basin[0]*basin[1]*basin[2]
    

puzzle.answer_b = part2()