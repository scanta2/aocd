from aocd.models import Puzzle
from aocd.transforms import lines, numbers

day = 2
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

shape_value = {'X': 1, 'Y': 2, 'Z': 3}
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}

def outcome_parta(a,b):
    if a == win[b]:
        return 6
    elif a == draw[b]:
        return 3
    else:
        return 0

outcome_partb = {'X': 0, 'Y': 3, 'Z': 6}
win_partb = {v: k for k, v in win.items()}
draw_partb = {v: k for k, v in draw.items()}
lose_partb = {'A': 'Z', 'B': 'X', 'C': 'Y'}

def part_a():
    score = 0
    for line in data:
        a,b = line.split(' ')
        score += shape_value[b] + outcome_parta(a,b)
    return score

puzzle.answer_a = part_a()

def part_b():
    score = 0
    for line in data:
        a,b = line.split(' ')
        outcome = outcome_partb[b]
        if outcome == 6:
            score += shape_value[win_partb[a]]
        elif outcome == 3:
            score += shape_value[draw_partb[a]]
        else:
            score += shape_value[lose_partb[a]]
        score += outcome
    return score

puzzle.answer_b = part_b()