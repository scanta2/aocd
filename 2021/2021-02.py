from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=2)



def part1(input_data):
    commands = {'forward': 1, 'down': 1j, 'up': -1j}
    depth = 0
    for line in input_data:
        command, position = line.split(' ')
        depth += commands[command]*int(position)
    return int(depth.real*depth.imag)

def part2(input_data):
    commands = {'forward': 1, 'down': 1j, 'up': -1j}
    depth = 0
    aim = 0
    for line in input_data:
        command, position = line.split(' ')
        if command != 'forward':
            aim += commands[command]*int(position)
        else:
            depth += int(position)
            depth += aim*int(position)
    return int(depth.real*depth.imag)    


puzzle.answer_a = part1(puzzle.input_data.split('\n'))
puzzle.answer_b = part2(puzzle.input_data.split('\n'))




