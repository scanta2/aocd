import numpy as np
import re
import itertools
from aocd.models import Puzzle
from copy import deepcopy
import collections
import operator
puzzle = Puzzle(day=21,year=2022)
data = puzzle.input_data.splitlines()

# data = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32""".splitlines()

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv, '=': operator.eq}
order_of_ops = []

def parta():
    global order_of_ops
    monkeys_solved = dict()
    monkeys_not_solved = dict()

    for line in data:
        monkey, op = line.split(': ')
        try:
            opi = int(op)
            monkeys_solved[monkey] = opi
        except:
            monkeys_not_solved[monkey] = list(op.split(' '))

    print(monkeys_solved)
    print(monkeys_not_solved)

    while monkeys_not_solved:
        for m, op in monkeys_not_solved.items():
            if op[0] in monkeys_solved and op[2] in monkeys_solved:
                order_of_ops.append(m)
                monkeys_solved[m] = operators[op[1]](monkeys_solved[op[0]],monkeys_solved[op[2]])
                monkeys_not_solved.pop(m)
                if m == 'root':
                    print(monkeys_solved[m])
                break

def partb():
    mynum = 0
    monkeys_solved_cache = dict()
    monkeys_not_solved_cache = dict()

    for line in data:
        monkey, op = line.split(': ')
        if monkey == "humn":
            monkeys_solved_cache[monkey] = mynum
        else:
            try:
                opi = int(op)
                monkeys_solved_cache[monkey] = opi
            except:
                monkeys_not_solved_cache[monkey] = list(op.split(' '))
                if monkey == "root":
                    monkeys_not_solved_cache[monkey][1] = "="
    while True:
        # if mynum&1023 == 0:
        #     print(mynum)
        monkeys_solved = monkeys_solved_cache.copy()
        monkeys_not_solved = monkeys_not_solved_cache.copy()
        monkeys_solved["humn"] = mynum
        works = True
        while works:
            for m in order_of_ops:
                op = monkeys_not_solved[m]
                monkeys_solved[m] = operators[op[1]](monkeys_solved[op[0]],monkeys_solved[op[2]])
                if m == 'root':
                    print(f"{mynum}: {monkeys_solved[op[0]]} {monkeys_solved[op[2]]}")
                    if monkeys_solved[m] == False:
                        mynum = mynum + (monkeys_solved[op[0]] - monkeys_solved[op[2]])//10
                        works = False
                        break
                    else:
                        # puzzle.answer_b = mynum
                        return
parta()
partb()


