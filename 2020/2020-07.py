from aocd.models import Puzzle
import networkx as nx
import string
import re

from networkx.algorithms.components.connected import connected_components

def parse_rules(INPUT):
    rules = dict()
    for rule in INPUT:
        color, rest = rule.split(' bags contain ')
        rules[color] = dict()
        if 'no other bags' in rest:
            continue
        else:
            contents = rest.split(', ')
            for content in contents:
                n, c1, c2, bla = content.split(' ')
                rules[color][c1 + ' ' + c2] = int(n)
    return rules

def part1(RULES):
    graph = nx.DiGraph()
    for key in RULES:
        for content in RULES[key]:
            graph.add_edge(key, content)
    
    count = sum([nx.has_path(graph,key,'shiny gold') for key in RULES])
    return count-1

def count_bags(RULES,color):
    count = 1
    for bag in RULES[color]:
        count += RULES[color][bag]*count_bags(RULES,bag)
    return count

def part2(RULES,color):
    return count_bags(RULES,color)-1


PUZZLE = Puzzle(year=2020,day=7)
INPUT = PUZZLE.input_data.splitlines()
RULES = parse_rules(INPUT)
PUZZLE.answer_a = part1(RULES)
PUZZLE.answer_b = part2(RULES,'shiny gold')



