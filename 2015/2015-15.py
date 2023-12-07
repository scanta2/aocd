from aocd.models import Puzzle
import re
import itertools

puzzle = Puzzle(year=2015,day=15)
input_data = puzzle.input_data
# input_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

class Cookie:
    def __init__(self,name,capacity,durability,flavor,texture,calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

cookies = []


for line in input_data.splitlines():
    tokens = line.replace(',','').replace(':','').split(' ')
    cookies.append(Cookie(tokens[0],int(tokens[2]),int(tokens[4]),int(tokens[6]),int(tokens[8]),int(tokens[10])))

cc = range(101)

max_score = 0

for i in itertools.product(cc,cc,cc,cc):
    if sum(i) == 100:
        if sum(cookies[j].calories*v for j,v in enumerate(i)) == 500:
            score  = max(0,sum(cookies[j].capacity*v for j,v in enumerate(i)))
            score *= max(0,sum(cookies[j].durability*v for j,v in enumerate(i)))
            score *= max(0,sum(cookies[j].flavor*v for j,v in enumerate(i)))
            score *= max(0,sum(cookies[j].texture*v for j,v in enumerate(i)))
            max_score = max(max_score,score)

print(max_score)
