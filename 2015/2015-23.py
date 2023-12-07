from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter, OrderedDict
import queue
from itertools import combinations
from math import sqrt, floor, ceil

lines = Puzzle(year=2015,day=23).input_data.split('\n')

registers = {'a': 1, 'b': 0}
ip = 0

def decode(line):
    global ip
    tk = line.replace(',', '').split(' ')
    if tk[0] == 'hlf':
        registers[tk[1]] //=2
        ip += 1
    elif tk[0] == 'tpl':
        registers[tk[1]] *= 3
        ip += 1
    elif tk[0] == 'inc':
        registers[tk[1]] += 1
        ip += 1
    elif tk[0] == 'jmp':
        ip += int(tk[1])
    elif tk[0] == 'jie':
        if registers[tk[1]]%2 == 0:
            ip += int(tk[2])
        else:
            ip += 1
    elif tk[0] == 'jio':
        if registers[tk[1]] == 1:
            ip += int(tk[2])
        else:
            ip += 1
    
while ip < len(lines):
    decode(lines[ip])

print(registers['b'])

    

            