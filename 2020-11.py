from aocd.models import Puzzle
from collections import Counter
from itertools import product, chain
from copy import deepcopy
import networkx as nx
import string
import re

def rule1(curr_state,nr,nc):
    def adjacents(row,col,state,nr,nc):
        for r in range(max(0,row-1),min(nr,row+2)):
            for c in range(max(0,col-1),min(nc,col+2)):
                if not(r == row and c == col):
                    yield curr_state[r][c]

    new_state = deepcopy(curr_state)
    for r,c in product(range(nr),range(nc)):
        if curr_state[r][c] == 'L':
            if '#' not in adjacents(r,c,curr_state,nr,nc):
                new_state[r][c] = '#'
            
        elif curr_state[r][c] == '#':
            if sum(1 for x in adjacents(r,c,curr_state,nr,nc) if x == '#') >= 4:
                new_state[r][c] = 'L'
    return new_state

def part1(curr_state):
    nr, nc = len(curr_state), len(curr_state[0])
    memory = set()
    done = False
    while not done:
        memory.add(repr(curr_state))
        next_state = rule1(curr_state,nr,nc)
        done = repr(next_state) in memory
        next_state, curr_state = None, next_state
    flat_list = list(chain(*curr_state))
    return sum(1 for x in flat_list if x == '#')

def rule2(curr_state,nr,nc):
    directions = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
    def adjacents(row,col,state,nr,nc):
        for d in directions:
            r,c = row+d[0], col+d[1]
            while r >= 0 and r < nr and c >= 0 and c < nc:
                if state[r][c] != '.':
                    yield state[r][c]
                    break
                r += d[0]
                c += d[1]
    new_state = deepcopy(curr_state)
    for r,c in product(range(nr),range(nc)):
        if curr_state[r][c] == 'L':
            if '#' not in adjacents(r,c,curr_state,nr,nc):
                new_state[r][c] = '#'
            
        elif curr_state[r][c] == '#':
            if sum(1 for x in adjacents(r,c,curr_state,nr,nc) if x == '#') >= 5:
                new_state[r][c] = 'L'
    return new_state

def part2(curr_state):
    nr, nc = len(curr_state), len(curr_state[0])
    memory = set()
    done = False
    while not done:
        memory.add(repr(curr_state))
        next_state = rule2(curr_state,nr,nc)
        done = repr(next_state) in memory
        next_state, curr_state = None, next_state
    flat_list = list(chain(*curr_state))
    return sum(1 for x in flat_list if x == '#')


PUZZLE = Puzzle(year=2020,day=11)
INPUT = PUZZLE.input_data.splitlines()
curr_state = [[x for x in word] for word in INPUT]
PUZZLE.answer_a = part1(curr_state)
PUZZLE.answer_b = part2(curr_state)
