from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import networkx as nx
import functools

day = 12
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split('\n')
    
@functools.cache
def recurse(springs, records, num_done_rec0 = 0):
    # base case, only dots are left in the spring
    if not springs:
        # valid solution if no more records and no open groups
        return 1 if not records and num_done_rec0 == 0 else 0
    
    num_sol = 0

    possibles = '#.' if springs[0] == '?' else springs[0]
    for possible in possibles:
        if possible == '#':
            # continue the current group
            num_sol += recurse(springs[1:], records, num_done_rec0+1)
        else:
            # if still in group
            if num_done_rec0 > 0:
                # close the group
                if records and records[0] == num_done_rec0:
                    num_sol += recurse(springs[1:], records[1:], 0)
            else:
                # move on
                num_sol += recurse(springs[1:], records, 0)
    return num_sol

def solve(copies=1):
    res = 0

    for line in data:
        ospring, orecord = line.split()
        spring = copy(ospring)
        record = copy(orecord)
        for i in range(1,copies):
            spring += '?' + ospring
            record += ',' + orecord 
        spring += '.' # simplify ending
        record = tuple([int(i) for i in record.split(',')])
        ans = recurse(spring, tuple(record))
        print(ans)
        res += ans

    print(res)
    if debug:
        return None
    else:
        return res


puzzle.answer_a = solve(1)
puzzle.answer_b = solve(5)
