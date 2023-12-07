from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=14)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter
from operator import itemgetter

input = puzzle.input_data.split('\n')

# input = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".split('\n')

def parse():
    start = ''
    rules = {}
    for line in input:
        if line == '':
            continue
        if ' -> ' in line:
            rules[line[0:2]] = line[-1]
        else:
            start = line
    return start, rules

start, rules = parse()

def part1(num_steps):
    old = start
    new = old[-1]
    for step in range(num_steps):
        for c in range(len(old)-2,-1,-1):
            pattern = old[c:c+2]
            if pattern in rules:
                new = rules[pattern] + new
            new = old[c] + new
        old, new = new, new[-1]
    counter = Counter(old)
    mx = max(counter.items(), key=itemgetter(1))
    mn = min(counter.items(), key=itemgetter(1))
    return mx[1]-mn[1]

def part2(num_steps):
    counter = Counter(start)
    memo = dict()

    def process(chunk,step):
        local_counter = Counter()
        if (chunk,step) in memo:
            return memo[chunk,step]
        if step > num_steps:
            return Counter()
        if chunk in rules:
            sub = rules[chunk]
            local_counter[sub] += 1
            local_counter += process(''.join([chunk[0],sub]),step+1)
            local_counter += process(''.join([sub,chunk[1]]),step+1)
            memo[(chunk,step)] = local_counter
            return local_counter
    
    for i in range(len(start)-1):
        counter += process(start[i:i+2],1)
    
    mx = max(counter.items(), key=itemgetter(1))
    mn = min(counter.items(), key=itemgetter(1))
    return mx[1]-mn[1]      



# puzzle.answer_a = part1(10)
puzzle.answer_b = part2(40)

