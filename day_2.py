from collections import defaultdict

with open('inputs/input_2.txt', 'r') as f:
    intcode = [int(i) for i in f.read().split(',')]
    
def opcode_1(a, b):
    return a + b

def opcode_2(a, b):
    return a * b

opcodes = {1: opcode_1,
           2: opcode_2,
           99: True}

def runcode(memory):
    index = 0 #  Instruction pointer

    while 1:
        op = opcodes[memory[index]]
        if op is True:
            return memory

        address_1, address_2, address_3 = memory[index+1:index+4]
        memory[address_3] = op(memory[address_1], memory[address_2])

        index += 4


if __name__ == '__main__':
    # Part 1
    intcode[1] = 12
    intcode[2] = 2
    part_1 = runcode(intcode[:]) #  Make a copy of the intcode
    print(f'Part 1: {part_1[0]}')

    #Part 2
    def part_2():
        for noun in range(0,100):
            for verb in range(0, 100):
                intcode[1] = noun
                intcode[2] = verb
                result = runcode(intcode[:])
                if result[0] == 19690720:
                    return noun, verb
    noun, verb = part_2()
    print(f'Part 2: Noun: {noun}, Verb: {verb}, Answer:{100*noun+verb}')
