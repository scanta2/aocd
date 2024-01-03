from aocd.models import Puzzle
from aocd.transforms import lines, numbers
import string

day = 3
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()
letters = string.ascii_lowercase + string.ascii_uppercase

def score(*groups):
    item, = set.intersection(*[set(i) for i in groups])
    return letters.find(item)+1

def part_a():
    return sum(score(sack[:len(sack)//2], sack[len(sack)//2:]) for sack in data)

puzzle.answer_a = part_a()

def part_b():
    step = 3
    return sum(score(a,b,c) for (a,b,c) in (data[ig:ig+step]
               for ig in range(0,len(data),step)))

puzzle.answer_b = part_b()

print(puzzle.answer_a)
print(puzzle.answer_b)