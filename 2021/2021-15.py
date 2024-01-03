from typing import Counter
from aocd.models import Puzzle
from requests.sessions import REDIRECT_STATI
puzzle = Puzzle(year=2021,day=15)
from copy import deepcopy, copy
import re
import time
from itertools import product, chain
from collections import defaultdict, Counter
from operator import itemgetter
import networkx as nx

input = puzzle.input_data.split('\n')
# input = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".split('\n')
risk_data = [[int(i) for i in row] for row in input]


def build_graph(rd):
    graph = nx.DiGraph()
    for x in range(len(rd[0])):
        for y in range(len(rd)):
            graph.add_node((x,y))
            nbx = [-1, 0, 1, 0]
            nby = [0, -1, 0, 1]
            for xx, yy in zip(nbx,nby):
                new_node = (x+xx,y+yy)
                if new_node[0] >= 0 and new_node[0] < len(rd) and new_node[1] >= 0 and new_node[1] < len(rd):
                    graph.add_node(new_node)
                    graph.add_edge((x,y),new_node, length = rd[new_node[1]][new_node[0]])
    return graph

def part1():
    risk_graph = build_graph(risk_data)
    nodes = nx.shortest_path(risk_graph,(0,0),(len(input)-1,len(input)-1), weight = 'length')[1:]
    cost = sum(risk_data[y][x] for x,y in nodes)
    return cost

def new_risk_data():
    ll = len(input)
    new_ll = 5*ll
    rd = [[0 for i in range(new_ll)] for j in range(new_ll)]
    for x,y in product(range(ll), range(ll)):
        rd[y][x] = risk_data[y][x]

    for tx,ty in product(range(5),range(5)):
        if (tx,ty) == (0,0):
            continue
        for x,y in product(range(ll), range(ll)):
            if tx-1 >= 0:
                rd[ty*ll+y][tx*ll+x] = rd[ty*ll+y][(tx-1)*ll+x] + 1
                if rd[ty*ll+y][tx*ll+x] > 9:
                    rd[ty*ll+y][tx*ll+x] = 1
            else:
                rd[ty*ll+y][tx*ll+x] = rd[(ty-1)*ll+y][(tx)*ll+x] + 1
                if rd[ty*ll+y][tx*ll+x] > 9:
                    rd[ty*ll+y][tx*ll+x] = 1
    return rd

def part2():
    rd = new_risk_data()
    risk_graph = build_graph(rd)
    nodes = nx.shortest_path(risk_graph,(0,0),(len(rd)-1,len(rd)-1), weight = 'length')[1:]
    cost = sum(rd[y][x] for x,y in nodes)
    return cost

puzzle.answer_a = part1()
puzzle.answer_b = part2()

