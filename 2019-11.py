from aocd.models import Puzzle
import intcode2019
from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter, deque
from itertools import product, permutations
from math import sqrt, atan2, pi
from functools import cmp_to_key
from fractions import gcd

puzzle = Puzzle(year=2019,day=11)
memory = puzzle.input_data.split('\n')
memory = intcode2019.convert(memory[0])

panels = defaultdict(int)
position = 0j
panels[position] = 1
direction = 1j

dirs = {'0': 1j, '1': -1j}

resume = 0
relative_base = 0
while resume != -1:
    inp = deque()
    inp.append(str(panels[position]))
    memory, output, resume, relative_base = intcode2019.parse(memory,inp,resume, relative_base)
    panels[position] = int(output[0])
    direction *= dirs[output[1]]
    position += direction


minx = min([x.real for x in panels])
maxx = max([x.real for x in panels])
miny = min([x.imag for x in panels])
maxy = max([x.imag for x in panels])

rows = maxy-miny+1
cols = maxx-minx+1
id_reg = [' '*int(cols) for i in range(int(rows))]
for panel in panels:
    if panels[panel] == 1:
        row = list(id_reg[int(panel.imag-miny)])
        row[int(panel.real-minx)] = 'X'
        id_reg[int(panel.imag-miny)] = ''.join(row)
[print(i) for i in reversed(id_reg)]