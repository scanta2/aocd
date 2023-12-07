from aocd.models import Puzzle
from math import pow
import string
import re

def part1(INPUT):
    pos = complex(0)
    dir = complex(1)
    actions = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1, 'L': 1j, 'R': -1j, 'F': 1}
    for line in INPUT:
        action, move = line[0], int(line[1:])
        if action in 'NSEW':
            pos += actions[action]*move
        elif action in 'LR':
            for i in range(move//90):
                dir *= actions[action]
        else:
            pos += dir*move
    return int(abs(pos.real) + abs(pos.imag))

def part2(INPUT):
    wp = 10+1j
    pos = complex(0)
    actions = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1, 'L': 1j, 'R': -1j, 'F': 1}
    for line in INPUT:
        action, move = line[0], int(line[1:])
        if action in 'NSEW':
            wp += actions[action]*move
        elif action in 'LR':
            for i in range(move//90):
                wp *= actions[action]
        else:
            pos += wp*move
    return int(abs(pos.real) + abs(pos.imag))

PUZZLE = Puzzle(year=2020,day=12)
INPUT = PUZZLE.input_data.splitlines()
PUZZLE.answer_a = part1(INPUT)
PUZZLE.answer_b = part2(INPUT)