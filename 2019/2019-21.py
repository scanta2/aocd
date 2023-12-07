import networkx as nx
import intcode2019 as intc
from collections import defaultdict, deque
from aocd.models import Puzzle
import string

puzzle = Puzzle(year=2019,day=21)

intcode_str = puzzle.input_data
intcode = intc.convert(intcode_str)
# program = """NOT A T
# AND D T
# NOT B J
# AND D J
# OR J T
# NOT C J
# AND D J
# OR T J
# RUN
# """

program= """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""

program2 = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT I T
NOT T T
OR F T
AND E T
OR H T
AND T J
AND T J
RUN
"""

inp = deque([str(ord(i)) for i in program2])
output = intc.parse(intcode,input=inp)
# print(output)
print(''.join([chr(int(i)) if int(i) < 255 else i for i in output[-3]]))
puzzle.answer_b = output[-3][-1]