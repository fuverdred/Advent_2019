import numpy as np
import re

from intcode_computer import Intcode_Computer


with open('inputs/input_17.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

computer = Intcode_Computer(intcode[:]+[0]*10000, [])
computer.run_code()

scaffold = ''.join([chr(i) for i in computer.outputs]).split('\n')[:-2]

directions = ((1,0), (0,1), (-1,0), (0,-1)) # Clockwise

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
                return np.array([i, j], dtype=np.int16)

def find_finish(scaffold):
    for i, row in enumerate(scaffold[1:-1],1):
        for j, val in enumerate(row[1:-1],1):
            if val == '#':
                if [scaffold[i+k][j+l] for k,l in directions] == ['#', '.', '.', '.']:
                    return np.array([i, j], dtype=np.int16)

def check_boundary(scaffold, coord):
    i, j = coord
    if i<0 or i>len(scaffold)-1:
        return False
    elif j<0 or j>len(scaffold[0])-1:
        return False
    return True

def path_find(scaffold):
    coord = find_start(scaffold)
    end = find_finish(scaffold)
    direction = 3
    instructions = 'L,' # Can see first instruction
    count = 0

    traverse = 0
    while tuple(coord) != tuple(end):
        new = coord + directions[direction]
        if check_boundary(scaffold, new) and scaffold[new[0]][new[1]] == '#':
            traverse += 1
            coord = new
        else:
            count += 1
            instructions += str(traverse)+','
            traverse = 0

            right = coord + directions[(direction+1)%4]
            if check_boundary(scaffold, right) and \
               scaffold[right[0]][right[1]]=='#':
                direction = (direction+1)%4
                instructions += 'L,'
            else:
                direction = (direction-1)%4
                instructions += 'R,'
    instructions += str(traverse) + ',' # add the last comma for matching
    return instructions

def routine_find(text, depth=0):
    for i in range(5,21):
        sub = re.compile(text[:i])
        if sub.pattern=='' or sub.pattern[-1] != ',':
            continue
        print(sub.pattern)
        text = ''.join(re.split(sub, text))
        if depth == 2:
            if text == '':
                return sub.pattern
        else:
            result = routine_find(text, depth+1)
            if result is not None:
                result = f'{result} {sub.pattern}'
                if depth == 0:
                    y = main_routine(text, *result.split())
                else:
                    return result
                                    
        

def main_routine(instructions, A, B, C):
    routines = {'A': A, 'B': B, 'C': C}
    routine_string = ''
    while instructions:
        for routine in routines.keys():
            if routines[routine] == instructions[:len(routines[routine])]:
                routine_string += routine + ','
                instructions = instructions[len(routines[routine]):]
                break
        else:
            return # Does not work
    return routine_string


## Part 2
instructions = path_find(scaffold)

A = 'L,6,L,4,R,12'
B = 'L,6,R,12,R,12,L,8'
C = 'L,6,L,10,L,10,L,6'
#routine = main_routine(instructions, A, B, C)
routine = 'A,B,A,C,B,A,C,B,A,C'

def asciify(x):
    return [ord(i) for i in x] + [10]

intcode[0] = 2
computer = Intcode_Computer(intcode+[0]*10000, [])
computer.inputs += [10, ord('n')]
for i in (C, B, A, routine):
    computer.inputs += asciify(i)[::-1]
