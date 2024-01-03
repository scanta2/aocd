from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain, product
from collections import defaultdict
from copy import deepcopy

day = 4
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

# data="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

def part1():
    points = 0
    for line in data:
        line = line.split(':')[1]
        winning, have = line.split('|')
        winning = set(re.findall(r'\d+', winning))
        have = set(re.findall(r'\d+', have))
        inter = len(winning.intersection(have))
        if inter > 0:
            points += 2**(inter-1)
    print(points)
    return points

# puzzle.answer_a = part1()

def part2():
    card_copies = [1 for i in range(len(data))]
    for i, line in enumerate(data):
        line = line.split(':')[1]
        winning, have = line.split('|')
        winning = set(re.findall(r'\d+', winning))
        have = set(re.findall(r'\d+', have))
        inter = len(winning.intersection(have))
        for j in range(i+1, i+inter+1):
            if j < len(card_copies):
                card_copies[j] += card_copies[i]
    print(card_copies)
    return sum(card_copies)

puzzle.answer_b = part2()
