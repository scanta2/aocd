from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=5)
from copy import deepcopy
import re

def part1(input):
    points = Counter()
    for line in input:
        x1,y1,x2,y2 = [int(i) for i in re.findall('[0-9]+',line)]
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1,x2+1):
                points[(i,y1)] += 1
        elif x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1,y2+1):
                points[(x1,i)] += 1
    return (sum(points[i] > 1 for i in points))

def part2(input):
    points = Counter()
    for line in input:
        x1,y1,x2,y2 = [int(i) for i in re.findall('[0-9]+',line)]
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1,x2+1):
                points[(i,y1)] += 1
        elif x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1,y2+1):
                points[(x1,i)] += 1
        else:
            incx = 1 if x2 > x1 else -1
            incy = 1 if y2 > y1 else -1
            nx, ny = x1, y1
            while (nx,ny) != (x2+incx, y2+incy):
                points[(nx,ny)]+=1
                nx += incx
                ny += incy
    return (sum(points[i] > 1 for i in points))
        

puzzle.answer_a = part1(puzzle.input_data.split('\n'))
puzzle.answer_b = part2(puzzle.input_data.split('\n'))
