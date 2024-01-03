from copy import copy, deepcopy
import itertools as it
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=25)
from collections import Counter
from math import prod
import networkx as nx

initial_state = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

initial_state = puzzle.input_data

initial_state = [[c for c in row] for row in initial_state.split('\n')]

step = 1
while True:
    moving = '>'
    moved = 0
    new_state = deepcopy(initial_state)
    length = len(new_state[0])
    nr = len(new_state)
    for r in range(nr):
        for c in range(length):
            if initial_state[r][c] == moving and initial_state[r][(c+1)%length] == '.':
                new_state[r][c], new_state[r][(c+1)%length] = new_state[r][(c+1)%length], new_state[r][c]
                moved += 1
    initial_state, new_state = new_state, None
    new_state = deepcopy(initial_state)
    moving  = 'v'
    for r in range(nr):
        for c in range(length):
            if initial_state[r][c] == moving and initial_state[(r+1)%nr][c] == '.':
                new_state[r][c], new_state[(r+1)%nr][c] = new_state[(r+1)%nr][c], new_state[r][c]
                moved += 1

    # print('After {} step:'.format(step))
    # for row in new_state:
    #     print(''.join(row))
    # print('')
    if moved == 0:
        puzzle.answer_a = step
        break
    initial_state, new_state = new_state, None
            



    step += 1