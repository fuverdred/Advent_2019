from itertools import permutations

from intcode_computer import Intcode_Computer

with open('inputs/input_7.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

## PART 1
best = 0
for phase in permutations(range(5)):
    amplitude = 0
    for p in phase:
        amplifier = Intcode_Computer(intcode[:], [amplitude, p])
        amplitude = amplifier.run_code()
    if amplitude > best:
        best = amplitude

print(best)
    
## PART 2
best = 0
for phase in permutations(range(5, 10)):
    amplitude = 0
    amplifiers = []
    outputs = []
    for p in phase:
        amplifiers.append(Intcode_Computer(intcode[:], [amplitude, p]))
        amplitude = amplifiers[-1].run_code()
    index = 0
    while not amplifiers[-1].finished:
        amplifiers[index%5].inputs = [amplitude]
        amplitude = amplifiers[index%5].run_code()
        if index%5 == 4 and amplitude is not None:
            outputs.append(amplitude)
        index += 1
    if outputs[-1] > best:
        best = outputs[-1]
print(best)
        
    
