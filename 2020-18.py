from aocd.models import Puzzle
import re
from itertools import product
from math import prod

def evaluate(line,precedence):
    tokens = re.findall(r"[\d\(\)\+\*\-\/]",line)
    output = []
    operators = []
    for t in tokens:
        if t.isdigit():
            output.append(int(t))
        elif t in "+-*\/":
            while len(operators) > 0 and operators[-1] != "(" and \
                  (precedence[operators[-1]] >= precedence[t]):
                output.append(operators.pop())
            operators.append(t)
        elif t == "(":
            operators.append(t)
        else:
            while operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
    output.extend(reversed(operators))
    
    st = []
    for t in output:
        if not isinstance(t,int): 
            if t == "+":
                st.append(st.pop()+st.pop())
            if t == "-":
                st.append(st.pop()-st.pop())
            if t == "*":
                st.append(st.pop()*st.pop())
            if t == "\/":
                st.append(st.pop()//st.pop())
        else:
            st.append(t)
    return st.pop()
    

def solve(INPUT,token_precedence):
    return sum(evaluate(line,token_precedence) for line in INPUT)

PUZZLE = Puzzle(year=2020,day=18)
INPUT = PUZZLE.input_data.splitlines()
token_precedence = {'+': 1, '-': 1, '*': 1, "\/": 1}
PUZZLE.answer_a = solve(INPUT,token_precedence)
token_precedence = {'+': 2, '-': 2, '*': 1, "\/": 1}
PUZZLE.answer_b = solve(INPUT,token_precedence)
