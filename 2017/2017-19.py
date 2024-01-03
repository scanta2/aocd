from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict
import queue
puzzle = Puzzle(year=2017,day=19)
lines = puzzle.input_data.split('\n')

d, u, l, r = (1,0), (-1,0), (0, -1), (0, 1)

direction = d
pos = (0,lines[0].find('|'))
letters = ''
steps = 0

while True:
    steps += 1
    new_pos = (pos[0]+direction[0], pos[1]+direction[1])
    new_value = lines[new_pos[0]][new_pos[1]]
    if new_value == ' ':
        break
    elif new_value == '+':
        steps += 1
        pos = new_pos
        if direction == d or direction == u:
            direction = r
            new_pos = (pos[0]+r[0], pos[1]+r[1])
            new_value = lines[new_pos[0]][new_pos[1]]
            if new_value == ' ':
                direction = l
                new_pos = (pos[0]+l[0], pos[1]+l[1])
                new_value = lines[new_pos[0]][new_pos[1]]
        else:
            direction = u
            new_pos = (pos[0]+u[0], pos[1]+u[1])
            new_value = lines[new_pos[0]][new_pos[1]]
            if new_value == ' ':
                direction = d
                new_pos = (pos[0]+d[0], pos[1]+d[1])
                new_value = lines[new_pos[0]][new_pos[1]]
    elif new_value.isalpha():
        letters += new_value
    pos = new_pos
puzzle.answer_a = letters
puzzle.answer_b = steps
