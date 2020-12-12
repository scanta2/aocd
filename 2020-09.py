from aocd.models import Puzzle
import string
import re

def part1(INPUT,len_preamble):
    def passing(num,preamble):
        for i in preamble:
            if num-i in preamble:
                return True
        return False
    for i, num in enumerate(INPUT):
        if i >= len_preamble:
            preamble = INPUT[i-len_preamble:i]
            if not passing(num,preamble):
                return i, num

def part2(idx,num,INPUT):
    cumsum_idx = dict()
    cumsum = 0
    for i in range(idx):
        cumsum += INPUT[i]
        cumsum_idx[cumsum] = i
        if cumsum == num:
            return min(INPUT[:i+1]) + max(INPUT[:i+1])

        if cumsum-num in cumsum_idx.keys():
            idx1, idx2 = cumsum_idx[cumsum], cumsum_idx[cumsum-num]
            idx1, idx2 = min(idx1,idx2), max(idx1,idx2)
            array = INPUT[idx1+1:idx2+1]
            return min(array) + max(array)





PUZZLE = Puzzle(year=2020,day=9)
INPUT = [int(x) for x in PUZZLE.input_data.splitlines()]
idx, num = part1(INPUT,25)
PUZZLE.answer_a = num
PUZZLE.answer_b = part2(idx,num,INPUT)


