from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=3)
from copy import copy



def part1(input):
    num_rows = len(input)
    gamma = ''.join('1' if sum(int(i) for i in row) >= num_rows/2 else '0' for row in zip(*input))
    swap = {'0': '1', '1': '0'}
    epsilon = ''.join(swap[i] for i in gamma)
    return int(gamma,2)*int(epsilon,2)

def part2(data):
    def filter_bit(data, bit_num, mostcommon):
        num_rows = len(data)
        col = list(zip(*data))[bit_num]
        bit = '1' if sum(int(i) for i in col) >= num_rows/2 else '0'
        if not mostcommon:
            swap = {'0': '1', '1': '0'}
            bit = swap[bit]
        return [row for row in data if row[bit_num] == bit]
    
    def filter(data,mostcommon):
        res = copy(data)
        for i in range(len(data[0])):
            res = filter_bit(res,i,mostcommon)
            if (len(res) == 1):
                break
        return int(res[0],2)

    return filter(data,True)*filter(data,False)

puzzle.answer_a = part1(puzzle.input_data.split('\n'))
puzzle.answer_b = part2(puzzle.input_data.split('\n'))




