import numpy as np
import re
import itertools
from aocd.models import Puzzle
from copy import deepcopy
import collections
import operator
from collections import defaultdict
puzzle = Puzzle(day=25,year=2022)
data = puzzle.input_data.splitlines()

convs2d = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
convd2s = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-', 5: '0'}


# data = """1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122""".splitlines()

def snafu2dec(snafu):
    return sum(convs2d[num]*5**i for i, num in enumerate(reversed(snafu)))

def dec2snafu(dec):
    conv = ''
    rem = 0
    while dec:
        m = dec%5 + rem
        rem = 0 if m < 3 else 1
        conv = conv + convd2s[m]
        dec //= 5
    return conv[-1::-1]

tot = 0
for line in data:
    tot += snafu2dec(line)
print(tot)
print(dec2snafu(tot))
print(snafu2dec(dec2snafu(tot)))