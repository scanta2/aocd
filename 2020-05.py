from aocd.models import Puzzle
import string
import re

def iter_bp_id(INPUT):
    for bp in INPUT:
        yield int(bp.translate(str.maketrans('FLBR','0011')),2)

PUZZLE = Puzzle(year=2020,day=5)
INPUT = PUZZLE.input_data.split('\n')
ids = set(iter_bp_id(INPUT))
PUZZLE.answer_a = max(ids)

# faster answer b
min_id = min(ids)
for i,id in enumerate(ids):
    if i != id-min_id:
        PUZZLE.answer_b = i+min_id
        break