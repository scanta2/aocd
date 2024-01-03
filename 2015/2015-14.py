from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2015,day=14)
input_data = puzzle.input_data


class Reindeer:
    def __init__(self, name, speed, moving_time, resting_time):
        self.name = name
        self.speed = speed
        self.moving_time = moving_time
        self.resting_time = resting_time
        self.total_distance = 0
        self.points = 0
        self.time = 0
    def advance(self, time):
        self.time += time
        cycle_time = self.moving_time + self.resting_time
        num_full_cycles = self.time // cycle_time
        remaining_time = self.time - num_full_cycles*cycle_time
        self.total_distance = num_full_cycles*self.moving_time*self.speed
        self.total_distance += min(remaining_time,self.moving_time)*self.speed
    def addPoints(self, num_points):
        self.points += num_points

reindeers = list()

for line in input_data.split('\n'):
    tokens = line.split(' ')
    reindeers.append(Reindeer(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13])))

for i in range(2503):
    [reindeer.advance(1) for reindeer in reindeers]
    pos = [reindeer.total_distance for reindeer in reindeers]
    winners = [reindeer.total_distance == max(pos) for reindeer in reindeers]
    [reindeers[i].addPoints(1) for i,winner in enumerate(winners) if winner]
for reindeer in reindeers:
    print('{} {}'.format(reindeer.name, reindeer.points))
    
