from typing import Counter
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=6)
from copy import deepcopy
import re
import time

def part1(input,days):
    fishes = [int(i) for i in input.split(',')]
    for day in range(1,days+1):
        num7 = sum(f == 7 for f in fishes)
        fishes = [f-1 if f > 0 else 6 for f in fishes]
        num_new_fishes = sum(f == 6 for f in fishes)-num7
        fishes.extend([8]*num_new_fishes)
    return len(fishes)

        
def part2(input,max_day):
    state_day = {}

    def fish_progeny(day,max_day,state):
        if (state,day) in state_day:
            return state_day[(state,day)]
        new_fish = 1
        for i in range(day+state+1,max_day+1,7):
            new_fish += fish_progeny(i,max_day,8)
        state_day[(state,day)] = new_fish
        return new_fish
    
    fish = [int(i) for i in input.split(',')]
    return sum(fish_progeny(0,max_day,f) for f in fish)
        
    

# puzzle.answer_a = part1(puzzle.input_data,80)
# puzzle.answer_b = part2(puzzle.input_data,256)
t = time.time()
part2(puzzle.input_data,2**15)
print((time.time()-t))