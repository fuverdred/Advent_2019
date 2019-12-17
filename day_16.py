from math import ceil

with open('inputs/input_16.txt', 'r') as f:
    inputs = [int(i) for i in f.read().strip('\n')]

base_pattern = [0, 1, 0, -1]
test = '12345678'

def nth_pattern(n, N):
    pattern = [i for i in base_pattern for _ in range(n)]
    multiplier = ceil((N+1)/len(pattern))
    return multiplier * pattern
    

def compute_phase(inputs):
    N = len(inputs)
    new = []
    for n, val in enumerate(inputs,1):
        pattern = nth_pattern(n, N)
        total = sum([pattern[i]*val for i,val in enumerate(inputs, 1)])
        new.append(abs(total)%10)
    return new
            

# Part 1
part_1 = inputs[:]
for _ in range(100):
    part_1 = compute_phase(part_1)
print(f"Part 1: {''.join([str(i) for i in part_1[:8]])}")

# Part 2
inputs *= 10000

message_offset = int(''.join([str(i) for i in inputs[:7]]))
inputs = inputs[message_offset:]

for _ in range(100):
    for i in range(-2, -len(inputs)-1, -1):
        inputs[i] = (inputs[i] + inputs[i+1]) % 10

print(f"Part 2: {''.join([str(i) for i in inputs[:8]])}")


