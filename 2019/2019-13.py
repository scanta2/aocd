from aocd.models import Puzzle
import intcode2019
import re
from collections import deque
import time

score = 0
step = 0
grid = []
ball_coord_y = 0 
paddle_coord_y = 0
num_blocks = 1

def draw(output):
    global num_blocks
    global grid
    global score
    global step
    global ball_coord_y
    global paddle_coord_y
    tile_dict = {'0' : ' ', '1': 'X', '2': '#', '3': '-', '4': 'O'}
    if step == 0:
        minx = max(0,min([int(output[i]) for i in range(0,len(output),3)]))
        maxx = max([int(output[i]) for i in range(0,len(output),3)])
        miny = max(0,min([int(output[i]) for i in range(1,len(output),3)]))
        maxy = max([int(output[i]) for i in range(1,len(output),3)])
        grid = [['*' for j in range(maxx-minx+1)] for i in range(maxy-miny+1)]
    for i in range(0,len(output),3):
        if output[i] == '-1'and output[i+1] == '0':
            score = max(score,int(output[i+2]))
        else:
            grid[int(output[i+1])][int(output[i])] = tile_dict[output[i+2]]
            if tile_dict[output[i+2]] == 'O':
                ball_coord_y = int(output[i])
            if tile_dict[output[i+2]] == '-':
                paddle_coord_y = int(output[i])
    num_blocks = 0
    for line in grid:
        num_blocks += line.count('#')
    # print('')
    # print(score)
    # for line in grid:
    #     print(''.join(line))

    if ball_coord_y == paddle_coord_y:
        return '0'
    elif ball_coord_y > paddle_coord_y:
        return '1'
    else:
        return '-1'

    

    


puzzle = Puzzle(year=2019,day=13)
memory = puzzle.input_data.split('\n')
memory = intcode2019.convert(memory[0])
memory[0] = '2'
resume = 0
relative_base = 0
inp = deque([])
while num_blocks > 0:
    memory, output, resume, relative_base = intcode2019.parse(memory,inp,resume, relative_base)
    inp = deque([draw(output)])
    if len(inp) == 0:
        break
    step += 1
puzzle.answer_b = score


