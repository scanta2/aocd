from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
puzzle = Puzzle(year=2017,day=16)

numprogs = 16
programs = string.ascii_lowercase[:numprogs]

def parse(line):
    global programs
    if line[0] == 's': #spin
        num = int(re.findall('\d+',line)[0])
        programs = programs[numprogs-num:] + programs[:numprogs-num]
    elif line[0] == 'x': #exchange
        pos = [int(x) for x in re.findall('\d+',line)]
        progList = list(programs)
        progList[pos[0]], progList[pos[1]] = progList[pos[1]], progList[pos[0]]
        programs = ''.join(progList)
    elif line[0] == 'p': #partner
        p1, p2 = line[1], line[3]
        progList = list(programs)
        pos = [progList.index(p1), progList.index(p2)]
        progList[pos[0]], progList[pos[1]] = progList[pos[1]], progList[pos[0]]
        programs = ''.join(progList)


dp = {}

for i in range(1000000000):
    initial = deepcopy(programs)
    if initial not in dp:
        for line in puzzle.input_data.split(','):
            parse(line)
        dp[initial] = (programs, i)
    else:
        first_rep_idx = dp[initial][1]
        break

print(first_rep_idx)
print(len(dp))

eq_index = 1000000000%len(dp)

for key, val in dp.items():
    if val[1] == eq_index:
        print(key)
        break



