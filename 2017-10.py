from aocd.models import Puzzle

from functools import reduce
from operator import xor
puzzle = Puzzle(year=2017,day=10)

max_length = 256
sequence = [i for i in range(0,max_length)]

lengths = [ord(x) for x in puzzle.input_data]
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
# print(sequence)

dense_hash = list()

for i in range(16):
    element = sequence[i*16:i*16+16]
    dense_hash += [reduce(xor,map(int,element))]
    
representation = ''.join(['{:02x}'.format(x) for x in dense_hash])
print(representation)
puzzle.answer_b = representation
