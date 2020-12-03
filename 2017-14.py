from aocd.models import Puzzle

from functools import reduce
from operator import xor
puzzle = Puzzle(year=2017,day=14)

used = 0

max_length = 256

matrix = []

for row in range(128):
    sequence = [i for i in range(max_length)]
    #lengths = [ord(x) for x in ''.join(['flqrgnkx','-',str(row)])]
    lengths = [ord(x) for x in ''.join([puzzle.input_data,'-',str(row)])]
    lengths += [17, 31, 73, 47, 23]

    current_position = 0
    skip_size = 0
    for i in range(64):
        for length in lengths:
            final_position = (current_position + length)%max_length
            if final_position > current_position or final_position == current_position and length == 0:
                sequence[current_position:final_position] = sequence[current_position:final_position][::-1]
            else:
                first = sequence[current_position:]
                to_be_reversed = first + sequence[:length-len(first)]
                to_be_reversed.reverse()
                sequence[current_position:] = to_be_reversed[:max_length-current_position]
                sequence[:length-len(sequence[current_position:])] = to_be_reversed[max_length-current_position:]
            current_position+=length+skip_size
            current_position%=max_length
            skip_size+=1

    dense_hash = list()

    for i in range(16):
        element = sequence[i*16:i*16+16]
        dense_hash += [reduce(xor,map(int,element))]
        
    representation = ''.join(['{0:02x}'.format(x) for x in dense_hash])
    representation = representation.replace(' ', '0')
    scale = 16
    numberofbits = 4
    representation = ''.join(['{0:04b}'.format(int(x,scale)) for x in representation ])
    matrix += [representation]
    used += sum([1 for x in representation if x == '1'])

def valid(num):
    return num >= 0 and num < 128

number_of_regions = 0
nodes_to_visit = set((row, col) for row in range(128) for col in range(128) if matrix[row][col] == '1')
positions = ((0, -1), (-1, 0), (1, 0), (0, 1))
while nodes_to_visit:
    # Pop first available node
    neighbors_to_visit = {nodes_to_visit.pop()}
    while neighbors_to_visit:
        current = neighbors_to_visit.pop()
        for row, col in positions:
            rowN, colN = current[0]+row, current[1]+col
            if valid(rowN) and valid(colN) and matrix[rowN][colN] == '1' and (rowN, colN) in nodes_to_visit:
                 neighbors_to_visit.add((rowN,colN))
                 nodes_to_visit.remove((rowN,colN))
    number_of_regions += 1

print(number_of_regions)
puzzle.answer_b = number_of_regions