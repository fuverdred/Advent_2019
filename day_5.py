with open('inputs/input_5.txt', 'r') as f:
    intcode = [int(i) for i in f.read()[:-1].split(',')]

def opcode_1(memory, index):
    '''ADD'''
    modes = parameter_modes(memory[index], 2) #  Third is always position mode
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    memory[memory[index+3]] = values[0] + values[1]
    return memory, index+4

def opcode_2(memory, index):
    '''MULTIPLY'''
    modes = parameter_modes(memory[index], 2) #  Third is always position mode
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    memory[memory[index+3]] = values[0] * values[1]
    return memory, index+4
        
def opcode_3(memory, index):
    '''INPUT'''
    value = int(input('Enter some input: '))
    address = memory[index + 1]
    memory[address] = value
    return memory, index + 2

def opcode_4(memory, index):
    '''OUTPUT'''
    modes = parameter_modes(memory[index], 1)
    address = memory[index+1]
    if modes[0]:
        print(address)
    else:
        print(memory[address])
    return memory, index + 2

def opcode_5(memory, index):
    '''JUMP-IF-TRUE'''
    modes = parameter_modes(memory[index], 2)
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    if values[0] != 0:
        return memory, values[1]
    return memory, index + 3

def opcode_6(memory, index):
    '''JUMP-IF-FALSE'''
    modes = parameter_modes(memory[index], 2)
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    if values[0] == 0:
        return memory, values[1]
    return memory, index + 3

def opcode_7(memory, index):
    '''LESS THAN'''
    modes = parameter_modes(memory[index], 2)
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    if values[0] < values[1]:
        memory[memory[index+3]] = 1
    else:
        memory[memory[index+3]] = 0
    return memory, index + 4

def opcode_8(memory, index):
    '''EQUALS'''
    '''LESS THAN'''
    modes = parameter_modes(memory[index], 2)
    values = [memory[index+i+1] if modes[i] else
              memory[memory[index+i+1]] for i in range(2)]
    if values[0] == values[1]:
        memory[memory[index+3]] = 1
    else:
        memory[memory[index+3]] = 0
    return memory, index + 4
    
    

opcodes = {1: opcode_1,
           2: opcode_2,
           3: opcode_3,
           4: opcode_4,
           5: opcode_5,
           6: opcode_6,
           7: opcode_7,
           8: opcode_8}


def parse_opcode(opcode):
    return int(('0' + str(opcode))[-2:]) # bodge bodge bodge

def parameter_modes(opcode, n):
    '''Returns array of modes, False for position mode, True for immediate'''
    opcode = str(opcode)
    if len(opcode) == 1:
        return [False] * n ## All position mode
    else:
        return [True if i=='1' else False
                for i in opcode[:-2][::-1]+n*'0'][:n] #  Good luck
           
def runcode(memory):        
    index = 0
    count = 0

    while True:
        count += 1
        opcode = parse_opcode(memory[index])
        if opcode == 99:
            return # program finished
        memory, index = opcodes[opcode](memory, index)

test = [3,0,4,0,99]
