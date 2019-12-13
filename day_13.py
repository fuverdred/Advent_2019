import numpy as np
import matplotlib.pyplot as plt

from intcode_computer import Intcode_Computer

with open('inputs/input_13.txt', 'r') as f:
    intcode = [int(c) for c in f.read().strip('\n').split(',')]

computer = Intcode_Computer(intcode[:]+[0]*10000, [])

data = []
while 1:
    line = computer.run_code()
    computer.outputs = []
    if line is None:
        break
    data.append(line)

print(f'Part 1: {len([i for i in data if i[-1]==2])}')


## Part 2

grid = np.zeros((max([i[1] for i in data])+1,max([i[0] for i in data])+1))
for x,y,val in data:
    if val == 4:
        paddle_x = x
    grid[y][x] = val

plt.imshow(grid)
plt.show()

computer = Intcode_Computer([2]+intcode[1:]+[0]*100000, [-1])

GAME_START = [-1, 0, 0]
started = False
data = []

while 1:
    line = computer.run_code()
    computer.outputs = []
    if line is None:
        break
    data.append(line)

    if line == GAME_START:
        started = True
    if line[-1] == 3:
        paddle_x = line[0]
    if line[-1] == 4 and started:
        if line[0] < paddle_x:
            computer.inputs.append(-1)
        elif line[0] > paddle_x:
            computer.inputs.append(1)
        else:
            computer.inputs.append(0)
    if line[:2] == [-1,0]:
        print(line[2])
    
