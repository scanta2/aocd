from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product
import re
import operator, string
import networkx as nx
import functools

day = 13
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.split('\n\n')

# data = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]""".split('\n\n')

def compare(left, right):
    for i,(l,r) in enumerate(zip(left,right)):
        if isinstance(l,int) and not isinstance(r,int):
            l = [l]
        if isinstance(r,int) and not isinstance(l,int):
            r = [r]
        if isinstance(l,int) and isinstance(r,int):
            if l < r:
                return True
            if r < l:
                return False
        elif isinstance(l,list) and isinstance(r,list):
            res = compare(l,r)
            if res is False or res is True:
                return res
    if len(right) > len(left):
        return True
    if len(left) > len(right):
        return False
    return None

        
# inorder = 0
# for idx, pair in enumerate(data):
#     left, right = [eval(i) for i in pair.splitlines()]
#     if compare(left,right):
#         inorder += idx+1
# print(inorder)

packets = []
for pair in data:
    left, right = [eval(i) for i in pair.splitlines()]
    packets.append(left)
    packets.append(right)
packets.append([[2]])
packets.append([[6]])


for i in range(len(packets)):
    for j in range(i+1,len(packets)):
        if not compare(packets[i], packets[j]):
            packets[i], packets[j] = packets[j], packets[i]

decoder_key = (packets.index([[2]])+1)*(packets.index([[6]])+1)
print(decoder_key)



    
