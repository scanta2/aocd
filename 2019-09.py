from aocd.models import Puzzle

import intcode2019

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter, deque
from itertools import product, permutations
puzzle = Puzzle(year=2019,day=9)
program = puzzle.input_data

program_intcode = intcode2019.convert(program)
inp = deque(['2'])
# program_intcode = intcode2019.convert('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
# inp = None

new_program, output, curr_instr = intcode2019.parse(program_intcode,inp)
puzzle.answer_b = output[0]