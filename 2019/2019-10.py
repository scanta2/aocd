from aocd.models import Puzzle
import intcode2019
from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter, deque
from itertools import product, permutations
from math import sqrt, atan2, pi
from functools import cmp_to_key
from fractions import gcd

puzzle = Puzzle(year=2019,day=10)
ast_map = puzzle.input_data.split('\n')

x_max, y_max = len(ast_map[0]), len(ast_map)

dirs = []

def add_to_dirs(x,y):
    found = False
    for dx,dy in dirs:
        if dx*y == dy*x and dx*x >= 0 and dy*y >= 0:
            found = True
            break 
    if not found:
        dirs.append((x,y))

def direction(dx,dy,x,y):
    if ast_map[y][x] == '#' and (dx,dy) != (x,y):
        if ast_map[dy][dx] == '#':
            add_to_dirs(dx-x,dy-y)

# num_directions = 0

# for x,y in product(range(x_max),range(y_max)):
#     dirs.clear()
#     [direction(dx,dy,x,y) for dx,dy in product(range(x_max),range(y_max))]
#     if (len(dirs) > num_directions):
#         station_coords = (x,y)
#     num_directions = max(len(dirs),num_directions)

# print(station_coords)

station_coords = (20,21)

def angle_dir(dir):
    x = atan2(-dir[1],dir[0])
    if x > pi/2:
        x -= 2*pi
    return 90 - x*180/pi

def dist(ast):
    return (ast[0]-station_coords[0])**2+(ast[1]-station_coords[1])**2

asteroids_per_dir = defaultdict(list)
xs,ys = station_coords
for x,y in product(range(x_max),range(y_max)):
    if (x,y) != station_coords and ast_map[y][x] == '#':
        xd,yd = x-xs, y-ys
        norm = abs(gcd(xd,yd))
        asteroids_per_dir[(xd//norm,yd//norm)].append((x,y))

for key in asteroids_per_dir:
    asteroids_per_dir[key] = sorted(asteroids_per_dir[key],key=dist)

sorted_dirs = sorted(asteroids_per_dir, key=angle_dir)

i = 0
while i < 200:
    for dir in sorted_dirs:
        if len(asteroids_per_dir[dir]) > 0:
            last_asteroid = asteroids_per_dir[dir].pop(0)
            i += 1
            if i == 200:
                break
puzzle.answer_b = last_asteroid[0]*100+last_asteroid[1]





    