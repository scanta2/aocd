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

row_f = 3010
col_f = 3019

row = 1
col = 1
row_p = 1
col_p = 1
value = 20151125
value_p = 20151125


while row != row_f or col != col_f:
    value_p = value
    if row - 1 == 0:
        row, col, row_p, col_p = col+1, 1, row, col
    else:
        row, col, row_p, col_p = row-1, col+1, row, col
    value = (value_p*252533)%33554393
print(value)

    