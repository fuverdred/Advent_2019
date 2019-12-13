import matplotlib.pyplot as plt
import numpy as np

with open('inputs/input_12.txt', 'r') as f:
    initials = [[int(i.split('=')[1].strip('>')) for i in moon.split(',')]
                for moon in f.read().split('\n')[:-1]]


##test = '<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>\n'
##initials = [[int(i.split('=')[1].strip('>')) for i in moon.split(',')]
##                for moon in test.split('\n')[:-1]]

class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0,0,0]
        self.energy = 0
        self.update_energy()

    def update_velocity(self, moon):
        for i in range(3):
            if self.position[i] < moon.position[i]:
                self.velocity[i] += 1
            elif self.position[i] > moon.position[i]:
                self.velocity[i] -= 1

    def update_position(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def update_energy(self):
        self.energy =  sum([abs(i) for i in self.position])*\
                       sum([abs(i) for i in self.velocity])


moons = [Moon(moon[:]) for moon in initials]
        
count = 0

periods = [None, None, None]

while 1:
    count += 1
    for moon in moons:
        for other_moon in moons:
            moon.update_velocity(other_moon) # won't change self
    for moon in moons:
        moon.update_position()
        moon.update_energy()
    for i in range(3):
        if [m.position[i] for m in moons] == [m[i] for m in initials] and\
           [m.velocity[i] for m in moons] == [0,0,0,0]:
            if not periods[i]:
                periods[i] = count
    if all(periods):
        break

print(f'Periods: {periods}')


            
