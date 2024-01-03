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

day = 20
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".split('\n')
    
def part1():
    modules = {}
    for line in data:
        name, outputs = line.split(' -> ')
        if name[0] == '%':
            modules[name[1:]] = {'type': 'ff', 'state': False, 'outputs': outputs.split(', ')}
        elif name[0] == '&':
            modules[name[1:]] = {'type': 'conj', 'inputs': {}, 'outputs': outputs.split(', ')}
        else:
            modules[name] = {'type': 'bc', 'state': 0, 'outputs': outputs.split(', ')}

    # second pass, initialize the conj modules
    for mod in modules:
        if modules[mod]['type'] == 'conj':
            modules[mod]['inputs'] = {n: False for n in modules if mod in modules[n]['outputs']}
    print(modules)

    n_high = 0
    n_low = 0
    max_count = 1000
    for button in range(max_count):
        stack = [('button', 0)]
        while stack:
            action = stack.pop(0)
            m_from, signal = action
            if m_from == 'button':
                n_low += 1
                stack.append(('broadcaster', 0))
            elif m_from not in modules:
                continue
            elif m_from == 'broadcaster':
                stack.extend([(out, 0) for out in modules['broadcaster']['outputs']])
                for m in modules['broadcaster']['outputs']:
                    if m in modules and modules[m]['type'] == 'conj':
                        modules[m]['inputs']['broadcaster'] = bool(0)
                n_low += len(modules['broadcaster']['outputs'])
            elif modules[m_from]['type'] == 'ff':
                if signal == 1:
                    continue
                modules[m_from]['state'] = not modules[m_from]['state']

                if modules[m_from]['state']:
                    stack.extend([(out, 1) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(1)
                    n_high += len(modules[m_from]['outputs'])
                else:
                    stack.extend([(out, 0) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(0)
                    n_low += len(modules[m_from]['outputs'])
            else:
                
                if all(v for v in modules[m_from]['inputs'].values()):
                    stack.extend([(out, 0) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(0)
                    n_low += len(modules[m_from]['outputs'])
                else:
                    stack.extend([(out, 1) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(1)
                    n_high += len(modules[m_from]['outputs'])
    return n_high*n_low

puzzle.answer_a = part1()

def part2():
    
    modules = {}
    for line in data:
        name, outputs = line.split(' -> ')
        if name[0] == '%':
            modules[name[1:]] = {'type': 'ff', 'state': False, 'outputs': outputs.split(', ')}
        elif name[0] == '&':
            modules[name[1:]] = {'type': 'conj', 'inputs': {}, 'outputs': outputs.split(', ')}
        else:
            modules[name] = {'type': 'bc', 'state': 0, 'outputs': outputs.split(', ')}

    # second pass, initialize the conj modules
    for mod in modules:
        if modules[mod]['type'] == 'conj':
            modules[mod]['inputs'] = {n: False for n in modules if mod in modules[n]['outputs']}
    print(modules)

    # find the only module that has rx as output
    name_rxparent = [m for m in modules if 'rx' in modules[m]['outputs']][0]
    rxparent_input = modules[name_rxparent]['inputs']
    # the tasks are to find when each input of rxparent is high
    steps = {}


    max_count = 10000000000000000000
    for button in range(max_count):
        stack = [('button', 0)]
        while stack:
            valid_ans = [m for m in modules[name_rxparent]['inputs'] if modules[name_rxparent]['inputs'][m] == True]
            for m in valid_ans:
                steps[m] = button+1
                if len(steps) == len(modules[name_rxparent]['inputs']):
                    return lcm(*steps.values())
            action = stack.pop(0)
            m_from, signal = action
            if m_from == 'button':
                stack.append(('broadcaster', 0))
            elif m_from not in modules:
                continue
            elif m_from == 'broadcaster':
                stack.extend([(out, 0) for out in modules['broadcaster']['outputs']])
                for m in modules['broadcaster']['outputs']:
                    if m in modules and modules[m]['type'] == 'conj':
                        modules[m]['inputs']['broadcaster'] = bool(0)
            elif modules[m_from]['type'] == 'ff':
                if signal == 1:
                    continue
                modules[m_from]['state'] = not modules[m_from]['state']

                if modules[m_from]['state']:
                    stack.extend([(out, 1) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(1)
                else:
                    stack.extend([(out, 0) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(0)
            else:
                
                if all(v for v in modules[m_from]['inputs'].values()):
                    stack.extend([(out, 0) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(0)
                else:
                    stack.extend([(out, 1) for out in modules[m_from]['outputs']])
                    for m in modules[m_from]['outputs']:
                        if m in modules and modules[m]['type'] == 'conj':
                            modules[m]['inputs'][m_from] = bool(1)


puzzle.answer_b = part2()

    
        