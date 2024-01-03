from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=16)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter
from operator import itemgetter
import networkx as nx
import math

hex_string = puzzle.input_data
integer = int(hex_string, 16)

bin_string = format(integer, '0'+str(len(hex_string)*4)+'b')

def part1(pos):
    V = int(bin_string[pos:pos+3],2)
    T = int(bin_string[pos+3:pos+6],2)
    if T == 4: # literal value
        first = pos+6
        number = ''
        while True:
            if bin_string[first] == '0':
                break
            first += 5
        first += 5        
        return V, first
    else:
        I = int(bin_string[pos+6],2)
        if I == 0:
            L = int(bin_string[pos+7:pos+22],2)
            start_pos = pos+22
            end_pos = start_pos+L
            while start_pos < end_pos:
                subV, start_pos = part1(start_pos)
                V += subV
            return V, start_pos
        else:
            L = int(bin_string[pos+7:pos+18],2)
            start_pos = pos+18
            for sub in range(L):
                subV, start_pos = part1(start_pos)
                V += subV
            return V, start_pos

def part2(pos):
    V = int(bin_string[pos:pos+3],2)
    T = int(bin_string[pos+3:pos+6],2)
    if T == 4: # literal value
        first = pos+6
        number = ''
        while True:
            number += bin_string[first+1:first+5]
            if bin_string[first] == '0':
                break
            first += 5
        first += 5        
        return int(number,2), first
    else:
        values = []
        I = int(bin_string[pos+6],2)
        if I == 0:
            L = int(bin_string[pos+7:pos+22],2)
            start_pos = pos+22
            end_pos = start_pos+L
            while start_pos < end_pos:
                subV, start_pos = part2(start_pos)
                values.append(subV)
        else:
            L = int(bin_string[pos+7:pos+18],2)
            start_pos = pos+18
            for sub in range(L):
                subV, start_pos = part2(start_pos)
                values.append(subV)
        if T == 0:
            return sum(values), start_pos
        elif T == 1:
            return math.prod(values), start_pos
        elif T == 2:
            return min(values), start_pos
        elif T == 3:
            return max(values), start_pos
        elif T == 5:
            return 1 if values[0] > values[1] else 0, start_pos
        elif T == 6:
            return 1 if values[0] < values[1] else 0, start_pos
        elif T == 7:
            return 1 if values[0] == values[1] else 0, start_pos

# V, _  = part1(0)
# puzzle.answer_a = V

V, _ = part2(0)
puzzle.answer_b = V
