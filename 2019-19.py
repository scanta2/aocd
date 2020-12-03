import networkx as nx
from aocd.models import Puzzle
import intcode2019
from itertools import product, permutations
from collections import deque
import string

puzzle = Puzzle(year=2019,day=19)
instr = puzzle.input_data

# beammap = [[' ' for i in range(50)] for j in range(50)]

# count = 0

# for x,y in product(range(50),range(50)):
#     inp = deque([str(x), str(y)])
#     computer = intcode2019.convert(instr)
#     _, output, _, _ = intcode2019.parse(computer,inp)
#     beammap[y][x] = output[0]
#     if beammap[y][x] == '1':
#         count += 1
# print(count)


# start from y at least 100
# find the min x and check that y-99 maxx is in a y-99 maxx+1 is out
# from my previous run I now xmin < y
y = 300
while True:
    if y%100 == 0:
        print(y)
    xmin = 0
    xmax = y
    while True:
        xtry = (xmax+xmin)//2
        xtrym1 = xtry-1

        inp = deque([str(xtry), str(y)])
        computer = intcode2019.convert(instr)
        _, output1, _, _ = intcode2019.parse(computer,inp)
        inp = deque([str(xtrym1), str(y)])
        computer = intcode2019.convert(instr)
        _, output2, _, _ = intcode2019.parse(computer,inp)

        if (output1[0] == '1' and output2[0] == '0'):
            break
        elif output1[0] == '0':
            xmin = xtry
        else:
            xmax = xtry
    inp = deque([str(xtry+100), str(y-99)])
    computer = intcode2019.convert(instr)
    _, output1, _, _ = intcode2019.parse(computer,inp)
    inp = deque([str(xtry+99), str(y-99)])
    computer = intcode2019.convert(instr)
    _, output2, _, _ = intcode2019.parse(computer,inp)
    if output1[0] == '0' and output2[0] == '1':
        break
    y += 1
print(xtry*10000+y-99)





