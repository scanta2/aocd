import curses
from curses import wrapper
from aocd.models import Puzzle
import intcode2019
from itertools import product
from collections import deque
puzzle = Puzzle(year=2019,day=17)
instr = puzzle.input_data

intersections = set()

instr = intcode2019.convert(instr)
instr, output, res, base = intcode2019.parse(instr)

camera_output = ''.join([str(chr(int(i))) for i in output]).split('\n')
camera_output = camera_output[0:len(camera_output)-2]
rows = len(camera_output)
cols = len(camera_output[0])
def find_intersections(x,y):
    dirs = {(1,0),(-1,0),(0,1),(0,-1)}
    if camera_output[y][x] == '#':
        if all([camera_output[y+dir[1]][x+dir[0]] == '#' for dir in dirs]):
            intersections.add((x,y))

[find_intersections(x,y) for x in range(1,cols-1) for y in range(1,rows-1)]
print(sum([i[0]*i[1] for i in intersections]))

# by inspection

A = 'R,6,L,10,R,8\n'
B = 'R,8,R,12,L,8,L,8\n'
C = 'L,10,R,6,R,6,L,8\n'

routines = [str(ord(a)) for a in 'A,B,A,B,C,A,B,C,A,C\n']
A = [str(ord(a)) for a in A]
B = [str(ord(a)) for a in B]
C = [str(ord(a)) for a in C]
videofeed = [str(ord(a)) for a in 'n\n']


instr = intcode2019.convert(puzzle.input_data)
instr[0] = '2'
inputs = routines
inputs.extend(A)
inputs.extend(B)
inputs.extend(C)
inputs.extend(videofeed)
inp = deque(inputs)
print(inp)
instr, output, i, rel = intcode2019.parse(instr,inp)
print(output[-1])
