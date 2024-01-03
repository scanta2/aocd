from types import prepare_class
from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=8)
from copy import deepcopy
import re
import itertools
import collections

known_lengths = set([2,4,3,7])

signals_ = {0: 'abcefg', \
           1: 'cf', \
           2: 'acdeg', \
           3: 'acdfg', \
           4: 'bcdf', \
           5: 'abdfg', \
           6: 'abdefg', \
           7: 'acf', \
           8: 'abcdefg', \
           9: 'abcdfg' }
signals = dict(zip(signals_.values(), signals_.keys()))

def part1(input):
    count = 0
    for line in input.split('\n'):
        i, o = line.split(' | ')
        count += sum(len(oo) in known_lengths for oo in o.split(' '))
    return count

def deduce(numoptions, outputs):
    substitutions = {}
    substitutions['c'] = [i for i in numoptions[1][0]]
    substitutions['f'] = [i for i in numoptions[1][0]]
    substitutions['a'] = [i for i in numoptions[7][0] if i not in substitutions['c']]
    substitutions['b'] = [i for i in numoptions[4][0] if i not in substitutions['c']]
    substitutions['d'] = [i for i in numoptions[4][0] if i not in substitutions['c']]
    substitutions['e'] = [i for i in numoptions[8][0] if i not in substitutions['c'] and i not in substitutions['a'] and i not in substitutions['b']]
    substitutions['g'] = [i for i in numoptions[8][0] if i not in substitutions['c'] and i not in substitutions['a'] and i not in substitutions['b']]
    
    keys, values = zip(*substitutions.items())
    for bundle in itertools.product(*values):
        if len(set(bundle)) != len(bundle):
            continue
        d = dict(zip(bundle,keys))
        translation = [''.join(sorted(d[i] for i in o)) for o in outputs]
        if all(o in signals for o in translation):
            v = 0
            for exp, o in enumerate(reversed(translation)):
                v += int(signals[o])*10**exp
            return int(v)

def part2(input):
    total = 0
    for line in input.split('\n'):
        inps, o = line.split(' | ')
        ii = inps.split(' ')
        matches = {}
        for num in range(10):
            matches[num] = [j for j in ii if len(j) == len(signals_[num])]
        total += deduce(matches, [''.join(oo) for oo in o.split(' ')])
    return total
        
        
        

# puzzle.answer_a = part1(puzzle.input_data)
puzzle.answer_b = part2(puzzle.input_data)