from aocd.models import Puzzle
import re
import string
from math import prod
from itertools import chain

day = 2
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

summ = 0

def is_game_possible(game):
    cubes = game.split(', ')
    return all(max_cubes[col] >= int(num) for num, col in (cube.split(' ') for cube in cubes))

for i, line in enumerate(data):
    games = line.split(': ')[-1].split('; ')
    if all(is_game_possible(game) for game in games):
        summ += i+1
puzzle.answer_a = summ

def power(line):
    powers = {'red': [0], 'green': [0], 'blue': [0]}
    cubes = list(chain.from_iterable(game.split(', ') for game in line.split(': ')[-1].split('; ')))
    for cube in cubes:
        num, col = cube.split(' ')
        powers[col].append(int(num))
    return prod(max(value) for value in powers.values())

puzzle.answer_b = sum(power(line) for line in data)



