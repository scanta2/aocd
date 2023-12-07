from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from collections import deque
from string import ascii_uppercase
import re

day = 6
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()
data = data[0]

def parta():
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == 4:
            return i+4

puzzle.answer_a = parta()


def partb(num_distinct):
    for i in range(len(data)-num_distinct):
        if len(set(data[i:i+num_distinct])) == num_distinct:
            return i+num_distinct

puzzle.answer_b = partb(14)
