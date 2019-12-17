import numpy as np
import matplotlib.pyplot as plt

from intcode_computer import Intcode_Computer

with open('inputs/input_15.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

def recursive(position, depth=1):
    global max_depth
    if depth > max_depth:
        max_depth = depth
    memory_copy = droid.memory[:] # Save the state of the computer at each step
    for index, direction in enumerate(directions, 1):
        if tuple(position + direction) not in visited_positions:
            visited_positions.add(tuple(position + direction))
            droid.inputs.append(index)
            droid.memory = memory_copy[:]
            status = droid.run_code()

            grid.add(tuple(np.append(position+direction, status)))

            if status:
                recursive(position + direction, depth+1)
            if status==2:
                print(f'Part 1: Minimum steps {depth}')
                oxygen_position.append(droid.memory[:])

#N, S, W, E. Movement code is the index + 1
directions = [(0,1), (0,-1), (-1,0), (1,0)]
max_depth = 0 # Only relevant in second part

visited_positions = set() # Just coords
grid = set() # Coords and square type (free, wall , Oxygen thing)

droid = Intcode_Computer(intcode, [])
coord = np.zeros(2, dtype=np.int16)
oxygen_position = []

recursive(coord) # Find the extent of the maze, all values stored externally

grid = np.array(list(grid))
min_x = min(grid[:,0])
min_y = min(grid[:,1])
grid[:,0] += abs(min_x)
grid[:,1] += abs(min_y)
display = np.zeros((max(grid[:,1])+1, max(grid[:,0])+1), dtype=np.int16)
for x,y,val in grid:
    display[y][x] = val
display[abs(min_y)][abs(min_x)] = 10
plt.imshow(display, origin='lower')
plt.show()

# Part 2
max_depth = 0
droid = Intcode_Computer(oxygen_position[0], [])
visited_positions = set() # Just coords
grid = set() # Coords and square type (free, wall , Oxygen thing)
coord = np.zeros(2, dtype=np.int16)

recursive(coord)
print(max_depth-1)
