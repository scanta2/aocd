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
def recurse(spring, records):
    if len(records) == 0 and '#' in spring:
        return 0
    record0, other_records = records[0], records[1:]    

    count = 0
    
    # the max length of this block needs to account that there
    # can be a block at the end of the string that can satisfy all
    # the records
    min_size_block_right = sum(records) + len(other_records)
    for i in range(len(spring)-min_size_block_right+1):
        # let's assume record zero is on the left of the string
        left, right = spring[i:i+record0], spring[i+record0:]

        # left can contain a split of length record0
        if all(c in "#?" for c in left):
            # we are sure left contains the split because we are done
            if len(other_records) == 0 and all(c in ".?" for c in right):
                count += 1
            elif len(right) > 0 and right[0] in '.?':
                # the left side can contain a split matching record0
                # and there is a pivot point and more stuff to check
                count += recurse(right[1:], other_records)
        
        # left can't contain a split, but if the first character
        # is # we can cut all the recursions
        if left[0] == '#':
            break
    
    return count

def solve(copies=1):
    res = 0

    for line in data:
        ospring, orecord = line.split()
        spring = copy(ospring)
        record = copy(orecord)
        for i in range(1,copies):
            spring += '?' + ospring
            record += ',' + orecord 
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
