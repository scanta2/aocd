from aocd.models import Puzzle
import copy
import re
from collections import deque, defaultdict
puzzle = Puzzle(year=2017,day=13)

range_depth = defaultdict(int)
range_location = defaultdict(int)
range_direction = defaultdict(int)
max_range = 0
damage = 0

print(puzzle.input_data)
for line in puzzle.input_data.split('\n'):
    tokens = [int(x) for x in re.findall('\d+',line)]
    range_depth[tokens[0]] = tokens[1]
    range_location[tokens[0]] = 0
    range_direction[tokens[0]] = 1
    max_range = max(max_range,tokens[0])

# for time in range(max_range+1):
#     # Entering a range, I can get caught
#     if time in range_location and range_location[time] == 0:
#         damage += time*range_depth[time]
#     # Move scanners
#     for scanner in range_location:
#         if range_location[scanner] == 0:
#             range_direction[scanner] = 1
#         elif range_location[scanner] == range_depth[scanner]-1:
#             range_direction[scanner] = -1
#         range_location[scanner] += range_direction[scanner]

# Initial status
# For each range, compute where the scanner is at time == range
# Check if any of them are at location 0. When we find a combination that works
# we are done

for scanner in range_depth:
    for i in range(scanner):
        if range_location[scanner] == 0:
            range_direction[scanner] = 1
        elif range_location[scanner] == range_depth[scanner]-1:
            range_direction[scanner] = -1
        range_location[scanner] += range_direction[scanner]

delay = 0
while any([range_location[x] == 0 for x in range_location]):
    delay += 1
    for scanner in range_depth:
        if range_location[scanner] == 0:
            range_direction[scanner] = 1
        elif range_location[scanner] == range_depth[scanner]-1:
            range_direction[scanner] = -1
        range_location[scanner] += range_direction[scanner]


print(delay)
