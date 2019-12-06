with open('inputs/input_1.txt', 'r') as f:
    data = [int(line[:-1])  for line in f.readlines()] #  strip \n

def fuel_required(mass):
    fuel = int(mass/3) - 2
    if fuel > 0:
        return fuel
    return 0

#Part 1
result = sum([fuel_required(m) for m in data])
print(f'Part 1 total fuel {result}')

# Part 2

def all_fuel(mass):
    fuel = 0
    while mass > 8:
        mass = fuel_required(mass)
        fuel += mass
    return fuel

result = sum([all_fuel(m) for m in data])
print(f'Part 2 total fuel {result}')
