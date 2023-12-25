from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations, permutations
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import functools
import numpy as np
import sympy
import networkx as nx

day = 25
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""".split('\n')

def part1():
    graph = nx.Graph()
    for line in data:
        source, others = line.split(': ')
        for other in others.split(" "):
            graph.add_edge(source, other, capacity=1)

    num_nodes = len(graph.nodes)

    for nodes in combinations(graph.nodes,2):
        cut_value, partition = nx.minimum_cut(graph, *nodes)
        if cut_value == 3:
            return len(partition[0])*len(partition[1])

if debug:
    print(part1())
else:
    puzzle.answer_a = part1()
