from aocd.models import Puzzle

import intcode2019

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter,deque
from itertools import product, permutations
import queue
# puzzle = Puzzle(year=2019,day=7)
# program = puzzle.input_data.split('\n')[0]

program = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'

max_signal = 0


for phase in permutations([0,1,2,3,4]):
    memory = [deepcopy(program) for i in range(5)]
    resume = [0,0,0,0,0]
    round = 1
    output = 0
    while any([r != -1 for r in resume]):
        for amplifier in range(5):
            input = deque([str(phase[amplifier]), str(output)]) if round == 1 else deque([str(output)])
            memory[amplifier] , output, resume[amplifier] = intcode2019.parse(deepcopy(memory[amplifier]),input,resume[amplifier])
            output = output[0]
        round += 1
    max_signal = max(max_signal, int(output))
puzzle.answer_b = max_signal