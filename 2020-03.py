from aocd.models import Puzzle
from math import prod
import re

def part1(INPUT,slope):
    right, down = slope
    x = -right
    count = 0
    for y,line in enumerate(INPUT):
        if y%down == 0:
            x = (x+right)%len(line)
            if line[x] == '#':
                count += 1
    return count

def part2(INPUT, slopes):
    return prod([part1(INPUT,slope) for slope in slopes])

PUZZLE = Puzzle(year=2020,day=3)
INPUT = PUZZLE.input_data.split('\n')
slope = (3,1)
PUZZLE.answer_a = part1(INPUT,slope)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
PUZZLE.answer_b = part2(INPUT,slopes)