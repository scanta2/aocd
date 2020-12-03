import networkx as nx
import intcode2019 as intc
from collections import defaultdict, deque, Counter
from aocd.models import Puzzle
from itertools import product
import string

puzzle = Puzzle(year=2019,day=24)
input_data = puzzle.input_data.split('\n')
# input_data = """....#
# #..#.
# #..##
# ..#..
# #....""".split('\n')

eris = {0: [[c for c in line] for line in input_data]}
replace = {'.': '#', '#': '.'}

def empty():
    return [['.' for j in range(5)] for i in range(5)]

def adjacency_list(l,x,y):
    pos = (x,y)
    if pos == (1,1) or pos == (3,1) or pos == (1,3) or pos == (3,3):
        return [(l,x+1,y), (l,x-1,y), (l,x,y+1), (l,x,y-1)]
    if pos == (0,0):
        return [(l,x,y+1), (l,x+1,y), (l-1,2,1), (l-1,1,2)]
    if pos == (4,0):
        return [(l,3,0), (l,4,1), (l-1,2,1), (l-1,3,2)]
    if pos == (0,4):
        return [(l,0,3), (l,1,4), (l-1,2,3), (l-1,1,2)]
    if pos == (4,4):
        return [(l,3,4), (l,4,3), (l-1, 3,2), (l-1,2,3)]
    if x == 0:
        return [(l,x+1,y), (l,x,y+1), (l,x,y-1), (l-1,1,2)]
    if x == 4:
        return [(l,x-1,y), (l,x,y+1), (l,x,y-1), (l-1,3,2)]
    if y == 0:
        return [(l,x-1,y), (l,x+1,y), (l,x,y+1), (l-1, 2, 1)]
    if y == 4:
        return [(l,x-1,y), (l,x+1,y), (l, x, y-1), (l-1, 2,3)]
    if pos == (2,1):
        return [(l,2,0),(l,1,1),(l,3,1),(l+1,0,0),(l+1,1,0),(l+1,2,0),(l+1,3,0),(l+1,4,0)]
    if pos == (2,3):
        return [(l,2,4),(l,1,3),(l,3,3),(l+1,0,4),(l+1,1,4),(l+1,2,4),(l+1,3,4),(l+1,4,4)]
    if pos == (1,2):
        return [(l,0,2),(l,1,1),(l,1,3),(l+1,0,0),(l+1,0,1),(l+1,0,2),(l+1,0,3),(l+1,0,4)]
    if pos == (3,2):
        return [(l,4,2),(l,3,1),(l,3,3),(l+1,4,0),(l+1,4,1),(l+1,4,2),(l+1,4,3),(l+1,4,4)]
    if pos == (2,2):
        return []

def do_replace(l,x,y):
    adj = adjacency_list(l,x,y)
    num_adj_bugs = sum([1 for (ll,xx,yy) in adj if eris[ll][yy][xx] == '#'])
    if eris[l][y][x] == '.':
        if num_adj_bugs == 1 or num_adj_bugs == 2:
            return True
    elif eris[l][y][x] == '#':
        if num_adj_bugs != 1:
            return True
    return False

def count(l):
    tally = 0
    for i in range(-l,l+1):
        for x,y in product(range(5),range(5)):
            if (x,y) == (2,2):
                pass
            if eris[i][y][x] == '#':
                tally += 1
    return tally

it_end = 200

for i in range(1,it_end+2):
    eris[i] = empty()
    eris[-i] = empty()

for i in range(1,it_end+1):
    actions = []
    for level in range(-i,i+1):
        for x,y in product(range(5),range(5)):
            if do_replace(level,x,y):
                actions += [(level,x,y)]

    for action in actions:
        l,x,y = action
        eris[l][y][x] = replace[eris[l][y][x]]
    print(count(i))