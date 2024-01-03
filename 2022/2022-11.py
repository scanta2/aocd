from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product
import re
import operator
from numpy import prod



day = 11
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n\n')

# data = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1""".split('\n\n')

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, }

class Monkey():
    def __init__(self,block):
        lines = block.splitlines()
        self.items = [int(i) for i in re.findall(r'\d+', lines[1])]
        _, self.op = lines[2].split('=')
        self.first, self.op, self.second = self.op.split()
        self.op = ops[self.op]
        self.test = int(lines[3].split()[-1])
        self.throwto = {True: int(lines[4].split()[-1]), False: int(lines[5].split()[-1])}
        self.inspected = 0

    def operation(self,worry):
        first = worry if self.first == 'old' else int(self.first)
        second = worry if self.second == 'old' else int(self.second)
        return self.op(first,second)        

    def take_a_turn(self,others,divisor=1,common=0):
        for item in self.items:
            new_worry = self.operation(item)
            if common != 0:
                new_worry %= common
            new_worry //= divisor
            throwto = self.throwto[new_worry%self.test == 0]
            
            others[throwto].items.append(new_worry)
        self.inspected += len(self.items)
        self.items = []

def parta():
    monkeys = [Monkey(block) for block in data]
    for turn in range(20):
        for monkey in monkeys:
            monkey.take_a_turn(monkeys,3)
    worry_levels = sorted([monkey.inspected for monkey in monkeys], reverse=True)[0:2]
    puzzle.answer_a = worry_levels[0]*worry_levels[1]

parta()

def partb():
    inspected = []
    prev_turn = []
    monkeys = [Monkey(block) for block in data]
    common_prod = prod([i.test for i in monkeys])
    for turn in range(10000):
        for monkey in monkeys:
            monkey.take_a_turn(monkeys, common=common_prod)
    worry_levels = sorted([monkey.inspected for monkey in monkeys], reverse=True)[0:2]
    puzzle.answer_b = prod(worry_levels)

partb()





    



            
