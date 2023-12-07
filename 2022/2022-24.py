import numpy as np
import re
import itertools
from aocd.models import Puzzle
from copy import deepcopy
import collections
import operator
from collections import defaultdict
puzzle = Puzzle(day=24,year=2022)
data = puzzle.input_data.splitlines()

# data = """#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#""".splitlines()

walls = []
blizzards = defaultdict(list)

for r, row in enumerate(data):
    for ic, c in enumerate(row):
        if c == "#":
            walls.append((r-1,ic-1))
        elif c == ".":
            continue
        else:
            blizzards[c].append([r-1,ic-1])
pass

blizzhor = len(data[0])-2
blizzvert = len(data)-2
moves = ((0,0),(-1,0),(1,0),(0,1),(0,-1))

def parta(start,end,part_a = True):
    global blizzards
    positions = {start}
    minute = 0
    while True:
        minute += 1
        new_positions = set()
        # move blizzards
        new_blizzards = defaultdict(list)
        new_blizzards['<'] = [(r,(c-1)%blizzhor) for r,c in blizzards['<']]
        new_blizzards['>'] = [(r,(c+1)%blizzhor) for r,c in blizzards['>']]
        new_blizzards['^'] = [((r-1)%blizzvert,c) for r,c in blizzards['^']]
        new_blizzards['v'] = [((r+1)%blizzvert,c) for r,c in blizzards['v']]
        
        blizz_cells = set.union(*[set(i) for i in new_blizzards.values()])

        for (r,c) in positions:
            for (rm,cm) in moves:
                newp = (r+rm,c+cm)
                if newp == end:
                    if part_a:
                        puzzle.answer_a = minute
                    blizzards = new_blizzards
                    return minute
                if newp != start and (newp[0] < 0 or newp[0] >= blizzvert or newp[1] < 0 or newp[1] >= blizzhor):
                    continue
                if newp not in blizz_cells:
                    new_positions.add(newp)
        blizzards = new_blizzards
        positions = new_positions

start = (-1,0)
end = (blizzvert,blizzhor-1)
parta(start,end)
walls = []
blizzards = defaultdict(list)

for r, row in enumerate(data):
    for ic, c in enumerate(row):
        if c == "#":
            walls.append((r-1,ic-1))
        elif c == ".":
            continue
        else:
            blizzards[c].append([r-1,ic-1])
puzzle.answer_b = parta(start,end,False) + parta(end,start,False) + parta(start,end,False)






