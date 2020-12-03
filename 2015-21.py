from aocd.models import Puzzle

from functools import reduce
from operator import xor
import string
import re
from copy import deepcopy
from collections import defaultdict, deque, Counter, OrderedDict
import queue
from itertools import combinations
from math import sqrt, floor, ceil

weapons = {'Dagger': {'Cost': 8, 'Damage': 4, 'Armor': 0}, \
           'Shortsword': {'Cost': 10, 'Damage': 5, 'Armor': 0}, \
           'Warhammer': {'Cost': 25, 'Damage': 6, 'Armor': 0}, \
           'Longsword': {'Cost': 40, 'Damage': 7, 'Armor': 0}, \
           'Greataxe': {'Cost': 74, 'Damage': 8, 'Armor': 0}}


armors = {'Leather': {'Cost': 13, 'Armor': 1, 'Damage': 0}, \
          'Chainmail': {'Cost': 31, 'Armor': 2, 'Damage': 0}, \
          'Splintmail': {'Cost': 53, 'Armor': 3, 'Damage': 0}, \
          'Bandedmail': {'Cost': 75, 'Armor': 4, 'Damage': 0}, \
          'Platemail': {'Cost': 102, 'Armor': 5, 'Damage': 0}}

rings = {'Da+1': {'Cost': 25, 'Damage': 1, 'Armor': 0}, \
         'Da+2': {'Cost': 50, 'Damage': 2, 'Armor': 0}, \
         'Da+3': {'Cost': 100, 'Damage': 3, 'Armor': 0}, \
         'De+1': {'Cost': 20, 'Damage': 0, 'Armor': 1}, \
         'De+2': {'Cost': 40, 'Damage': 0, 'Armor': 2}, \
         'De+3': {'Cost': 80, 'Damage': 0, 'Armor': 3}, \
    }

cost = 0

for chosen_weapon in combinations(weapons,1):
    for num_armor in range(2):
        for chosen_armor in combinations(armors,num_armor):
            for num_rings in range(3):
                for chosen_ring in combinations(rings,num_rings):
                    chosen_cost = weapons[chosen_weapon[0]]['Cost'] + sum(armors[i]['Cost'] for i in chosen_armor) + sum(rings[i]['Cost'] for i in chosen_ring)
                    player = {'hit_points': 100, 'damage': 0, 'armor': 0}
                    player['damage'] = weapons[chosen_weapon[0]]['Damage'] + sum(armors[i]['Damage'] for i in chosen_armor) + sum(rings[i]['Damage'] for i in chosen_ring)
                    player['armor'] = weapons[chosen_weapon[0]]['Armor'] + sum(armors[i]['Armor'] for i in chosen_armor) + sum(rings[i]['Armor'] for i in chosen_ring)
                    boss = {'hit_points': 103, 'damage': 9, 'armor': 2}
                    attacker, defendant = player, boss
                    while True:
                        hit_points = max(1, attacker['damage'] - defendant['armor'])
                        defendant['hit_points'] -= hit_points
                        if defendant['hit_points'] < 1:
                            break
                        attacker, defendant = defendant, attacker
                    if defendant is player:
                        cost = max(chosen_cost, cost)

print(cost)
                    
