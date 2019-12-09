with open('inputs/input_9.txt', 'r') as f:
    intcode = [int(c) for c in f.read().strip('\n').split(',')]

from intcode_computer import Intcode_Computer

test = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

comp = Intcode_Computer(intcode[:]+[0]*100, [1])
comp.run_code()
print(f'Part 1: {comp.outputs[0]}')
comp = Intcode_Computer(intcode[:]+[0]*1000, [2])
comp.run_code()
print(f'Part 2: {comp.outputs[0]}')

