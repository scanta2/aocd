from aocd.models import Puzzle

import intcode2019

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
from itertools import product
import queue
puzzle = Puzzle(year=2019,day=6)
lines = puzzle.input_data.split('\n')

# lines = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

orbits = defaultdict(list)
for line in lines:
    orb = line.split(')')
    orbits[orb[0]].append(orb[1])

distances = defaultdict(defaultdict)

def count_orbits(center, level):
    return level + sum(count_orbits(p,level+1) for p in orbits[center])
# puzzle.answer_a = count_orbits('COM',0)

trees = [[],[]]

def p_to_COM(p):
    chain = []
    while True:
        # find parent of p
        for center,planets in orbits.items():
            if p in planets:
                chain.append(center)
                p = center
                break
        if center == 'COM':
            break
    return chain

trees[0] = p_to_COM('YOU')
trees[0].reverse()
trees[1] = p_to_COM('SAN')
trees[1].reverse()
for i in range(min(len(t) for t in trees)):
    if trees[0][i] != trees[1][i]:
        break

i -= 1
puzzle.answer_b = sum(len(t) for t in trees)-2*(i+1)

# answer = len(trees[0])-i-1
# print(answer)
# answer = len(trees[1])-i-1
# print(answer)

