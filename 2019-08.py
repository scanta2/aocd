from aocd.models import Puzzle

import intcode2019

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter,deque
from itertools import product, permutations
import queue
puzzle = Puzzle(year=2019,day=8)
program = puzzle.input_data

width, height = 25, 6
num_layer = len(program)//width//height

num_zeros = width*height+1
answer_a = 0

for i_layer in range(num_layer):
    layer = program[i_layer*width*height:(i_layer+1)*width*height]
    cond = Counter(layer)
    if cond['0'] < num_zeros:
        num_zeros = cond['0']
        answer_a = cond['1']*cond['2']
# puzzle.answer_a = answer_a


answer_b = ['2' for i in range(width*height)]
for i_layer in range(num_layer):
    layer = program[i_layer*width*height:(i_layer+1)*width*height]
    for i,pixel in enumerate(layer):
        if answer_b[i] == '2':
            answer_b[i] = pixel
for i in range(height):
    row = answer_b[i*width:(i+1)*width]
    row = ''.join(row)
    row = row.replace('0', ' ').replace('1', '*')
    print(row)

