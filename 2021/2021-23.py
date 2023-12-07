from copy import copy, deepcopy
import itertools as it
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=23)
from collections import Counter
from math import prod

import networkx as nx

initial_state = nx.Graph()
final_state = nx.Graph()
for i in range(11):
    initial_state.add_node(i,amphipod='')
    final_state.add_node(i,amphipod='')

initial_state.add_node(2+1j,amphipod='C')
initial_state.add_node(2+2j,amphipod='D')
initial_state.add_node(2+3j,amphipod='D')
initial_state.add_node(2+4j,amphipod='B')
initial_state.add_node(4+1j,amphipod='A')
initial_state.add_node(4+2j,amphipod='C')
initial_state.add_node(4+3j,amphipod='B')
initial_state.add_node(4+4j,amphipod='A')
initial_state.add_node(6+1j,amphipod='B')
initial_state.add_node(6+2j,amphipod='B')
initial_state.add_node(6+3j,amphipod='A')
initial_state.add_node(6+4j,amphipod='D')
initial_state.add_node(8+1j,amphipod='D')
initial_state.add_node(8+2j,amphipod='A')
initial_state.add_node(8+3j,amphipod='C')
initial_state.add_node(8+4j,amphipod='C')

# initial_state.add_node(2+1j,amphipod='B')
# initial_state.add_node(2+2j,amphipod='A')
# initial_state.add_node(4+1j,amphipod='C')
# initial_state.add_node(4+2j,amphipod='D')
# initial_state.add_node(6+1j,amphipod='B')
# initial_state.add_node(6+2j,amphipod='C')
# initial_state.add_node(8+1j,amphipod='D')
# initial_state.add_node(8+2j,amphipod='A')


def add_edges(graph):
    for i in range(10):
        graph.add_edge(i,i+1)
    for i in range(2,9,2):
        graph.add_edge(i,i+1j)
        graph.add_edge(i+1j,i+2j)
        graph.add_edge(i+2j,i+3j)
        graph.add_edge(i+3j,i+4j)

add_edges(initial_state)

step_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
real_pos = {'': 10000, 'A': 2, 'B': 4, 'C': 6, 'D': 8}
penalty = 1000000000000000
best_cost = 1000000000000000

room_pos = list(it.product((2,4,6,8),(1j,2j,3j,4j)))

def move(state,cost):
    global best_cost
    populated_nodes = set(inode for inode in state.nodes if state.nodes[inode]['amphipod'] != '')

    if not any(n.imag == 0 for n in populated_nodes):
        if all(real_pos[state.nodes[r+i]['amphipod']] == r for r, i in room_pos):
            if cost < best_cost:
                best_cost = cost
                print(best_cost)
            return

    for inode in populated_nodes:
        node = state.nodes[inode]
        ca = node['amphipod']
        if cost == 0:
            print("starting node {} {}".format(inode, node))

        rpos = real_pos[ca]
        def node_is_ok(inode):
            return inode.real == rpos and (\
            inode.imag == 4 or all(state.nodes[rpos+i*1j]['amphipod'] == ca for i in range(int(inode.imag+1),5)))

        if node_is_ok(inode):
            continue

        dest = None
        idest = -1
        end = 4
        while dest == None and end > 0:
            if all(state.nodes[rpos+i*1j]['amphipod'] == '' for i in range(1,end+1)) and all(state.nodes[rpos+i*1j]['amphipod'] == ca for i in range(end+1,5)):
                idest = rpos+end*1j
                dest = state.nodes[idest]
            end -= 1
        if dest != None:
            path = nx.shortest_path(state,inode,idest)
            if any(i in populated_nodes for i in path[1:]):
                continue
            new_cost = cost + (len(path)-1)*step_costs[ca]
            dest['amphipod'], node['amphipod'] = node['amphipod'], dest['amphipod']
            move(state,new_cost)
            dest['amphipod'], node['amphipod'] = node['amphipod'], dest['amphipod']


        if dest is None and inode.imag != 0:
            # go to hallway
            for idest in (0,1,3,5,7,9,10):
                dest = state.nodes[idest]
                if dest['amphipod'] == '':
                    path = nx.shortest_path(state,inode,idest)
                    if any(i in populated_nodes for i in path[1:]):
                        continue
                    new_cost = cost + (len(path)-1)*step_costs[ca]
                    dest['amphipod'], node['amphipod'] = node['amphipod'], dest['amphipod']
                    move(state,new_cost)
                    dest['amphipod'], node['amphipod'] = node['amphipod'], dest['amphipod']
                

move(initial_state,0)
# puzzle.answer_a = best_cost
