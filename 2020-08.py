from aocd.models import Puzzle
import string
import re

class Assembler2020():

    def parse(self,instrs):
        self.parsed_instr = []
        for instr in instrs:
            operation, argument = instr.split(' ')
            argument = int(argument)
            self.parsed_instr.append([operation,argument])
        self.eof = len(instrs)

    def interpret(self,line_nr):
        instr, arg = self.parsed_instr[line_nr]
        if instr == 'acc':
            self.accumulator_ += arg
            self.curr_line += 1
        elif instr == 'jmp':
            self.curr_line += arg
        elif instr == 'nop':
            self.curr_line += 1

    def executePart1(self):
        while True:
            if self.curr_line in self.instructions_run:
                self.bootloop = True
                return self.accumulator_
            if self.curr_line == self.eof:
                return self.accumulator_
            self.instructions_run.add(self.curr_line)
            self.interpret(self.curr_line) 

    def executePart2(self):
        changeset = {'jmp': 'nop', 'nop': 'jmp', 'acc': 'acc'}
        def changeline(obj,line_nr):
            obj.parsed_instr[line_nr][0] = changeset[obj.parsed_instr[line_nr][0]]
        for line_nr in range(self.eof):
            changeline(self,line_nr)
            self.executePart1()
            changeline(self,line_nr)
            if self.bootloop:
                self.reset()
            else:
                return self.accumulator_


    def __init__(self,INPUT):
        self.parse(INPUT)
        self.reset()

    def reset(self):
        self.accumulator_ = 0
        self.curr_line = 0
        self.instructions_run = set()
        self.bootloop = False



PUZZLE = Puzzle(year=2020,day=8)
INPUT = PUZZLE.input_data.splitlines()
handheld = Assembler2020(INPUT)
PUZZLE.answer_a = handheld.executePart1()
PUZZLE.answer_b = handheld.executePart2()



