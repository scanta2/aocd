import networkx as nx
import intcode2019 as intc
from collections import defaultdict, deque, Counter
from aocd.models import Puzzle
from itertools import product
import string

puzzle = Puzzle(year=2019,day=24)
eris = [[c for c in line] for line in puzzle.input_data.split('\n')]
action = [[0 for i in range(5)] for j in range(5)]
replace = {'.': '#', '#': '.'}
positions = [(1,0), (-1,0), (0,1), (0,-1)]

def reset_action():
    global action
    action = [[0 for i in range(5)] for j in range(5)]

def state_number():
    return sum([2**lin_index(x,y) for x,y in product(range(5), range(5)) if eris[y][x] == '#'])

def print_state():
    for r in eris:
        print(''.join(r))
    print('\n')

valid_adjacent = lambda x,y : x >= 0 and x < 5 and y >= 0 and y < 5
adjacent = lambda x,y : [(x+pos[0],y+pos[1]) for pos in positions if valid_adjacent(x+pos[0],y+pos[1])]
lin_index = lambda x,y : y*5 + x

states = Counter()

while True:
    print_state()
    reset_action()
    state_number_ = state_number()
    states[state_number_] += 1
    if states[state_number_] == 2:
        print(state_number_)
        break
    for x,y in product(range(5), range(5)):
        adj = adjacent(x,y)
        num_adj_bugs = sum([1 for (xx,yy) in adj if eris[yy][xx] == '#'])
        if eris[y][x] == '.':
            if num_adj_bugs == 1 or num_adj_bugs == 2:
                action[y][x] = 1
        elif eris[y][x] == '#':
            if num_adj_bugs != 1:
                action[y][x] = 1
    for x,y in product(range(5), range(5)):
        if action[y][x] == 1:
            eris[y][x] = replace[eris[y][x]]