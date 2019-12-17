import numpy as np
import matplotlib.pyplot as plt

from intcode_computer import Intcode_Computer

with open('inputs/input_15.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

def recursive(position, depth=1, part_1=False, part_2 = False):
    if part_2:
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
            if status:
                recursive(position + direction, depth+1, part_1, part_2)
            if status==2 and part_1:
                print(f'Part 1 Minimum steps: {depth}')
                oxygen_position.append(droid.memory[:]) # Save this for part 2

#N, S, W, E. Movement code is the index + 1
directions = [(0,1), (0,-1), (-1,0), (1,0)]

# Part 1
visited_positions = set()
droid = Intcode_Computer(intcode, [])
oxygen_position = []

recursive(np.zeros(2, dtype=np.int16), part_1=True) # Find the extent of the maze, all values stored externally


# Part 2
max_depth = 0
droid = Intcode_Computer(oxygen_position[0], [])
visited_positions = set()

recursive(np.zeros(2, dtype=np.int16), depth=0, part_2=True)
print(f'Part 2 Time taken: {max_depth} minutes')
