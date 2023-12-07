from aocd.models import Puzzle
from aocd.transforms import lines, numbers
from itertools import product
import re
import operator, string
import networkx as nx
import functools

day = 15
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

# data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

sensors = set()
beacons = set()
arrangements = {}

for line in data:
    rs_,is_,rb_,ib_ = [int(i) for i in re.findall(r'(-?[\d]+)', line)]
    sensor = complex(rs_,is_)
    beacon = complex(rb_,ib_)
    distance = int(abs(rs_-rb_) + abs(is_-ib_))
    sensors.add(sensor)
    beacons.add(beacon)
    arrangements[sensor] = distance

row = 15

parta = set()

for s,d in arrangements.items():
    if s.imag - d <= row <= s.imag + d:
        vd = int(abs(row-s.imag))
        hdmax = d-vd
        for hd in range(-hdmax,hdmax+1):
            pos = complex(s.real+hd,row)
            if pos not in sensors and pos not in beacons:
                parta.add(pos)

puzzle.answer_a = len(parta)
def part2_search():
    sensors = arrangements

    MIN_COORD = 0
    MAX_COORD = 4000000

    for y in range(MIN_COORD, MAX_COORD+1):
        ranges = []
        for s,d in sensors.items():
            half_width = int(d - abs(s.imag - y))
            if half_width < 0:
                continue

            ranges.append((s.real - half_width,
                           s.real + half_width))

        ranges.sort()

        compact = []
        low_x, high_x = ranges[0]
        for n_low_x, n_high_x in ranges[1:]:
            if n_low_x-1 <= high_x:
                high_x = max(high_x, n_high_x)
            else:
                compact.append((low_x, high_x))
                low_x, high_x = n_low_x, n_high_x
        compact.append((low_x, high_x))

        if len(compact) != 1:
            assert(len(compact) == 2)
            (a, b), (c, d) = compact
            assert(b+2 == c)
            x = b+1
            return int(x * 4000000 + y)

puzzle.answer_b = part2_search()