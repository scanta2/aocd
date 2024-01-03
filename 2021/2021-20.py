from copy import deepcopy
import itertools
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=20)
from copy import copy

input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

input = puzzle.input_data

algorithm = input.split('\n')[0]
image = [[h for h in line] for line in input.split('\n')[2:]]

template = [[['.','.','.'],['.','.','.'],['.','.','.']],[['#','#','#'],['#','#','#'],['#','#','#']]]

for application in range(50):
    # finished = False
    # while not finished:
        # for i in image:
        #     i.insert(0,'.')
        #     i.append('.')
        # extraline = ['.' for i in range(len(image[0]))]
        # image.insert(0,copy(extraline))
        # image.append(copy(extraline))
        outimage = []
        rl, cl = len(image), len(image[0])
        for row in range(-1,rl+1):
            out_row = []
            for col in range(-1,cl+1):
                t = deepcopy(template[application%2])
                for ir, r in enumerate(range(row-1,row+2)):
                    for ic, c in enumerate(range(col-1,col+2)):
                        if r>=0 and r < rl and c>=0 and c < cl:
                            t[ir][ic] = image[r][c]
                t = ''.join(['0' if p == '.' else '1' for p in itertools.chain(*t)])
                t = int(t,2)
                out_row.append(algorithm[t])
            outimage.append(out_row)
            # print(''.join(out_row))
        image, outimage = outimage, []
        print(sum(1 for p in itertools.chain(*image) if p == '#'))
        # finished = all(p == '.' for p in image[0]) and \
        #            all(p == '.' for p in image[-1]) and \
        #            all(p == '.' for p in list(zip(*image))[0]) and \
        #            all(p == '.' for p in list(zip(*image))[-1])
        # print('')
print(sum(1 for p in itertools.chain(*image) if p == '#'))


