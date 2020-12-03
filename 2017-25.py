from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque
import queue
puzzle = Puzzle(year=2017,day=25)

turing_machine = defaultdict(int)
state = 'a'
slot = 0

for i in range(12919244):
    if state == 'a':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot += 1
            state = 'b'
        else:
            turing_machine[slot] = 0
            slot -= 1
            state = 'c'
    elif state == 'b':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot -= 1
            state = 'a'
        else:
            turing_machine[slot] = 1
            slot += 1
            state = 'd'
    elif state == 'c':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot += 1
            state = 'a'
        else:
            turing_machine[slot] = 0
            slot -= 1
            state = 'e'
    elif state == 'd':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot += 1
            state = 'a'
        else:
            turing_machine[slot] = 0
            slot += 1
            state = 'b'
    elif state == 'e':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot -= 1
            state = 'f'
        else:
            turing_machine[slot] = 1
            slot -= 1
            state = 'c'
    elif state == 'f':
        if (turing_machine[slot]) == 0:
            turing_machine[slot] = 1
            slot += 1
            state = 'd'
        else:
            turing_machine[slot] = 1
            slot += 1
            state = 'a'

print(turing_machine)
print(sum([turing_machine[k] for k in turing_machine.keys()]))


