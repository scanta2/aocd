from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, Counter
import queue
puzzle = Puzzle(year=2017,day=20)
lines = puzzle.input_data.split('\n')

positions = []
velocities = []
accelerations = []
distances = []
same_quadrant = []
valid = []

def is_same_quadrant(p,a):
    products = (p[i]*a[i] for i in range(3))
    return all(i >= 0 for i in products)

def update(i):
    velocities[i] = [velocities[i][n]+accelerations[i][n] for n in range(3)]
    positions[i] = [velocities[i][n]+positions[i][n] for n in range(3)]
    distances[i] = sum(abs(p) for p in positions[i])
    same_quadrant[i] = is_same_quadrant(positions[i], accelerations[i])

def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
 
    return indexPosList

def destroy_same_position():
    totuple = [tuple(i) for i in positions]
    counts = Counter(totuple)
    for key in counts:
        if counts[key] > 1:
            indexes = getIndexPositions(totuple, key)
            for index in indexes:
                valid[index] = False
                same_quadrant[index] = True
    

for line in lines:
    tokens = list(int(i) for i in re.findall('[+-]?\d+',line))
    positions.append(tokens[0:3])
    velocities.append(tokens[3:6])
    accelerations.append(tokens[6:])
    distance = sum([abs(i) for i in tokens[0:3]])
    distances.append(distance)
    same_quadrant.append(is_same_quadrant(tokens[0:3],tokens[6:]))
    valid.append(True)

while not all(same_quadrant):
    for i in range(len(lines)):
        if valid[i]:
            update(i)
    destroy_same_position()

puzzle.answer_a = distances.index(min(distances))
puzzle.answer_b = sum(1 if i == True else 0 for i in valid)