from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=4)
from copy import deepcopy

# print(puzzle.input_data)

input = puzzle.input_data.split('\n')

called_numbers = [int(i) for i in input[0].split(',')]
print(called_numbers)

boards = list()
line = 2
while line < len(input):
    board = [[[int(i),False] for i in input[l].split()] for l in range(line,line+5)]
    boards.append(board)
    line += 6

def win(board):
    return any(all(b[1] for b in row) for row in board) or \
           any(all(b[1] for b in row) for row in zip(*board))

def mark(board,num):
    for row in board:
        for b in row:
            if b[0] == num:
                b[1] = True
                return True
    return False

def part1():
    for called in called_numbers:
        for board in boards:
            if (mark(board,called)) and win(board):
                return called*sum(b[0] for row in board for b in row if not b[1])

def part2():
    score = 0
    bb = deepcopy(boards)
    for board in bb:
        for row in board:
            for b in row:
                b[1] = False

    for called in called_numbers:
        mark_to_remove = []
        for board in bb:
            if (mark(board,called)) and win(board):
                score = called*sum(b[0] for row in board for b in row if not b[1])
                mark_to_remove.append(board)
        for b in mark_to_remove:
            bb.remove(b)
    return score

puzzle.answer_a = part1()
puzzle.answer_b = part2()




