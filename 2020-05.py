from aocd.models import Puzzle
import string
import re

def to_number(input):
    lb = 0
    ub = 2**len(input)-1

    for i in input:
        if i == 'F' or i == 'L':
            ub -= (ub-lb)//2 + 1
        else:
            lb += (ub-lb)//2 + 1
    
    if lb == ub:
        return lb
    else:
        raise

def convert_bp(input):
    row, col = to_number(input[:7]), to_number(input[7:])
    return row*8+col

PUZZLE = Puzzle(year=2020,day=5)
INPUT = PUZZLE.input_data.split('\n')
ids = sorted([convert_bp(bp) for bp in INPUT])
PUZZLE.answer_a = ids[-1]

# slow answer b
for i in range(ids[0],ids[-1]+1):
    if i not in ids:
        PUZZLE.answer_b = i

# faster answer b
min_id = ids[0]
ids = [i-min_id for i in ids]
for i,id in enumerate(ids):
    if i != id:
        PUZZLE.answer_b = i+min_id