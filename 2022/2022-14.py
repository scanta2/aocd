from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product
import re
import operator, string
import networkx as nx
import functools

day = 14
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

def build_rocks():
    rocks = set()
    for line in data:
        segments = line.split(' -> ')
        for t0,t1 in zip(segments[:-1],segments[1:]):
            t0 = complex(*(int(i) for i in t0.split(',')))
            t1 = complex(*(int(i) for i in t1.split(',')))
            t = (t1-t0)/abs(t1-t0)
            while t0 != t1:
                rocks.add(t0)
                t0 += t
            rocks.add(t1)
    return rocks


rocks = build_rocks()
occupied = rocks.copy()
abyss_depth = max(i.imag for i in rocks)+1
floor = max(i.imag for i in rocks)+2

down = 1j
right = 1+1j
left = -1+1j

def addrock(start=500,parta=True):
    if parta and start.imag >= abyss_depth:
        return False
    if start+down not in occupied and (not parta and (start+down).imag < floor):
        return addrock(start=start+down,parta=parta)
    elif start+left not in occupied and (not parta and (start+left).imag < floor):
        return addrock(start=start+left,parta=parta)
    elif start+right not in occupied and (not parta and (start+right).imag < floor):
        return addrock(start=start+right,parta=parta)
    else:
        occupied.add(start)
        if start == 500:
            return False
        return True

# while(addrock()):
#     continue
# puzzle.answer_a = len(occupied)-len(rocks)

occupied = rocks.copy()
while(addrock(parta=False)):
    continue
print(len(occupied)-len(rocks))


