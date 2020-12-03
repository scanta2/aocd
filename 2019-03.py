from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
from itertools import product
import queue
puzzle = Puzzle(year=2019,day=3)
lines = puzzle.input_data.split('\n')
print(lines)

directions = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}
points = [[], []]
for i,line in enumerate(lines):
    point = 0j
    for token in line.split(','):
        for j in range(int(token[1:])):
            point += directions[token[0]]
            points[i].append(point)

common_points = set(points[0]).intersection(set(points[1]))
# distances = [abs(p.real)+abs(p.imag) for p in common_points]
# puzzle.answer_a = int(min(distances))

def distance(p):
    return abs(p.real)+abs(p.imag)

combined_distances = [points[0].index(p)+points[1].index(p)+2 for p in common_points]
puzzle.answer_b = min(combined_distances)


