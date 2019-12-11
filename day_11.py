from intcode_computer import Intcode_Computer
import matplotlib.pyplot as plt
import numpy as np

with open('inputs/input_11.txt', 'r') as f:
    intcode = [int(i) for i in f.read().strip('\n').split(',')]

class Robot:
    directions = ('^', '>', 'v', '<') # rotating clockwise in order
    moves = {'^': (1,0), '>': (0,1), 'v': (-1,0), '<': (0,-1)}
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.direction_index = 0 # index in self.directions
        self.direction = self.directions[self.direction_index]

    def turn(self, turn_direction):
        if turn_direction: # Turn left
            return (self.direction_index - 1) % 4
        else: # Turn right
            return (self.direction_index + 1) % 4

    def detect(self, grid):
        return grid[self.i][self.j]

    def move(self):
        up, right = self.moves[self.direction]
        self.i += up
        self.j += right

    def spray_grid(self, grid, paint):
        grid[self.i][self.j] = paint

    def run(self, grid, paint, turn_direction):
        self.spray_grid(grid, paint)
        self.direction_index = self.turn(turn_direction)
        self.direction = self.directions[self.direction_index]
        self.move()
        return self.detect(grid)

robot = Robot(75, 75)
brain = Intcode_Computer(intcode+[0]*1000, [1])

visited_panels = set()

grid = [[0 for _ in range(150)] for _  in range(150)]
grid[75][75] = 1

while 1:
    output = brain.run_code()
    if output is None:
        break
    new_panel = robot.run(grid, *output)
    visited_panels.add((robot.i, robot.j))
    brain.inputs.append(new_panel)
    brain.outputs = []

plt.imshow(np.array(grid))
plt.show()
    
