from aocd.models import Puzzle
from collections import Counter, defaultdict
from itertools import product
import math
import re    

PUZZLE = Puzzle(year=2020,day=25)
card_pk, door_pk = [int(i) for i in PUZZLE.input_data.splitlines()]
p = 20201227
g = 7

a = 1
while pow(7,a,p) != card_pk:
    a+=1

b = 1
while pow(7,b,p) != door_pk:
    b+=1

print(pow(card_pk,b,p))
print(pow(door_pk,a,p))


