from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
import queue
puzzle = Puzzle(year=2019,day=1)
lines = puzzle.input_data.split('\n')

fuel_requirement = sum(int(l)//3-2 for l in lines)
# puzzle.answer_a = fuel_requirement

def compute_fuel_recursive(mass):
    fuel_mass = max(mass//3-2,0)
    if fuel_mass == 0:
        return fuel_mass
    else:
        return fuel_mass + compute_fuel_recursive(fuel_mass)

fuel_requirement = sum(compute_fuel_recursive(int(l)) for l in lines)
puzzle.answer_b = fuel_requirement
