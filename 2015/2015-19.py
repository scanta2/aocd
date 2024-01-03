from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter
import queue
from itertools import combinations

puzzle = Puzzle(year=2015,day=19).input_data.split('\n')
# puzzle = """e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOHOHO""".split('\n')

final_molecule = puzzle[-1]


def howmany(string, sub):
    return len([m.start() for m in re.finditer(sub, string)])

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

rules = defaultdict(list)
rev_rules = defaultdict(list)

for i in range(len(puzzle)-2):
    tk = puzzle[i].split(' ')
    rules[tk[0]].append(tk[2])
    rev_rules[tk[2]].append(tk[0])

numRn = howmany(final_molecule,'Rn')
numAr = howmany(final_molecule,'Ar')
numY = howmany(final_molecule,'Y')
numUpper = sum([1 for c in final_molecule if c.isupper()])
print(numUpper - numRn - numAr - 2*numY -1)