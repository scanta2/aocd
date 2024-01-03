from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import functools
import networkx

day = 19
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    workflows_, parts = puzzle.input_data.split('\n\n')
else:
    workflows_, parts = puzzle.examples[0].input_data.split('\n\n')

class Part():
    def __init__(self,line):
        self.x, self.m, self.a, self.s = list(int(x) for x in re.findall(r'\d+',line))
        self.score = self.x+self.m+self.a+self.s

class Workflow():
    def __init__(self,instr):
        options = instr.split(',')
        self.options = []
        for option in options:
            if ':' in option:
                fun, goto = option.split(':')
            else:
                fun = 'True'
                goto = option
            self.options.append((fun,goto))

    def eval(self, part, other_workflows):
        for opt in self.options:
            if opt[0] == 'True' or eval(''.join(('part.', opt[0]))):
                if opt[1] == 'R':
                    return 0
                if opt[1] == 'A':
                    return part.score
                return other_workflows[opt[1]].eval(part,other_workflows)

    
def part1():
    workflows = {}
    for workflow in workflows_.split('\n'):
        w, instr = workflow.split(r'{')
        workflows[w] = Workflow(instr[:-1])

    res = 0
    for p in parts.split('\n'):
        part = Part(p)
        res += workflows['in'].eval(part, workflows)
    return res
    
puzzle.answer_a = part1()

def solve_p2(values, curr, workflows):
    res = 0
    for fun, goto in workflows[curr].options:
        if '<' in fun:
            key, val = fun.split('<')
            if values[key][0] >= int(val):
                continue
            new_values = deepcopy(values)
            new_values[key][1] = min(new_values[key][1], int(val))
            if goto == 'A':
                res += prod(k[1]-k[0] for k in new_values.values())
            elif goto == 'R':
                res += 0
            else:
                res += solve_p2(new_values, goto, workflows)
            values[key][0] = max(values[key][0], int(val))
        elif '>' in fun:
            key, val = fun.split('>')
            if values[key][1] <= int(val):
                continue
            new_values = deepcopy(values)
            new_values[key][0] = max(new_values[key][0], int(val)+1)
            if goto == 'A':
                res += prod(k[1]-k[0] for k in new_values.values())
            elif goto == 'R':
                res += 0
            else:
                res += solve_p2(new_values, goto, workflows)
            values[key][1] = min(values[key][1], int(val)+1)
        else:
            if goto == 'A':
                res += prod(k[1]-k[0] for k in values.values())
            elif goto == 'R':
                res += 0
            else:
                res += solve_p2(values, goto, workflows)
    return res

def part2():
    workflows = {}
    for workflow in workflows_.split('\n'):
        w, instr = workflow.split(r'{')
        workflows[w] = Workflow(instr[:-1])

    values = {'x': [1,4001], 'm': [1,4001], 'a': [1,4001], 's': [1,4001]}
    return solve_p2(values, 'in', workflows)

puzzle.answer_b = part2()

    
        