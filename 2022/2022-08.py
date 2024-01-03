from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product


day = 8
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

# data = """30373
# 25512
# 65332
# 33549
# 35390""".splitlines()

trees = [[int(i) for i in line] for line in data]
R,C = len(trees), len(trees[0])

def parta():
    numvisibible = 0
    for r,c in product(range(R), range(C)):
        if all(trees[r-i][c] < trees[r][c] for i in range(1,r+1)) or \
               all(trees[r+i][c] < trees[r][c] for i in range(1,R-r)) or \
               all(trees[r][c-i] < trees[r][c] for i in range(1,c+1)) or \
               all(trees[r][c+i] < trees[r][c] for i in range(1,C-c)):
               numvisibible += 1
    return numvisibible
 
puzzle.answer_a = parta()

def partb():
    score = 0
    for r,c in product(range(R), range(C)):
        up = 0
        curr = trees[r][c]
        while r-up-1 >= 0:
            up += 1
            if trees[r-up][c] < curr:
                continue #curr = max(curr,trees[r-up-1][c])
            else:
                break
        down = 0
        curr = trees[r][c]
        while r+down+1 < R:
            down += 1
            # if trees[r+down+1][c] <= trees[r][c]:
            if trees[r+down][c] < curr:
                continue #curr = max(curr,trees[r+down+1][c])
            else:
                break
        
        left = 0
        curr = trees[r][c]
        while c-left-1 >= 0:
            left += 1
            # if trees[r][c-left-1] <= trees[r][c]:
            if trees[r][c-left] < curr:
                continue #curr = max(curr,trees[r][c-left-1])
            else:
                break
        
        right = 0
        curr = trees[r][c]
        while c+right+1 < C:
            right += 1
            # if trees[r][c+right+1] <= trees[r][c]:
            if trees[r][c+right] < curr:
                continue
            else:
                break
        score = max(score, up*down*right*left)
    return score

print(partb())
puzzle.answer_b = partb()