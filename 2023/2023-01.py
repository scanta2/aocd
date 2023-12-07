from aocd.models import Puzzle
import re
import string

day = 1
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

digits = string.digits

subs = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

subs_rev = {k[::-1]: v for (k,v) in subs.items()}

def first_digit(line, subs) -> int:
    for i, l in enumerate(line):
        if l in digits:
            return int(l)
        elif subs:
            for key, val in subs.items():
                if line[i:].startswith(key):
                    return val
    return 0

def compute_sum(data, subs=None, subs_rev=None):
    sum = 0
    for line in data:
        sum += 10*first_digit(line,subs) + \
                  first_digit(line[::-1],subs_rev)
    print(sum)
    return sum

puzzle.answer_a = (compute_sum(data))
puzzle.answer_b = (compute_sum(data, subs=subs, subs_rev=subs_rev))