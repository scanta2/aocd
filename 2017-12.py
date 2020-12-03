from aocd.models import Puzzle
import copy
import re
from collections import deque, defaultdict
puzzle = Puzzle(year=2017,day=13)

range_depth = defaultdict(int)
range_location = defaultdict(int)
range_direction = defaultdict(int)

print(puzzle.input_data)
