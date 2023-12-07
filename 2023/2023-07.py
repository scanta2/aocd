from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import deepcopy

day = 7
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

# data=puzzle.examples[0].input_data.split('\n')

cards = 'AKQJT98765432'[::-1]

cards_two = 'AKQT98765432J'[::-1]

def part1():
    hands = {x:y for x,y in (line.split(' ') for line in data)}
    def ordering(h):
        hac = Counter(x for x in h)

        hand_strength = max(int(x) for x in hac.values())
        if hand_strength > 3:
            hand_strength += 2
        elif hand_strength == 3:
            if 2 in hac.values():
                hand_strength += 2
            else:
                hand_strength += 1
        elif hand_strength == 2:
            if sum(1 for i in hac.values() if i == 2) == 2:
                hand_strength += 1
        
        key = (hand_strength, *(cards.index(a) for a in h))
        return key
                
    ordered_hands = OrderedDict(sorted(hands.items(), key= lambda x: ordering(x[0])))
    return sum((i+1)*int(val) for i, (key, val) in enumerate(ordered_hands.items()))
                
puzzle.answer_a = part1()

def part2():
    hands = {x:y for x,y in (line.split(' ') for line in data)}
    def ordering(h):
        hac = Counter(x for x in h)
        jc = hac['J']
        hac['J'] = 0
        hac[hac.most_common(1)[0][0]] += jc
        
        hand_strength = max(int(x) for x in hac.values())
        if hand_strength > 3:
            hand_strength += 2
        elif hand_strength == 3:
            if 2 in hac.values():
                hand_strength += 2
            else:
                hand_strength += 1
        elif hand_strength == 2:
            if sum(1 for i in hac.values() if i == 2) == 2:
                hand_strength += 1
        
        key = (hand_strength, *(cards_two.index(a) for a in h))
        return key
                
    ordered_hands = OrderedDict(sorted(hands.items(), key= lambda x: ordering(x[0])))
    return sum((i+1)*int(val) for i, (key, val) in enumerate(ordered_hands.items()))

puzzle.answer_b = part2()
