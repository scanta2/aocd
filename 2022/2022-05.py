from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from collections import deque
from string import ascii_uppercase
import re

day = 5
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

def read_stacks_a():
    num_stacks = (len(data[0])+1)//4
    stacks = [[] for i in range(num_stacks)]
    for il, line in enumerate(data):
        if '1' in line:
            break
        for stack_idx in range(num_stacks):
            crate = line[stack_idx*4+1]
            if crate in ascii_uppercase:
                stacks[stack_idx].insert(0,crate)
    for il, line in enumerate(data[il+2:]):
        num, origin, destination = [int(i) for i in re.findall(r'\d+', line)]
        stacks[origin-1], tmp = stacks[origin-1][:-num], stacks[origin-1][-num:]
        stacks[destination-1].extend(reversed(tmp))
        # for i in range(num):
        #     stacks[destination-1].append(stacks[origin-1][-1])
        #     stacks[origin-1].pop()
    return stacks

def read_stacks_b():
    num_stacks = (len(data[0])+1)//4
    stacks = [[] for i in range(num_stacks)]
    for il, line in enumerate(data):
        if '1' in line:
            break
        for stack_idx in range(num_stacks):
            crate = line[stack_idx*4+1]
            if crate in ascii_uppercase:
                stacks[stack_idx].insert(0,crate)
    for il, line in enumerate(data[il+2:]):
        num, origin, destination = [int(i) for i in re.findall(r'\d+', line)]
        stacks[origin-1], tmp = stacks[origin-1][:-num], stacks[origin-1][-num:]
        stacks[destination-1].extend(tmp)
    return stacks

def part_a():
    return ''.join([stack[-1] for stack in read_stacks_a()])

puzzle.answer_a = part_a()

def part_b():
    return ''.join([stack[-1] for stack in read_stacks_b()])

puzzle.answer_b = part_b()

print(puzzle.answer_a)
print(puzzle.answer_b)
