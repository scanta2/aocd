from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
puzzle = Puzzle(year=2017,day=17)

steps = 348
buffer = [0]
pos = 0

value = 0
buffer_len = 1

for i in range (1,50000000+1):
    pos = (pos + steps)%buffer_len
    if pos == 0:
        value = i
    buffer_len += 1
    pos = (pos+1)%buffer_len
puzzle.answer_b = value
