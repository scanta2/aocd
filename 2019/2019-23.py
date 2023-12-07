import networkx as nx
import intcode2019 as intc
from collections import defaultdict, deque
from aocd.models import Puzzle
import string

puzzle = Puzzle(year=2019,day=23)
instructions = puzzle.input_data

intcode = [[] for i in range(50)]
output = [[] for i in range(50)]
instr_ptr = [0 for i in range(50)]
relative_base = [0 for i in range(50)]

queue = defaultdict(list)

for i in range(50):
    intcode[i] = intc.convert(instructions)
    inp = deque([str(i)])
    intcode[i], output[i], instr_ptr[i], relative_base[i] = intc.parse(intcode[i], input=inp)
    # print(output[i])

nat_y = []
net_idle = 0

while True:
    if len(queue) == 0:
        net_idle += 1
    else:
        net_idle = 0
    for i in range(50):
        inp = deque([-1]) if i not in queue.keys() else deque(queue[i])
        if i in queue.keys():
            queue.pop(i)
        intcode[i], output[i], instr_ptr[i], relative_base[i] = intc.parse(intcode[i], input=inp, resume=instr_ptr[i], relative_base=relative_base[i])
        for o in range(0,len(output[i]), 3):
            queue[int(output[i][o])] += (output[i][o+1], output[i][o+2])
    if len(queue) == 1 and 255 in queue.keys():
        nat_packet = [queue[255][-2], queue[255][-1]]
        if len(nat_y) and nat_y[-1] == nat_packet[1]:
            print(nat_y[-1])
            raise
        nat_y += [nat_packet[1]]
        queue[0] += nat_packet

            