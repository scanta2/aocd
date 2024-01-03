from aocd.models import Puzzle
from time import sleep
from math import floor, ceil
puzzle = Puzzle(year=2019,day=16)
instr = puzzle.input_data

offset = int(instr[0:7])
print('offset: ', offset)

rep = 10000
numphase = 100

old = [int(i) for i in instr for j in range(rep)]
lenold = len(old)
base_pattern = [0, 1, 0, -1]

# for phase in range(numphase):
#     old = [abs(sum([old[(j)]*base_pattern[((j+1)//(i+1)) & 3] for j in range(lenold)]))%10 for i in range(lenold)]
#     print(phase)
# output = ''.join([str(old[i]) for i in range(offset,offset+8)])
# print(output)

from itertools import cycle, accumulate
digits = [int(i) for i in instr]
l = 10000 * len(digits) - offset
i = cycle(reversed(digits))
arr = [next(i) for _ in range(l)]
# Repeatedly take the partial sums mod 10
for _ in range(100):
    arr = [n % 10 for n in accumulate(arr)]
print("".join(str(i) for i in arr[-1:-9:-1]))