with open('inputs/input_6.txt', 'r') as f:
    data = [orbit[:-1].split(')') for orbit in f.readlines()] # strip \n

class Orbiting_thing():
    def __init__(self, name):
        self.name = name
        self.children = []

    def __repr__(self):
        return self.name

all_names = set([i[0] for i in data] + [i[1] for i in data])
orbit_dic = {name: Orbiting_thing(name) for name in all_names}

for parent, child in data:
    #  Sorting the orbit tree
    orbit_dic[parent].children.append(orbit_dic[child])
    orbit_dic[child].parent = orbit_dic[parent]

def recursive(orbiter, depth=0, total=0):
    total += depth
    if orbiter.children == []:
        return total
    else:
        for child in orbiter.children:
            total = recursive(child, depth+1, total)
    return total


print(f"Part 1 total: {recursive(orbit_dic['COM'])}")

# Part 2 solution only works because the branches never recombine. Find the path
# from YOU to COM, then find where the SAN->COM path intersects it and add up
# the total number of steps

x = orbit_dic['YOU']
path = []
while x is not orbit_dic['COM']:
    path.append(x)
    x = x.parent

x = orbit_dic['SAN']
count = 0
while x is not orbit_dic['COM']:
    if x in path:
        break
    x = x.parent
    count += 1

print(f'Part 2 Minimum jumps: {count + path.index(x) - 2}')
    

            

        
