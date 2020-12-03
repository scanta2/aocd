from aocd.models import Puzzle
puzzle = Puzzle(year=2020,day=1)
input_data = puzzle.input_data
expenses = sorted([int(x) for x in input_data.split('\n')])
TARGET = 2020

# for expense in expenses:
#     if (TARGET-expense) in expenses:
#         puzzle.answer_a = expense*(TARGET-expense) 

for i in range(len(expenses)):
    for j in range(i+1,len(expenses)):
        i_plus_j = expenses[i] + expenses[j]
        product = expenses[i] * expenses[j]
        missing = TARGET - i_plus_j
        if missing >= expenses[j] and missing in expenses:
            puzzle.answer_b = product*missing
