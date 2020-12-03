from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque
import queue
puzzle = Puzzle(year=2017,day=24)
lines = puzzle.input_data.split('\n')
ports = set()
length = 0
max_score = 0
used_parts = deque()

def build_bridge(current_bridge):
    global max_score
    global length
    last_piece = current_bridge[-1]
    candidates = [x for x in ports if x[0] == last_piece[1] or x[1] == last_piece[1]]
    if len(candidates) == 0:
        if len(current_bridge) >= length:
            length = len(current_bridge)
            max_score = max(max_score, sum(sum(x) for x in current_bridge))
    else:
        for candidate in candidates:
            ports.remove(candidate)
            if (candidate[0] == last_piece[1]):
                added_piece = (candidate[0], candidate[1])
            else:
                added_piece = (candidate[1], candidate[0])
            current_bridge.append(added_piece)
            build_bridge(current_bridge)
            current_bridge.remove(added_piece)
            ports.add(candidate)
    pass


for line in lines:
    sides = tuple([int(x) for x in line.split('/')])
    ports.add(sides)

ports.remove((0,30))
build_bridge([(0,30)])
print(max_score)
