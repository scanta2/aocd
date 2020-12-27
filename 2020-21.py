from aocd.models import Puzzle
from collections import Counter, defaultdict
from itertools import product
import math
import re

def part1(INPUT):
    allergens_dict = defaultdict(list)
    ingredients_counter = Counter()
    for line in INPUT.splitlines():
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        ingredients_counter += Counter(ingredients)
        allergens = allergens.replace(')','')
        allergens = allergens.split(', ')
        for a in allergens:
            allergens_dict[a].append(ingredients)
    allergens = set(a for a in allergens_dict)

    allergen_ingredient = {}
    for a in allergens:
        allergen_ingredient[a] = set.intersection(*[set(i) for i in allergens_dict[a]])

    while any(len(allergen_ingredient[a]) != 1 for a in allergen_ingredient):
        for a, v in allergen_ingredient.items():
            if len(v) == 1:
                for b, w in allergen_ingredient.items():
                    if b != a:
                        w -= v

    for i in allergen_ingredient.values():
        for j in i:
            ingredients_counter[j] = 0
    return sum(ingredients_counter.values()), allergen_ingredient
    

PUZZLE = Puzzle(year=2020,day=21)
INPUT = PUZZLE.input_data
# INPUT = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)"""
PUZZLE.answer_a, ai = part1(INPUT)

ins = []
for a in sorted(ai):
    ins.append(ai[a])

PUZZLE.answer_b = ','.join(list(i)[0] for i in ins)


