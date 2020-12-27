from aocd.models import Puzzle
import re
from itertools import product
from math import prod

def neighbors(p0,state):
    ns = []
    if len(p0) == 3:
        ns = product(range(p0[0]-1,p0[0]+2),\
                         range(p0[1]-1,p0[1]+2),\
                         range(p0[2]-1,p0[2]+2))
    else:
        ns = product(range(p0[0]-1,p0[0]+2),\
                         range(p0[1]-1,p0[1]+2),\
                         range(p0[2]-1,p0[2]+2),\
                         range(p0[3]-1,p0[3]+2))
    for p in ns:
        # p = (i,j,k)
        if p != p0 and p in state:
            yield p

def num_active_neighbors(p0, state):
    n_active = sum(1 for p in neighbors(p0, state) if state[p] == '#')
    return n_active

def apply_rule(n_active,value):
    if value == '#':
        if 2 <= n_active <= 3:
            return '#'
        else:
            return '.'
    else:
        if n_active == 3:
            return '#'
        else:
            return '.'

def solve(state, bbox, ispart2):
    for i in range(6):
        bbox['x'][0] -= 1
        bbox['x'][1] += 1
        bbox['y'][0] -= 1
        bbox['y'][1] += 1
        bbox['z'][0] -= 1
        bbox['z'][1] += 1
        if ispart2:
            bbox['w'][0] -= 1
            bbox['w'][1] += 1

        new_state = state.copy()
        ns = []
        if not ispart2:
            ns = product(range(bbox['x'][0],bbox['x'][1]),\
                          range(bbox['y'][0],bbox['y'][1]),\
                          range(bbox['z'][0],bbox['z'][1]))
        else:
            ns = product(range(bbox['x'][0],bbox['x'][1]),\
                          range(bbox['y'][0],bbox['y'][1]),\
                          range(bbox['z'][0],bbox['z'][1]),\
                          range(bbox['w'][0],bbox['w'][1]))
        for p0 in ns:
            if p0 not in new_state:
                new_state[p0] = '.'
            n_active = num_active_neighbors(p0,state)
            new_state[p0] = apply_rule(n_active,new_state[p0])
        state, new_state = new_state, state
    return sum(1 for p in state if state[p] == '#')


PUZZLE = Puzzle(year=2020,day=17)
INPUT = PUZZLE.input_data.splitlines()
# INPUT = """.#.
# ..#
# ###""".splitlines()
state1 = {(i,j,0): v for j,x in enumerate(INPUT) for i,v in enumerate(x) }
state2 = {(i,j,0,0): v for j,x in enumerate(INPUT) for i,v in enumerate(x) }
bbox = {'x': [0, len(INPUT[0])],\
        'y': [0, len(INPUT)],\
        'z': [0,1],
        'w': [0,1]}
PUZZLE.answer_a = solve(state1, bbox, False)
PUZZLE.answer_b = solve(state2, bbox, True)