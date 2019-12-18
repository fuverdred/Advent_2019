from intcode_computer import Intcode_Computer


with open('inputs/input_17.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

computer = Intcode_Computer(intcode+[0]*10000, [])
computer.run_code()

scaffold = ''.join([chr(i) for i in computer.outputs]).split('\n')[:-2]

directions = ((1,0), (0,1), (-1,0), (0,-1))

def intersection_finder(scaffold, i, j):
    for k, l in directions:
        if scaffold[i+k][j+l] != '#':
            return 0
    return i * j

x = [intersection_finder(scaffold, i, j)
     for i, row in enumerate(scaffold[1:-1],1)
     for j, val in enumerate(row[1:-1],1) if val == '#']

print(f'Part 1: {sum(x)}')

def find_start(scaffold):
    for i, row in enumerate(scaffold):
        for j, val in enumerate(row):
            if val == '^':
                return [i, j]

def find_finish(scaffold):
    for i, row in enumerate(scaffold[1:-1],1):
        for j, val in enumerate(row[1:-1],1):
            if val == '#':
                if [scaffold[i+k][j+l] for k,l in directions] == ['#', '.', '.', '.']:
                    return [i, j]

def path_find(scaffold):
    coord = find_start(scaffold)
    end = find_end(scaffold)
