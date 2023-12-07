from aocd.models import Puzzle
from aocd.transforms import lines, numbers

day = 1
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n\n')

calories_per_elf = [sum(int(i) for i in lines(group)) for group in data]
calories_per_elf = sorted(calories_per_elf, reverse=True)

def part_a():
    return calories_per_elf[0]

puzzle.answer_a = part_a()

def part_b():
    return sum(calories_per_elf[:3])

puzzle.answer_b = part_b()