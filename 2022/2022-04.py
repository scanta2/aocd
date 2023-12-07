from aocd.models import Puzzle
from aocd.transforms import lines, numbers
import re

day = 4
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

def split_line(line):
    numbers = [int(i) for i in re.split(',|-', line)]
    step = 2
    ranges = [tuple(numbers[i:i+step]) for i in range(0,len(numbers),step)]
    c = list(zip(*ranges))
    d = (max(c[0]), min(c[1]))
    return ranges, d
    
def parta_line(line):
    ranges, overlap = split_line(line)
    return any(overlap == i for i in ranges)

def part_a():
    return sum(parta_line(line) for line in data)

puzzle.answer_a = part_a()

def partb_line(line):
    _, overlap = split_line(line)
    return overlap[0] <= overlap[1]

def part_b():
    return(sum(partb_line(line) for line in data))

puzzle.answer_b = part_b()

print(puzzle.answer_a)
print(puzzle.answer_b)
