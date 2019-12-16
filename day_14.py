import math
from collections import defaultdict

with open('inputs/input_14.txt', 'r') as f:
    values = [i[:-1].split(' => ') for i in f.readlines()]

tests = [
'''
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
'''
,
'''
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
'''
,
'''
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
''']

solutions = [13312, 180697, 2210736]


def extract_ingredient(ingredient):
    amount, ingredient = ingredient.strip(' ').split(' ')
    return int(amount), ingredient

def recursive(output, amount_req=1, ore=0):
    index = outputs.index(output) # All lists stay in the same order
    amount = output_counts[index] # The amount produced in one reaction
    multiplier = 0
    while (multiplier*amount) + leftovers[output] < amount_req:
        # See if we can use leftovers from another reaction to help this one
        multiplier += 1
    leftovers[output] = (multiplier*amount)+leftovers[output]-amount_req
    
    for ingredient in recipes[index].split(','):
        amount, ingred = extract_ingredient(ingredient)
        if ingred == 'ORE':
            return ore + (multiplier * amount)
        else:
            ore = recursive(ingred, amount*multiplier, ore)
    return ore
        
            
##for answer, test in zip(solutions, tests):
##    data = [i.split(' => ') for i in test.split('\n')[1:-1]]
##
##    recipes, outputs = zip(*data)
##    output_counts, outputs = zip(*[extract_ingredient(output) for output in outputs])
##
##    leftovers = defaultdict(int)
##    ore_amount = recursive('FUEL')
##    assert(ore_amount == answer)
##    print(f'{answer} == {ore_amount}')

# Part 1
recipes, outputs = zip(*values)
output_counts, outputs = zip(*[extract_ingredient(output) for output in outputs])

leftovers = defaultdict(int)
ore_amount = recursive('FUEL', 1000000)
print(1000000000000/ore_amount)
    
