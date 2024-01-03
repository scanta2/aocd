import itertools
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=18)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter
from operator import itemgetter
import networkx as nx
import math as m
import ast
from collections.abc import Iterable

lines = []

expressions = puzzle.input_data
for espression in expressions.split('\n'):
    lines.append(ast.literal_eval(espression))   

def flatten(stack,l):
    for i, el in enumerate(l):
        stack.append(i)
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(stack, el)
        else:
            yield [copy(stack), el]
        stack.pop()

def reduce(partial):
    for i, elem in enumerate(partial):
        stack, num = elem
        if len(stack) == 5:
            if i-1 >= 0:
                partial[i-1][1] += partial[i][1]
            if i+2 < len(partial):
                partial[i+2][1] += partial[i+1][1]
            partial.remove(partial[i+1])
            partial[i][0].pop()
            partial[i][1] = 0
            return True

    for i, elem in enumerate(partial):
        stack, num = elem
        if num >= 10:
            partial[i][0].append(0)
            partial[i][1] = num//2
            partial.insert(i+1,deepcopy(partial[i]))
            partial[i+1][0][-1] = 1
            partial[i+1][1] = num-partial[i][1]
            return True
    return False

def magnitude(result):
    if len(result) == 2:
        return 3*result[0][1] + 2*result[1][1]
    else:
        for i, elem in enumerate(result):
            stack = elem[0]
            stackn = result[i+1][0]
            if len(stack) == len(stackn):
                if all(stack[j] == stackn[j] for j in range(len(stack)-1)):
                    elem[0].pop()
                    elem[1] = elem[1]*3+2*result[i+1][1]
                    result.remove(result[i+1])
                    return magnitude(result)
    


def part1(inputs):
    flattened = list(flatten([],inputs[0]))
    for line in inputs[1:]:
        for f in flattened:
            f[0].insert(0,0)
        flattened.extend(list(flatten([1],line)))
        while reduce(flattened):
            continue
    while reduce(flattened):
        continue
    return magnitude(flattened)

puzzle.answer_a = part1(lines)

def part2(inputs):
    mag = 0
    for new_input in itertools.permutations(inputs,2):
        mag = max(mag,part1(new_input))
    return(mag)

puzzle.answer_b = part2(lines)
        

    