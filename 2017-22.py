from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
import queue
puzzle = Puzzle(year=2017,day=22)
input_grid = puzzle.input_data.split('\n')

grid = {}
im = 0
for line in input_grid:
    re = 0
    for pixel in line:
        grid[complex(re,im)] = pixel
        re +=1
    im += -1
point = complex(12,-12)
j = complex(0,1)
direction = j

rotation = {'#': -j, '.': j, 'f': -1, 'w': 1}
flip_status = {'#': 'f', '.': 'w', 'w': '#', 'f': '.'}
get_infected = {'.': 0, '#': 0, 'w': 1, 'f': 0}

become_infected = 0

for b in range(10000000):
    if point not in grid.keys():
        grid[point] = '.'
    direction *= rotation[grid[point]]
    become_infected += get_infected[grid[point]]
    grid[point] = flip_status[grid[point]]
    point += direction
print(become_infected)

    
    

