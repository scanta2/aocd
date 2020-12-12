from aocd.models import Puzzle
from collections import Counter
import networkx as nx
import string
import re

def part1(chain):
    diffs = [chain[i+1]-chain[i] for i in range(len(chain)-1)]
    counts = Counter(diffs)
    return counts[1]*counts[3]

def memoize_paths(f):
    memory = {}
    def inner(chain,source):
        if source not in memory:
            memory[source] = f(chain,source)
        return memory[source]
    return inner

@memoize_paths
def part2(chain,source):
    acceptable = [x for x in chain if source+1<=x<=source+3]
    if len(acceptable) == 0:
        return 0
    if acceptable == [chain[-1]]:
        return 1
    return sum(part2(chain,x) for x in acceptable)



PUZZLE = Puzzle(year=2020,day=10)
INPUT = [int(x) for x in PUZZLE.input_data.splitlines()]
chain = sorted(INPUT)
rating = chain[-1]+3
chain = [0] + chain + [rating]
PUZZLE.answer_a = part1(chain)
PUZZLE.answer_b = part2(chain,chain[0])

