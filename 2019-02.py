from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
from itertools import product
import queue

import intcode2019
puzzle = Puzzle(year=2019,day=2)
lines = puzzle.input_data



for noun,verb in product(range(69,70), range(100)):
    program = deepcopy(lines)
    tweak = program.split(',')
    tweak[1] = str(noun)
    tweak[2] = str(verb)
    program = ','.join(tweak)
    program = intcode2019.parse(program)

    if program.startswith('19690720'):
        bla = 100*noun + verb
        break
