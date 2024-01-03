from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain, product
from collections import defaultdict
from copy import deepcopy

day = 5
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n\n')

# data=puzzle.examples[0].input_data.split('\n\n')

def part1():
    value = 10000000000000
    seeds = re.finditer(r'\d+',data[0])
    for seed in seeds:
        curr_value = int(seed.group(0))
        for group in data[1:]:
            for line in group.split('\n')[1:]:
                values = line.split(' ')
                if curr_value in range(int(values[1]), int(values[1])+int(values[2])):
                    curr_value = curr_value-int(values[1])+int(values[0])
                    break
        value = min(curr_value, value)
    print(value)
    return value
                

puzzle.answer_a = part1()

def part2():
    value = 10000000000000
    seeds = re.findall(r'\d+',data[0])
    found_values = dict()

    parsed_groups = []

    for group in data[1:]:
        p_group = dict()
        for line in group.split('\n')[1:]:
            values = line.split(' ')
            p_group[range(int(values[1]), int(values[1])+int(values[2]))] = int(values[0])
        parsed_groups.extend([p_group])
    
    for i in range(0,len(seeds),2):
        seed_range = [int(s) for s in seeds[i:i+2]]
        extent = seed_range[1]
        curr_seed = seed_range[0]
        while curr_seed < seed_range[0]+seed_range[1]:
            curr_value = curr_seed
            for group in parsed_groups:
                for rr in group:
                    if curr_value in rr:
                        extent = min(extent, rr.stop-curr_value)
                        curr_value = curr_value-rr[0]+group[rr]
                        break
            value = min(curr_value, value)
            curr_seed += extent
    print(value)
    return value

puzzle.answer_b = part2()
