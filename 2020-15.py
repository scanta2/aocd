from aocd.models import Puzzle
from collections import defaultdict

def solve(INPUT,final):
    memory = defaultdict(list)
    for t, i in enumerate(INPUT):
        memory[i].append(t)
    last = INPUT[-1]

    for t in range(len(INPUT),final):
        if len(memory[last]) == 1:
            last = 0
        else:
            last = memory[last][-1] - memory[last][-2]
        memory[last].append(t)
    return last



PUZZLE = Puzzle(year=2020,day=15)
INPUT = [int(x) for x in PUZZLE.input_data.split(',')]
PUZZLE.answer_a = solve(INPUT,2020)
PUZZLE.answer_b = solve(INPUT,30000000)