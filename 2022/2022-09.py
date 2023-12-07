from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product


day = 9
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

# data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".splitlines()

moves = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

def solve(num):
    rope = [0 for i in range(num)]
    visited = [rope[-1]]
    for line in data:
        move, times = line.split(' ')
        for jj in range(int(times)):
            rope[0] += moves[move]
            for i in range(1,len(rope)):
                if abs(rope[i-1].imag - rope[i].imag) <= 1 and abs(rope[i-1].real-rope[i].real) <= 1:
                    continue
                elif abs(rope[i-1].imag - rope[i].imag) == 0:
                    rope[i] += (rope[i-1].real-rope[i].real)//abs(rope[i-1].real-rope[i].real)
                elif abs(rope[i-1].real-rope[i].real) == 0:
                    rope[i] += 1j*((rope[i-1].imag-rope[i].imag)//abs(rope[i-1].imag-rope[i].imag))
                else:
                    rope[i] += (rope[i-1].real-rope[i].real)//abs(rope[i-1].real-rope[i].real)
                    rope[i] += 1j*((rope[i-1].imag-rope[i].imag)//abs(rope[i-1].imag-rope[i].imag))
            visited.append(rope[-1])
                
            
    return len(set(visited))

puzzle.answer_a = solve(2)
puzzle.answer_b = solve(10)






