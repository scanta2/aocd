from aocd.models import Puzzle

from functools import reduce
from operator import xor
puzzle = Puzzle(year=2017,day=15)

genA = 289
genB = 629

genAfact = 16807
genBfact = 48271
modulo = 2147483647

comp = 65535

num_matches = 0
for i in range(5000000):
    while genA & 3:
        genA = ((genA%modulo)*(genAfact))%modulo
    while genB & 7:
        genB = ((genB%modulo)*(genBfact))%modulo
    if (genA & comp) == (genB & comp):
        num_matches += 1
    genA = ((genA%modulo)*(genAfact))%modulo
    genB = ((genB%modulo)*(genBfact))%modulo
puzzle.answer_b = num_matches





