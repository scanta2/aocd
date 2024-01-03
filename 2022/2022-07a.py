from aocd.models import Puzzle
from aocd.transforms import lines, numbers


day = 7
year = 2022

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data.splitlines()

import collections


def get_folder_sizes(s):
    folders = collections.defaultdict(int)

    cwd = []

    for line in s.splitlines():
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    cwd.pop()
                elif parts[2] == '/':
                    # Special handling to avoid double slash
                    cwd = ['']
                else:
                    cwd.append(parts[2])
            elif parts[1] == 'ls':
                pass
            else:
                assert(False)
        elif parts[0] == 'dir':
            pass # Handled implicitly when adding up sizes
        else:
            size = int(parts[0])
            name = ''
            for fold in cwd:
                if name != '/':
                    # Special handling to avoid double slash
                    name += '/'
                name += fold
                folders[name] += size

    return folders

def part1(s):
    answer = sum(size
                 for size in get_folder_sizes(s).values()
                 if size <= 100000)

    

def part2(s):
    folders = get_folder_sizes(s)

    TO_FREE = 30000000 - (70000000 - folders['/'])

    answer = min(size
                 for size in folders.values()
                 if size >= TO_FREE)

    

INPUT = puzzle.input_data
part1(INPUT)
part2(INPUT)
