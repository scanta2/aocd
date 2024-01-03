from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=7)
from copy import deepcopy
import re

def part1(input):
    hpf, fuelf = -1, int(1e9)
    hps = [int(i) for i in input.split(',')]
    for hp in range(min(hps), max(hps)+1):
        fuel = sum(abs(i-hp) for i in hps)
        if fuel < fuelf:
            hpf, fuelf = hp, fuel
    return fuelf

def part2(input):
    hpf, fuelf = -1, int(1e9)
    hps = [int(i) for i in input.split(',')]
    for hp in range(min(hps), max(hps)+1):
        fuel = sum(abs(i-hp)*(abs(i-hp)+1)//2 for i in hps)
        if fuel < fuelf:
            hpf, fuelf = hp, fuel
    return fuelf


# puzzle.answer_a = part1(puzzle.input_data)
puzzle.answer_b = part2(puzzle.input_data)
