from types import prepare_class
from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=10)
from copy import deepcopy
import re
import itertools
import collections

score_p1 = {')' : 3, ']' : 57, '}': 1197, '>' : 25137}
matches = {'(' : ')', '[': ']', '{': '}', '<': '>'}

def parse1(line):
    stack = []
    for i in line:
        if i in matches:
            stack.append(i)
        else:
            if i == matches[stack[-1]]:
                stack.pop()
            else:
                return score_p1[i]
    return 0

def part1(input):
    return sum(parse1(line) for line in input.split('\n'))

# puzzle.answer_a = part1(puzzle.input_data)

score_p2 = {')' : 1, ']' : 2, '}': 3, '>' : 4}

def parse2(line):
    stack = []
    for i in line:
        if i in matches:
            stack.append(i)
        else:
            if i == matches[stack[-1]]:
                stack.pop()
            else:
                return 0
    score = sum(score_p2[matches[i]]*5**j for j,i in enumerate(stack))
    return score

def part2(input):
    scores = [parse2(line) for line in input.split('\n')]
    scores = sorted([i for i in scores if i != 0])
    return scores[len(scores)//2]

puzzle.answer_b = part2(puzzle.input_data)