from aocd.models import Puzzle
from collections import Counter, defaultdict
from itertools import product
import math
import re

def part1(cups,n_moves):
    curr_idx = 0
    pickup = []
    for i in range(n_moves):
        curr_idx = i%len(cups)
        curr_cup = cups[curr_idx]
        if curr_idx+4 < len(cups):
            pickup = cups[curr_idx+1:curr_idx+4]
            cups = cups[:curr_idx+1] + cups[curr_idx+4:]
        else:
            pickup = cups[curr_idx+1:]
            cups = cups[:curr_idx+1]
            lp = len(pickup)
            pickup += cups[0:3-lp]
            cups = cups[3-lp:]
        destination = curr_cup - 1
        while destination not in cups:
            destination -= 1
            if all(destination < c for c in cups):
                destination = max(cups)
        d_idx = cups.index(destination)
        cups = cups[:d_idx+1] + pickup + cups[d_idx+1:]
        # rotate back
        new_idx = cups.index(curr_cup)
        if new_idx > curr_idx:
            diff = new_idx - curr_idx
            cups = cups[diff:] + cups[0:diff]
        elif new_idx < curr_idx:
            diff = curr_idx - new_idx
            cups = cups[-diff:] + cups[0:-diff]
    idx = cups.index(1)
    cups.remove(1)
    return ''.join(str(i) for i in cups[idx:] + cups[:idx])


def part2(cups,n_moves):
    curr_idx = 0
    pickup = []
    for i in range(n_moves):
        curr_idx = i%len(cups)
        curr_cup = cups[curr_idx]
        if curr_idx+4 < len(cups):
            pickup = cups[curr_idx+1:curr_idx+4]
            cups = cups[:curr_idx+1] + cups[curr_idx+4:]
        else:
            pickup = cups[curr_idx+1:]
            lp = len(pickup)
            pickup += cups[0:3-lp]
            cups = cups[3-lp:curr_idx+1]
        destination = curr_cup - 1
        lb = 1
        if 1 in pickup:
            lb = 2
            if 2 in pickup:
                lb = 3
                if 3 in pickup:
                    lb = 4
        ub = 1000000
        if 1000000 in pickup:
            ub -= 1
            if ub in pickup:
                ub -=1
                if ub in pickup:
                    ub -= 1
        while destination in pickup:
            destination -= 1
            if destination < lb:
                destination = ub
        d_idx = cups.index(destination)
        cups = cups[:d_idx+1] + pickup + cups[d_idx+1:]
        # rotate back
        new_idx = cups.index(curr_cup)
        if new_idx > curr_idx:
            diff = new_idx - curr_idx
            cups = cups[diff:] + cups[0:diff]
        elif new_idx < curr_idx:
            diff = curr_idx - new_idx
            cups = cups[-diff:] + cups[0:-diff]
    idx = cups.index(1)
    cups.remove(1)
    return cups[idx%len(cups)]*cups[(idx+1)%len(cups)]


PUZZLE = Puzzle(year=2020,day=23)
INPUT = PUZZLE.input_data
cups = [int(i) for i in INPUT]
cups = [int(i) for i in "389125467"]
print(part1(cups,100))
cups = cups + [i for i in range(len(cups)+1,1000001)]
# print(cups[-1])
# print(len(cups))
print(part2(cups,10000000))