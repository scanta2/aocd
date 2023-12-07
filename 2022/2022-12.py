from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product
import re
import operator, string
import networkx as nx

day = 12
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()
elevations = string.ascii_lowercase

# data = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".splitlines()

map = nx.DiGraph()

for row, line in enumerate(data):
    if 'S' in line:
        col = line.find('S')
        origin = (row, col)
        line = line[:col] + 'a' + line[col+1:]
    if 'E' in line:
        col = line.find('E')
        destination = (row, col)
        line = line[:col] + 'z' + line[col+1:]
    for col, h in enumerate(line):
        map.add_node((row,col), height=elevations.find(h))

for row,col in product(range(len(data)),range(len(data[0]))):
    h = map.nodes[(row,col)]['height']
    if row-1 >= 0 and map.nodes[(row-1,col)]["height"]-h <= 1:
        map.add_edge((row,col),(row-1,col))
    if row+1 < len(data) and map.nodes[(row+1,col)]["height"]-h <= 1:
        map.add_edge((row,col),(row+1,col))
    if col-1 >= 0 and map.nodes[(row,col-1)]["height"]-h <= 1:
        map.add_edge((row,col),(row,col-1))
    if col+1 < len(data[0]) and map.nodes[(row,col+1)]["height"]-h <= 1:
        map.add_edge((row,col),(row,col+1))

print(map)
# puzzle.answer_a = nx.shortest_path_length(map,source=origin,target=destination)

min_len = 1000000000000
for i in map.nodes:
    if map.nodes[i]['height'] == 0:
        try:
            path = nx.shortest_path(map,source=i,target=destination)
            if len(path) > 0 and len(path)-1 < min_len:
                min_len = len(path)-1
        finally:
            continue
puzzle.answer_b = min_len







    


