from aocd.models import Puzzle

import intcode2019

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
from itertools import product
import queue
puzzle = Puzzle(year=2019,day=5)
lines = puzzle.input_data

lines = intcode2019.parse(lines,input='5')

