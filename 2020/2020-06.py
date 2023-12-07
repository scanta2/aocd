from aocd.models import Puzzle
import string
import re

def group_answers1_iter(groups):   
    for group in groups:
        group_ = ''.join(set(group.replace('\n','')))
        yield len(group_)

def part1(groups):
    return sum(group_answers1_iter(groups))

def group_answers2_iter(groups):   
    for group in groups:
        people = [set(person) for person in group.splitlines()]
        intersection = set.intersection(*people)
        yield len(intersection)

def part2(groups):
    return sum(group_answers2_iter(groups))


PUZZLE = Puzzle(year=2020,day=6)
INPUT = PUZZLE.input_data
groups = INPUT.split('\n\n')
PUZZLE.answer_a = part1(groups)
PUZZLE.answer_b = part2(groups)

