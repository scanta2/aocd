import networkx as nx
import intcode2019 as intc
from collections import deque
from aocd.models import Puzzle

instr = Puzzle(year=2019,day=15).input_data
instr = intc.convert(instr)
resume = 0
rel_base = 0
maze = nx.Graph()
ox_sys_pos = 0
visited = set()
dirs = {'1': 1j, '2': -1j, '3': -1, '4': 1}
backtrack = {'1': '2', '2': '1', '3': '4', '4': '3'}

def build_recur(pos):
    global visited
    global instr
    global resume
    global rel_base
    global maze
    global ox_sys_pos

    visited.add(pos) 
    for move in ['1','2','3','4']:
        inp = deque([move]) # north
        instr, output, resume, rel_base = intc.parse(instr,inp,resume,rel_base)
        if output[0] != '0':
            new_pos = pos + dirs[move]
            if output[0] == '2':
                ox_sys_pos = new_pos
            if new_pos not in visited:
                maze.add_edge(pos,new_pos,weight=1)
                build_recur(new_pos)
            inp = deque([backtrack[move]])
            instr, output, resume, rel_base = intc.parse(instr,inp,resume,rel_base)
build_recur(0j)
print(ox_sys_pos)
print(nx.dijkstra_path_length(maze,0j,ox_sys_pos))

all_path = nx.single_source_dijkstra_path_length(maze,ox_sys_pos)
print(all_path)   

