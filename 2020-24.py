from aocd.models import Puzzle
from collections import Counter, defaultdict
from itertools import product
import math
import re

def part1(INPUT):
    moves = {'se': -1+1j, 'ne': 1+1j, 'nw': 1-1j, 'sw': -1-1j, 'e': 2j, 'w': -2j}
    color_flips = {'B': 'W', 'W': 'B'}
    tiles = dict()
    for line in INPUT.splitlines():
        tile = 0
        while len(line) != 0:
            if any(line.startswith(c) for c in ['se','sw','ne','nw']):
                tile += moves[line[:2]]
                line = line[2:]
            else:
                tile += moves[line[:1]]
                line = line[1:]
        if tile not in tiles:
            tiles[tile] = 'B'
        else:
            tiles[tile] = color_flips[tiles[tile]]
    return sum(1 for i in tiles.values() if i == 'B'), tiles

def part2(tiles,ndays):
    new_tiles = dict()
    moves = {'se': -1+1j, 'ne': 1+1j, 'nw': 1-1j, 'sw': -1-1j, 'e': 2j, 'w': -2j}
    for _ in range(ndays):
        for k,v in tiles.items():
            adjB = sum(1 for i in moves.values() if k+i in tiles and tiles[k+i]=='B')
            if v == 'B':
                new_tiles[k] = 'W' if adjB == 0 or adjB > 2 else 'B'
            else:
                new_tiles[k] = 'B' if adjB == 2 else 'W'
            for i in moves.values():
                kk = k+i
                if kk not in tiles:
                    adjB = sum(1 for j in moves.values() if kk+j in tiles and tiles[kk+j]=='B')
                    new_tiles[kk] = 'B' if adjB == 2 else 'W'
        new_tiles, tiles = tiles, new_tiles
    return sum(1 for i in tiles.values() if i == 'B')
                

PUZZLE = Puzzle(year=2020,day=24)
INPUT = PUZZLE.input_data
PUZZLE.answer_a, tiles = part1(INPUT)
PUZZLE.answer_b = part2(tiles,100)



