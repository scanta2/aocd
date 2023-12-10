from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import networkx as nx

day = 10
year = 2023

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n')

def start_and_dir():
    # find S
    datalin = ''.join(chain(*data))
    idxS = datalin.index('S')
    iS, jS = idxS//len(data[0]), idxS%len(data[0])
    start = complex(jS,iS)

    possibleS = set('|-LJ7F')
    if start.imag > 0:
        upN = data[iS-1][jS]
        if upN in '|F7':
            possibleS -= set('-7F')
    if start.imag < len(data)-1:
        downN = data[iS+1][jS]
        if downN in '|LJ':
            possibleS -= set('-LJ')
    if start.real > 1:
        leftN = data[iS][jS-1]
        if leftN in '-FL':
            possibleS -= set('|FL')
    if start.real < len(data[0])-1:
        rightN = data[iS][jS+1]
        if rightN in '-7J':
            possibleS -= set('|7J')
    onlyS = list(possibleS)[0]
    data[iS] = data[iS].replace('S',onlyS)
    if onlyS in '|JL':
        return (start, -1j)
    elif onlyS in '7F':
        return (start, 1j)
    else:
        return (start, 1)

def part1():

    def update_dir(value, dir):
        update_instr = {
            ('L', 1j):  1, ('L',-1): -1j,
            ('J', 1j): -1, ('J', 1): -1j,
            ('7',-1j): -1, ('7', 1):  1j,
            ('F',-1j):  1, ('F',-1):  1j,
            ('-',  1):  1, ('-',-1):  -1,
            ('|', 1j): 1j, ('|',-1j): -1j
            }
        return update_instr[(value,dir)]

    start, dir = start_and_dir()
    pos = start
    loop_tiles = []
    while True:
        loop_tiles.append((int(pos.imag),int(pos.real)))
        if pos == start and len(loop_tiles) != 1:
            break
        pos += dir   
        value = data[int(pos.imag)][int(pos.real)]
        dir = update_dir(value,dir)
    return len(loop_tiles)//2, loop_tiles

res, loop_tiles = part1()
puzzle.answer_a = res


def part2():
    d_loop_tiles = [(2*a,2*b) for (a,b) in loop_tiles]
    edges = list(zip(d_loop_tiles[:-1], d_loop_tiles[1:]))
    # get all the vertical edges sorted for ascending rows first
    v_edges = [sorted(e) for e in edges if e[0][-1] == e[1][-1]]
    

    inside_tiles = set()

    for i,j in product(range(2*len(data)),range(2*len(data[0]))):
        ni, nj = i//2, j//2
        if (ni,nj) in loop_tiles or (ni,nj) in inside_tiles:
            continue
        # ray-casting algorithm
        # count how many v_edges are crossed going right,
        # even: point is out, odd: point is in
        if sum(1 for (a,b) in v_edges if a[1]>j and a[0]<=i<=b[0]) % 2 == 1:
            inside_tiles.add((ni,nj))
    return len(inside_tiles)
puzzle.answer_b = part2()
