from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from collections import deque
from string import ascii_uppercase
import re

day = 7
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

class node:
    def __init__(self,name):
        self.name = name
        self.subnodes = []
        self.localsize = 0
    def __repr__(self):
        return self.name
    def plot(self):
        print(f"{self.name} {self.localsize}")
        for o in self.subnodes:
            o.plot()

def parser():
    parent = []
    current = None
    for line in data:
        if line.startswith(r"$ cd"):
            *others, directory = line.split(' ')
            if directory == "..":
                parent, current = parent[:-1], parent[-1]
            else:
                if current == None:
                    current = node(directory)
                else:
                    parent.append(current)
                    parent[-1].subnodes.append(node(directory))
                    current = parent[-1].subnodes[-1]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            ssize, _ = line.split(' ')
            current.localsize += int(ssize)
    return parent[0]

filesystem = parser()

sizes = []
def addsizes(obj):
    ssize = obj.localsize + sum(addsizes(o) for o in obj.subnodes)
    sizes.append(ssize)
    return ssize

addsizes(filesystem)
puzzle.answer_a = sum(s if s <= 100000 else 0 for s in sizes)

sizes = sorted(sizes)
space = 70000000-sizes[-1]
for s in sizes:
    if space+s>=30000000:
        puzzle.answer_b = s
        break




