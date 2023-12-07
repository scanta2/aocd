import numpy as np
import itertools
from aocd.models import Puzzle
puzzle = Puzzle(day=18,year=2022)
data = puzzle.input_data.splitlines()
# data = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5""".splitlines()

cubes = [np.array(list(int(i) for i in cube.split(','))) for cube in data]

def adjacent(i,j):
    return sum(np.absolute(i-j))==1

surface = 6*len(cubes)

for i,cubei in enumerate(cubes):
    for j, cubej in enumerate(cubes[i+1:]):
        if adjacent(cubei,cubej):
            surface -= 2
print(surface)

def parse_input(s):
    for line in s:
        yield tuple(map(int, line.split(',')))
def neighbors(x, y, z):
    return [(x-1, y, z), (x+1, y, z),
            (x, y-1, z), (x, y+1, z),
            (x, y, z-1), (x, y, z+1)]
def part2(s):
    data = set(parse_input(s))

    min_x = min(x for x,y,z in data)
    max_x = max(x for x,y,z in data)
    min_y = min(y for x,y,z in data)
    max_y = max(y for x,y,z in data)
    min_z = min(z for x,y,z in data)
    max_z = max(z for x,y,z in data)

    x_range = range(min_x, max_x+1)
    y_range = range(min_y, max_y+1)
    z_range = range(min_z, max_z+1)

    known_exterior = set()

    def is_exterior(x, y, z):
        if (x, y, z) in data:
            return False

        checked = set()
        todo = [(x, y, z)]

        while todo:
            x, y, z = todo.pop()
            if (x, y, z) in checked:
                continue
            checked.add((x, y, z))
            if (x, y, z) in known_exterior:
                known_exterior.update(checked - data)
                return True
            if x not in x_range or y not in y_range or z not in z_range:
                # We breached the range, it's exterior!
                known_exterior.update(checked - data)
                return True
            if (x, y, z) not in data:
                todo += neighbors(x, y, z)

        # We couldn't reach the outside!
        return False

    answer = 0

    for x, y, z in data:
        for n in neighbors(x, y, z):
            if is_exterior(*n):
                answer += 1

    puzzle.answer_b = answer

puzzle.answer_b = part2(data)







# puzzle.answer_a = surface