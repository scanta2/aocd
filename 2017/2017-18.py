from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict
import queue
puzzle = Puzzle(year=2017,day=18)
lines = puzzle.input_data.split('\n')

# lines = ['set a 1', 'add a 2', 'mul a a', 'mod a 5',
# 'snd a',
# 'set a 0',
# 'rcv a',
# 'jgz a -1',
# 'set a 1',
# 'jgz a -2']

# lines = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']

# registers = defaultdict(int)

# last_sound_played = -1
# last_sound_recovered = -1
# jump = 1

# def parsepart1(line):
#     global jump
#     global last_sound_played
#     global last_sound_recovered
#     jump = 1
#     tokens = line.split(' ')
#     if tokens[0] == 'snd':
#         last_sound_played = int(tokens[1]) if tokens[1].lstrip('-').isdigit() else registers[tokens[1]]
#     elif tokens[0] == 'set':
#         registers[tokens[1]] = int(tokens[2]) if tokens[2].lstrip('-').isdigit() else registers[tokens[2]]
#     elif tokens[0] == 'add':
#         registers[tokens[1]] += int(tokens[2]) if tokens[2].lstrip('-').isdigit() else registers[tokens[2]]
#     elif tokens[0] == 'mul':
#         registers[tokens[1]] *= int(tokens[2]) if tokens[2].lstrip('-').isdigit() else registers[tokens[2]]
#     elif tokens[0] == 'mod':
#         registers[tokens[1]] %= int(tokens[2]) if tokens[2].lstrip('-').isdigit() else registers[tokens[2]]
#     elif tokens[0] == 'rcv':
#         if registers[tokens[1]] != 0 and last_sound_recovered == -1:
#             last_sound_recovered = last_sound_played
#     elif tokens[0] == 'jgz':
#         if registers[tokens[1]] != 0:
#             jump = int(tokens[2]) if tokens[2].lstrip('-').isdigit() else registers[tokens[2]]

# line_nr = 0
# while line_nr < len(lines) and line_nr >= 0:
#     parsepart1(lines[line_nr])
#     line_nr += jump
#     if last_sound_recovered != -1:
#         break
# print(last_sound_recovered)
registers_p2 = [defaultdict(int), defaultdict(int)]
registers_p2[0]['p'] = 0
registers_p2[1]['p'] = 1
jump_p2 = [1, 1]
line_nr_p2 = [0, 0]
snd_count = [0, 0]
rcv_queue = [[], []]
deadlock = False
curr_id = 0
next_id = 1
terminated = [False, False]

def value(token):
    if token in 'qwertyuiopasdfghjklzxcvbnm':
        return registers_p2[curr_id][token]
    else:
        return int(token)

def parsepart2(line):
    global deadlock
    jump_p2[curr_id] = 1
    tokens = line.split(' ')
    if tokens[0] == 'snd':
        rcv_queue[next_id].append(value(tokens[1]))
        snd_count[curr_id] += 1
    elif tokens[0] == 'set':
        registers_p2[curr_id][tokens[1]] = value(tokens[2])
    elif tokens[0] == 'add':
        registers_p2[curr_id][tokens[1]] += value(tokens[2])
    elif tokens[0] == 'mul':
        registers_p2[curr_id][tokens[1]] *= value(tokens[2])
    elif tokens[0] == 'mod':
        registers_p2[curr_id][tokens[1]] %= value(tokens[2])
    elif tokens[0] == 'rcv':
        # Check other queue
        if rcv_queue[curr_id] == []:
            deadlock = True
        else:
            registers_p2[curr_id][tokens[1]] = rcv_queue[curr_id].pop(0)
    elif tokens[0] == 'jgz':
        if value(tokens[1]) > 0:
            jump_p2[curr_id] = value(tokens[2])

while not deadlock and not terminated[curr_id]:
    while line_nr_p2[curr_id] < len(lines) and line_nr_p2[curr_id] >= 0 and not deadlock:
        # print(lines[line_nr_p2[curr_id]])
        parsepart2(lines[line_nr_p2[curr_id]])
        #print(registers_p2[curr_id])
        line_nr_p2[curr_id] += jump_p2[curr_id]
    if deadlock:
        line_nr_p2[curr_id] -= jump_p2[curr_id]
    else:
        terminated[curr_id] = True
    deadlock = all([i == [] for i in rcv_queue])
    curr_id, next_id = next_id, curr_id
    print(snd_count)