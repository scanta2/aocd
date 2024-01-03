from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=12)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter

input = puzzle.input_data

# input = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""

def parse_input():
    caves = defaultdict(list)
    for line in input.split('\n'):
        a,b = line.split('-')
        caves[a].append(b)
        caves[b].append(a)
    return caves

caves = parse_input()

path = []

def traverse1(node,last):
    if node == last:
        return 1
    if str.islower(node) and node in path:
        return 0
    path.append(node)
    num_paths = sum(traverse1(child,last) for child in caves[node])
    path.pop()
    return num_paths

def part1():
    return(traverse1('start','end'))
 

def part2(begin, end):
    to_visit = [list(reversed(sorted(copy(caves[begin]))))]
    path = [begin]
    num_paths = 0
    while to_visit:
        if len(to_visit[-1]) == 0:
            path.pop()
            to_visit.pop()
            continue
        path.append(to_visit[-1].pop())
        if path[-1] == end:
            num_paths += 1
            path.pop()
            continue
        elif path[-1] == begin and path.count(begin) > 1:
            path.pop()
            continue
        elif str.islower(path[-1]):
            counter = Counter(path)
            if any(counter[b] > 2 for b in counter if str.islower(b)) or sum(counter[b] >= 2 for b in counter if str.islower(b))>1:
                path.pop()
                continue
        to_visit.append(list(reversed(sorted(copy(caves[path[-1]])))))
        
    return num_paths

    
    


puzzle.answer_b = part2('start','end')
