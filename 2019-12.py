from aocd.models import Puzzle
import re
from itertools import product
from math import gcd

puzzle = Puzzle(year=2019,day=12)
data = puzzle.input_data.split('\n')

moons = []
for line in data:
    pos = [int(i) for i in re.findall('-?\d+', line)]
    vel = [0,0,0]
    moons.append([pos,vel])

periods = [0,0,0]

for axis in range(3):
    states = dict()
    step = 0
    while True:
        state = (moons[0][0][axis], moons[0][1][axis],
                moons[1][0][axis], moons[1][1][axis], 
                moons[2][0][axis], moons[2][1][axis], 
                moons[3][0][axis], moons[3][1][axis])

        if state not in states:
            states[state] = step
        else:
            periods[axis] = step


        # apply gravity
        for i,j in product(range(4),range(4)):
            # update moon i given the influence of moon j
            if i != j:
                incr = 1 if moons[i][0][axis] < moons[j][0][axis] else -1
                if moons[i][0][axis] == moons[j][0][axis]:
                    incr = 0
                moons[i][1][axis] += incr
        
        # update positions
        for i in range(len(data)):
            moons[i][0][axis] += moons[i][1][axis]
        
        # update step counter
        step += 1
            
        if periods[axis] != 0:
            break

lcm = 1
for i in range(3):
    lcm = lcm*periods[i]//gcd(lcm,periods[i])
print(lcm)


