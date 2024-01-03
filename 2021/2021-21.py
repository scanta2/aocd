from copy import copy, deepcopy
import itertools as it
from aocd.models import Puzzle
puzzle = Puzzle(year=2021,day=21)
from collections import Counter

positions = list(range(1,11))
numbers = list(range(1,101))

counter = Counter((sum(r) for r in it.product(range(1,4),range(1,4), range(1,4))))
print(counter)

def part1():
    pos = [3,1]
    scores = [0,0]
    die = 0
    num_rolls = 0
    final = 0


    while final == 0:
        for player in range(2):
            rolls = list(numbers[r%100] for r in range(die,die+3))
            num_rolls += 3
            pos[player] = (pos[player]+sum(rolls))%10
            scores[player] += positions[pos[player]]
            if scores[player] >= 1000:
                final = scores[(player+1)%2]*num_rolls
                break
            die = (die+3)%100
    puzzle.answer_a = final

wins = [0, 0]
def play(player, pos, scores, num_univ):
    old_pos = pos[player]
    old_score = scores[player]
    for roll in range(3,10):
        pos[player] = (pos[player]+roll)%10
        scores[player] += positions[pos[player]]
        if scores[player] >= 21:
            wins[player] += num_univ*counter[roll]
        else:
            play((player+1)%2,pos,scores, num_univ*counter[roll])
        pos[player] = old_pos
        scores[player] = old_score


def part2():
    pos = [3,1]
    scores = [0,0]
    num_univ = 1
    play(0,pos,scores,num_univ)
    puzzle.answer_b = max(wins)

part2()
print(wins)








