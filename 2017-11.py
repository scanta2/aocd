from aocd.models import Puzzle
puzzle = Puzzle(year=2017,day=11)

position = (0,0,0)

max_distance = 0

n, ne, se, s, sw, nw = (0,1,-1), (1,0,-1), (1,-1,0), (0,-1,1),(-1,0,1),(-1,1,0)
moves = {'n': n, 'ne': ne, 'se': se, 's': s, 'sw': sw, 'nw': nw}

for step in puzzle.input_data.split(','):
    move = moves[step]
    position = (position[0]+move[0], position[1]+move[1], position[2]+move[2])
    max_distance = max(max_distance,max((abs(x) for x in position)))

print(max_distance)








