from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque
import queue
puzzle = Puzzle(year=2015,day=16).input_data.split('\n')

wanted_sue = {'children': 3, 'cats': 7, 'samoyeds': 2,'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

aunts_sue = [{} for i in range(500)]
for num, line in enumerate(puzzle):
    tokens = line.replace(',','').replace(':', '').split(' ')
    match = True
    for i in range(1,len(tokens)//2):
        if tokens[2*i] == 'cats' or tokens[2*i] == 'trees':
            if int(tokens[2*i+1]) <= wanted_sue[tokens[2*i]]:
                match = False
                break
        elif tokens[2*i] == 'pomeranians' or tokens[2*i] == 'goldfish':
            if int(tokens[2*i+1]) >= wanted_sue[tokens[2*i]]:
                match = False
                break
        elif int(tokens[2*i+1]) != wanted_sue[tokens[2*i]]:
            match = False
            break
    if match:
        print(num+1)
        break
    
