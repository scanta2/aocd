from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product


day = 10
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

# data = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop""".splitlines()

class CPU:
    def __init__(self):
        self.initX = 1
        self.afterX = 1
        self.X = []
    def execute(self,instructions):
        for instruction in instructions:
            tokens = instruction.split(' ')
            self.afterX, self.initX = self.initX, self.afterX
            if tokens[0] == 'noop':
                self.afterX = self.initX
                self.X.append(self.initX)
            if tokens[0] == 'addx':
                self.afterX = self.initX
                self.X.append(self.initX)
                self.X.append(self.initX)
                self.afterX += int(tokens[1])
    def parta(self):
        return sum((i+1)*val if (i+1)%40==20 else 0 for i, val in enumerate(self.X))
    def partb(self):
        CRT = ["#" if val-1 <= i%40 <= val+1 else '.' for i, val in enumerate(self.X)]
        for r in range(6):
            print(''.join(CRT[r*40:(r+1)*40]))

cpu = CPU()
cpu.execute(data)
puzzle.answer_a = cpu.parta()
cpu.partb()