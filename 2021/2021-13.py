from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=13)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter

input = puzzle.input_data.split('\n')

paper = set()
for line in input:
    if ',' in line:
        x,y = line.split(',')
        paper.add((int(x),int(y)))

folds = []
for line in input:
    if '=' in line:
        instr,where = line.split('=')
        folds.append((instr[-1], int(where)))

def process_fold(dot,fold):
    if (fold[0] == 'x'):
        if (dot[0] < fold[1]):
            return copy(dot)
        else:
            return (2*fold[1]-dot[0],dot[1])
    else:
        if (dot[1] < fold[1]):
            return copy(dot)
        else:
            return (dot[0],2*fold[1]-dot[1])


def part1():
    new_paper = set()
    for dot in paper:
        new_paper.add(process_fold(dot,folds[0]))
    return len(new_paper)

def visualize(dots):
    x = set(dot[0] for dot in dots)
    y = set(dot[1] for dot in dots)
    for row in range(max(y)+1):
        line = ''
        for col in range(max(x)+1):
            if (col,row) in dots:
                line += '#'
            else:
                line += ' '
        print(line)

def part2():
    old_paper = copy(paper)
    new_paper = set()
    for fold in folds:
        for dot in old_paper:
            new_paper.add(process_fold(dot,fold))
        old_paper, new_paper = new_paper, set()
    visualize(old_paper)
        

# puzzle.answer_a = part1()
part2()
