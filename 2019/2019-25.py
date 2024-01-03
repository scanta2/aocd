import networkx as nx
import intcode2019 as intc
from collections import defaultdict, deque, Counter
from aocd.models import Puzzle
from itertools import product, combinations
import string

puzzle = Puzzle(year=2019,day=25)
input_data = puzzle.input_data
computer = intc.convert(input_data)
computer, output, pointer, relative_base = intc.parse(computer,input=deque([]))

commands = """north
take easter egg
east
take astrolabe
south
take space law space brochure
north
west
north
take manifold
north
north
take hologram
north
take weather machine
north
take antenna
south
south
south
south
south
east
north
north
take fuel cell
south
south
west
north
north
north
north
north
west
"""

for command in commands.split('\n'):
    output_ = ''.join([chr(int(o)) for o in output])
    print(output_)
    if 'Security Checkpoint' in output_:
        break
    string_ = command + '\n'
    string_ = deque([ord(o) for o in string_])
    computer, output, pointer, relative_base = intc.parse(computer,input=string_,resume=pointer,relative_base=relative_base)


items = ['hologram', 'weather machine', 'manifold', 'fuel cell', 'astrolabe', 'antenna', 'easter egg', 'space law space brochure' ]
drop = items.copy()

for r in range(len(items)):
    for keep in combinations(items,r):
        commands = []
        for item in items:
            commands += ['drop ' + item]
        for item in keep:
            commands += ['take ' + item]
        commands += ['south']
        for command in commands:
            output_ = ''.join([chr(int(o)) for o in output])
            print(output_)
            string_ = command + '\n'
            string_ = deque([ord(o) for o in string_])
            computer, output, pointer, relative_base = intc.parse(computer,input=string_,resume=pointer,relative_base=relative_base)
        output_ = ''.join([chr(int(o)) for o in output])
        print(output_)
        if 'A loud,' in output_:
            pass
        else:
            break