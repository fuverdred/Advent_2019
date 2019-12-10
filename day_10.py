from math import atan2, pi
from collections import defaultdict

with open('input_10.txt', 'r') as f:
    data = [[c for c in row[:-1]] for row in f.readlines()]

# If any line as the same equation and is in the same 'hemisphere' as another
# asteroid then it is not detectable.

test = '''
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
'''

test = [[c for c in row] for row in test.split('\n')[1:-1]]


class Asteroid:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.coords = []

    def polar(self, a):
        r = ((self.i-a.i)**2 + (self.j-a.j)**2)**0.5
        return r, atan2(self.i-a.i, self.j-a.j)

    def LOS(self, asteroids):
        for a in asteroids:
            if a is not self:
                self.coords.append((a, *self.polar(a)))

    def convert_angle(self, theta):
        if theta <= pi/2:
            theta = pi/2 - theta
        elif theta < 0:
            theta = pi/2 - theta
        else:
            theta = 2*pi - (theta-pi/2)
        return theta
        
#data = test
asteroids = [Asteroid(i, j) for i, row in enumerate(data)
             for j, c in enumerate(row) if c=='#']



for a in asteroids:
    a.LOS(asteroids)

asteroids.sort(key=lambda x: len({c[2] for c in x.coords}))
print(f'part 1: {len({c[2] for c in asteroids[-1].coords})}')

base = asteroids.pop()
print(base.j, base.i)
angle_dic = defaultdict(list)
for a,r,theta in base.coords:
    theta = base.convert_angle(theta)
    angle_dic[theta].append((a, r))

for key in angle_dic.keys():
    angle_dic[key].sort(key=lambda x: x[1], reverse=True)

keys = list(angle_dic.keys())
keys.sort()

order = []
length_order = -1
while length_order != len(order):
    length_order = len(order)
    for key in keys[::-1]: # going clockwise
        if angle_dic[key] != []:
            a, r = angle_dic[key].pop()
            order.append((a, r, key))
    

print(order[198][0].j*100 + order[198][0].i)




