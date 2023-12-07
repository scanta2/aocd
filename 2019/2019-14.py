from math import ceil, floor
from aocd.models import Puzzle
import time
puzzle = Puzzle(year=2019,day=14).input_data.split('\n')

# puzzle = '''171 ORE => 8 CNZTR
# 7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
# 114 ORE => 4 BHXH
# 14 VRPVC => 6 BMBT
# 6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
# 6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
# 15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
# 13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
# 5 BMBT => 4 WPTQ
# 189 ORE => 9 KTJDG
# 1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
# 12 VRPVC, 27 CNZTR => 2 XDBXC
# 15 KTJDG, 12 BHXH => 5 XCVML
# 3 BHXH, 2 VRPVC => 7 MZWV
# 121 ORE => 7 VRPVC
# 7 XCVML => 6 RJRHP
# 5 BHXH, 4 VRPVC => 5 LTCX'''.split('\n')
recipe = {}
for line in puzzle:
    new_line = line.replace(',', '').split(' ')
    recipe[new_line[-1]] = (int(new_line[-2]), tuple((new_line[2*i+1], int(new_line[2*i])) for i in range((len(new_line)-3)//2)))
for instr in recipe:
    print(instr, recipe[instr])

# Objective: get 1 fuel
from collections import Counter
def make_material(material, desired_quantity):
    global material_counter
    global needed_ore
    if material == 'ORE':
        needed_ore += desired_quantity
        material_counter[material] += desired_quantity
        return

    instruction = recipe[material]
    recipe_quantity = instruction[0]
    if desired_quantity<=material_counter[material]:
        multiplier = 1
    else:
        multiplier = max(ceil((desired_quantity-material_counter[material])/recipe_quantity),1)
    # multiplier = 1
    # while multiplier*recipe_quantity+material_counter[material] < desired_quantity:
    #     multiplier += 1
    for new_mat in instruction[1]:
        if material_counter[new_mat[0]] < new_mat[1]*multiplier:
            make_material(new_mat[0], new_mat[1]*multiplier)
        material_counter[new_mat[0]] -= new_mat[1]*multiplier

    material_counter[material] += multiplier*recipe_quantity

goal = int(1e12)

needed_ore = 0

fuel = 0.5
while needed_ore <= goal:
    fuel = int(fuel*2)
    needed_ore = 0
    material_counter = Counter()
    make_material('FUEL', fuel)

min_try = fuel//2
max_try = fuel
while max_try - min_try > 1:
    fuel = (max_try+min_try)//2
    needed_ore = 0
    material_counter = Counter()
    make_material('FUEL', fuel)
    if needed_ore > goal:
        max_try = fuel
    else:
        min_try = fuel


print(fuel)
print(needed_ore)
print(min_try)

