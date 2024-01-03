import numpy as np
import re
import itertools
from aocd.models import Puzzle
from copy import deepcopy
import collections
puzzle = Puzzle(day=20,year=2022)

def solve(s, times=1, num_mult=1):
    class Wrapper:
        def __init__(self, n):
            self.n = n
        def __repr__(self):
            return str(self.n)

    nums = collections.deque(map(Wrapper, map(int, s.split())))
    order = list(nums)

    # Multiplier for part 2
    for n in nums:
        n.n *= num_mult

    for _ in range(times):
        for n in order:
            idx = nums.index(n)
            nums.rotate(-idx)
            nums.popleft()
            nums.rotate(-n.n)
            nums.insert(0, n)

    nums = [n.n for n in nums]

    zero_idx = nums.index(0)

    return sum(nums[(zero_idx + off) % len(nums)]
               for off in (1000, 2000, 3000))

def part1(s):
    answer = solve(s)

    print(answer)

def part2(s):
    answer = solve(s, 10, num_mult=811589153)

    print(answer)

INPUT = Puzzle(day=20,year=2022).input_data
part1(INPUT)
part2(INPUT)