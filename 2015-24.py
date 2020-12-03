from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter, OrderedDict
import queue
from itertools import combinations
from math import sqrt, floor, ceil, prod
import operator

packages = set([int(i) for i in Puzzle(year=2015,day=24).input_data.split('\n')])
parts = 4
tot = sum(packages)//parts

def hasSum(lst, sub):
    for y in range(1,len(lst)): 
        for x in (z for z in combinations(lst, y) if sum(z) == tot):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return reduce(operator.mul, x, 1)
print(hasSum(packages, parts))


