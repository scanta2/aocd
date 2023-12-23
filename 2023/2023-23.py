from aocd.models import Puzzle
import re
import string
from math import prod, lcm
from itertools import chain, product, combinations
import operator
from collections import defaultdict, OrderedDict, Counter
from copy import copy, deepcopy
from sympy.ntheory.modular import crt
import functools
import numpy as np
import networkx as nx

day = 23
year = 2023
puzzle = Puzzle(day=day, year=year)

debug = False
if debug == False:
    data = puzzle.input_data.split('\n')
else:
    data = puzzle.examples[0].input_data.split('\n')
grid = [[c for c in line] for line in data]
height = len(data)
width = len(data[0])

def isvalid(x,y):
    return x >= 0 and x < width and y >= 0 and y < height and grid[y][x] != '#'

def solve(part2=False):
    if part2 is False:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '.' or part2 and grid[y][x] != '#':
                for dirx, diry in zip([0,0,1,-1],[1,-1,0,0]):
                    if isvalid(x+dirx,y+diry):
                        graph.add_edge((x,y),(x+dirx, y+diry))
            elif grid[y][x] == '>' and isvalid(x+1,y):
                graph.add_edge((x,y),(x+1,y))
            elif grid[y][x] == '<' and isvalid(x-1,y):
                graph.add_edge((x,y),(x-1,y))
            elif grid[y][x] == '^' and isvalid(x,y-1):
                graph.add_edge((x,y),(x,y-1))
            elif grid[y][x] == 'v' and isvalid(x,y+1):
                graph.add_edge((x,y),(x,y+1))
    start = (grid[0].index('.'), 0)
    stop = (grid[-1].index('.'), height-1)

    max_length = 0

    lp = nx.all_simple_paths(graph,start,stop)
    for p in lp:
        lenp = len(p)-1
        if lenp > max_length:
            max_length = lenp
            print(max_length)
    return max_length

def part2fast():
    start = (grid[0].index('.'), 0)
    stop = (grid[-1].index('.'), height-1)
    graph = nx.Graph()
    for y in range(height):
        for x in range(width):
            if grid[y][x] != '#':
                for dirx, diry in zip([0,0,1,-1],[1,-1,0,0]):
                    if isvalid(x+dirx,y+diry):
                        graph.add_edge((x,y),(x+dirx, y+diry))

    # find super nodes
    sn = set([n for n in graph.nodes if graph.degree[n] > 2])
    sn.add(start)
    sn.add(stop)

    # find the longest distances between pairs of supernodes only if the
    # path does not cross any other supernode, add add to supergraph 
    edges_dict = defaultdict(lambda: 1)
    for a,b in combinations(sn,2):
        print((a,b))
        new_graph = deepcopy(graph)
        set_to_remove = set.difference(sn, set([a,b]))
        for n in set_to_remove:
            new_graph.remove_node(n)

        for path in nx.all_simple_paths(new_graph,a,b):
            if sum(n in path[1:-1] for n in sn) == 0:
                edges_dict[(a,b)] = max(edges_dict[(a,b)], len(path)-1)
    
    sgraph = nx.Graph()
    for (a,b), d in edges_dict.items():
        sgraph.add_edge(a,b,cost=d)
    
    max_length = 0
    lp = nx.all_simple_paths(sgraph,start,stop)
    for p in lp:
        lpl = nx.path_weight(sgraph,p,'cost')
        if lpl > max_length:
            max_length = lpl
    return max_length
    

puzzle.answer_a = solve()
puzzle.answer_b = part2fast()
