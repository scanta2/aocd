from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter
import queue
from itertools import combinations

rows = Puzzle(year=2015,day=18).input_data.split('\n')

nr = 100
nc = 100

grid = defaultdict(lambda:'.')
new_grid = defaultdict(lambda:'.')

for r,row in enumerate(rows):
    for c,col in enumerate(row):
        grid[(r,c)] = col

def neighbors(row,col):
    neighs = []
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if not (r == row and c == col):
                neighs.append((r,c))
    return neighs

def rule(curr_status,row,col):
    neighs = neighbors(row,col)
    counts = Counter()
    for (r,c) in neighs:
        counts[grid[(r,c)]] += 1
    if curr_status == '#':
        if counts['#'] == 2 or counts['#'] == 3:
            return '#'
        else:
            return '.'
    else:
        if counts['#'] == 3:
            return '#'
        else:
            return '.'

for step in range(100):
    grid[(0,0)] = '#'
    grid[(0,nc-1)] = '#'
    grid[(nr-1,0)] = '#'
    grid[(nc-1,nc-1)] = '#'
    for r in range(0,nr):
        for c in range(0, nc):
            new_grid[(r,c)] = rule(grid[(r,c)],r,c)
    grid, new_grid = new_grid, grid


grid[(0,0)] = '#'
grid[(0,nc-1)] = '#'
grid[(nr-1,0)] = '#'
grid[(nc-1,nc-1)] = '#'
print(sum([1 for k in grid if grid[k] == '#' ]))






