from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=17)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter
from operator import itemgetter
import networkx as nx
import math as m

xt = list(range(20,30+1))
yt = list(range(-10,-5+1))

xt = list(range(102,157+1))
yt = list(range(-146,-90+1))

def part1():
    maxvy = yt[0]
    maxypos = 0

    for vx0 in range(m.ceil(0.5*(-1+m.sqrt(8*xt[0]+1))), xt[-1]):
        # at what time does the x coordinate fall within the target xt?
        vy0 = xt[-1]
        while vy0 > maxvy:
            # y is 0 again after 2*vy+1 steps
            t = 2*vy0+1
            vx = vx0-t
            vy = -vy0
            x, y = max(vx0*(vx0+1)//2 - vx*(vx+1)//2, vx0*(vx0+1)//2), 0
            while y >= yt[0]:
                vx = max(0,vx-1)
                vy -= 1
                x,y = x+vx, y+vy
                if x in xt and y in yt:
                    if vy0 > maxvy and vy0 > 0:
                        maxypos = max(vy0*(vy0+1)//2,maxypos)
                        maxvy = vy0
                        break
            vy0 -= 1
    return maxypos


# puzzle.answer_a = part1()

def part2():
    num_vel = 0

    for vx0 in range(m.ceil(0.5*(-1+m.sqrt(8*xt[0]+1))), xt[-1]+1):
        # at what time does the x coordinate fall within the target xt?
        vy0 = xt[-1]
        while vy0 >= yt[0]:
            x,y = 0,0
            vx, vy = vx0, vy0
            while y >= yt[0]:
                x,y = x+vx, y+vy
                vx = max(0,vx-1)
                vy -= 1
                if x in xt and y in yt:
                    num_vel += 1
                    break
            vy0 -= 1
    return num_vel

puzzle.answer_b = part2()


        

