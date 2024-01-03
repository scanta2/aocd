from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
from itertools import product
import queue
puzzle = Puzzle(year=2019,day=4)
lines = puzzle.input_data.split('\n')

def matches_rule(password):
    monotonic = all(int(password[i]) <= int(password[i+1]) for i in range(0,len(password)-1))
    if not monotonic:
        return False
    adj_idx = list(password[i] == password[i+1] for i in range(0,len(password)-1))
    adj_idx.append(False)
    adj_count = adj_idx.count(True)
    two_adj = adj_count >= 1
    if not two_adj:
        return False
    nolargegroup = adj_count == 1
    if adj_count > 1:
        nolargegroup |= adj_idx[0] and not adj_idx[1]
        checks = [not adj_idx[i] and adj_idx[i+1] and not adj_idx[i+2] for i in range(0,4)]
        nolargegroup |= any(checks)
    return nolargegroup

pass_range = list(int(i) for i in re.findall('\d+', lines[0]))

nr_valid = [matches_rule(str(i)) for i in range(pass_range[0], pass_range[1])].count(True)
print(nr_valid)