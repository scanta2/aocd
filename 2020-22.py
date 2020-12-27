from os import MFD_HUGE_1MB
from aocd.models import Puzzle
from collections import Counter, defaultdict
from itertools import product
import math
import re

def part1(decks):
    
    w = 0
    while all(len(i) > 0 for i in decks):
        w = 0 if decks[0][0] > decks[1][0] else 1
        l = (w+1)%2
        decks[w] = decks[w][1:] + [decks[w][0]] + [decks[l][0]]
        decks[l] = decks[l][1:]
    
    return sum(v*(len(decks[w])-i) for i,v in enumerate(decks[w]))

def part2(decks):
    memory = set()
    w, l = 0, 1
    while all(len(i) > 0 for i in decks):
        if repr(decks) in memory:
            w = 0
            break
        else:
            memory.add(repr(decks))
            recurse = all(len(d)-1 >= d[0] for d in decks) 
            if recurse:
                new_deck = [d[1:1+d[0]] for d in decks]
                w, _ = part2(new_deck)
            else:
                w = 0 if decks[0][0] > decks[1][0] else 1
        l = (w+1)%2
        decks[w] = decks[w][1:] + [decks[w][0]] + [decks[l][0]]
        decks[l] = decks[l][1:]

    return w, sum(v*(len(decks[w])-i) for i,v in enumerate(decks[w]))
    

PUZZLE = Puzzle(year=2020,day=22)
INPUT = PUZZLE.input_data

decks = []
for p in INPUT.split('\n\n'):
    deck = list(map(int,list(p.split('\n'))[1:]))
    decks.append(deck)

#PUZZLE.answer_a = part1(decks)
w, PUZZLE.answer_b = part2(decks)
