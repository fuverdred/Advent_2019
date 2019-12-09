class Intcode_Computer():
    def __init__(self, intcode, inputs):
        '''
        Takes intcode and inputs as a list of integers
        '''
        self.index = 0
        self.relative_base = 0
        self.memory = intcode

        self.inputs = inputs
        self.outputs = []

        self.opcodes = {1: self.opcode_1,
                        2: self.opcode_2,
                        3: self.opcode_3,
                        4: self.opcode_4,
                        5: self.opcode_5,
                        6: self.opcode_6,
                        7: self.opcode_7,
                        8: self.opcode_8,
                        9: self.opcode_9}

        self.finished = False

    def parse_modes(self, opcode):
        # 1 if immediate mode, 0 for position mode
        # Always returns the maximum  possible required number of modes
        return [opcode // i % 10 for i in (100, 1000, 10000)]

    def opcode_1(self):
        '''ADD'''
        modes = self.parse_modes(self.memory[self.index])
        values = []
        for mode in modes[:2]:
            self.index += 1 # Move to next value to evaluate
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value] #  Position mode
            if mode == 2:
                value = self.memory[self.relative_base + value]
            values.append(value)
        self.index += 1 # go to third param
        value = self.memory[self.index]
        if modes[2] == 2:
            self.memory[self.relative_base+value] = values[0]+values[1]
        else:
            self.memory[value] = values[0] + values[1]
        self.index += 1 #  Move to next instruction

    def opcode_2(self):
        '''MULTIPLY'''
        modes = self.parse_modes(self.memory[self.index])
        values = []
        for mode in modes[:2]:
            self.index += 1 # Move to next value to evaluate
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value] #  Position mode
            if mode == 2:
                value = self.memory[self.relative_base + value]
            values.append(value)
        self.index += 1 # go to third param
        value = self.memory[self.index]
        if modes[2] == 2:
            self.memory[self.relative_base+value] = values[0] * values[1]
        else:
            self.memory[value] = values[0] * values[1]
        self.index += 1 #  Move to next instruction

    def opcode_3(self):
        '''INPUT'''
        try:
            value_in = self.inputs.pop()
        except IndexError:
            print("INPUT QUEUE EMPTY")
            return
        mode = self.parse_modes(self.memory[self.index])[0]
        self.index += 1
        value = self.memory[self.index]
        if mode == 2:
            value = self.relative_base + value
        self.memory[value] = value_in
        self.index += 1 #  Move to next instruction

    def opcode_4(self):
        '''OUTPUT'''
        mode = self.parse_modes(self.memory[self.index])[0]
        self.index += 1 # Move to value
        value = self.memory[self.index]
        if mode == 0:
            value = self.memory[value] # Position mode
        if mode == 2:
            value = self.memory[self.relative_base + value]
        self.outputs.append(value)
        self.index += 1 #  Move to next instruction

    def opcode_5(self):
        '''JUMP-IF-TRUE'''
        modes = self.parse_modes(self.memory[self.index])[:2]
        values = []
        for mode in modes:
            self.index += 1 # move to next value
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value]
            if mode == 2:
                value = self.memory[self.relative_base + value]
            values.append(value)
        if values[0] != 0:
            self.index = values[1] # Jump
            return
        self.index += 1 # Move to next instruction

    def opcode_6(self):
        '''JUMP-IF-FALSE'''
        modes = self.parse_modes(self.memory[self.index])[:2]
        values = []
        for mode in modes:
            self.index += 1 # move to next value
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value]
            if mode == 2:
                value = self.memory[self.relative_base + value]
            values.append(value)
        if values[0] == 0:
            self.index = values[1] # Jump
            return
        self.index += 1 # Move to next instruction

    def opcode_7(self):
        '''LESS THAN'''
        modes = self.parse_modes(self.memory[self.index])
        values = []
        for mode in modes[:2]:
            self.index += 1 # move to next value
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value]
            if mode == 2:
                value = self.memory[self.relative_base+value]
            values.append(value)
        self.index += 1
        address = self.memory[self.index]
        if modes[2] == 2:
            address = self.relative_base + address
        
        if values[0] < values[1]:
            self.memory[address] = 1
        else:
            self.memory[address] = 0
        self.index += 1 # Move to next instruction

    def opcode_8(self):
        '''EQUAL'''
        modes = self.parse_modes(self.memory[self.index])
        values = []
        for mode in modes[:2]:
            self.index += 1 # move to next value
            value = self.memory[self.index]
            if mode == 0:
                value = self.memory[value]
            if mode == 2:
                value = self.memory[self.relative_base+value]
            values.append(value)
        self.index += 1
        address = self.memory[self.index]
        if modes[2] == 2:
            address = self.relative_base + address
        
        if values[0] == values[1]:
            self.memory[address] = 1
        else:
            self.memory[address] = 0
        self.index += 1 # Move to next instruction

    def opcode_9(self):
        '''ADJUST RELATIVE BASE'''
        mode = self.parse_modes(self.memory[self.index])[0]
        self.index += 1
        value = self.memory[self.index]
        if mode == 0:
            value = self.memory[value]
        if mode == 2:
            value = self.memory[self.relative_base + value]
        self.relative_base += value
        self.index += 1 # Move to next instruction

    def run_code(self):
        while True:
            op = self.memory[self.index] % 100
            if op == 99:
                self.finished = True
                return
            self.opcodes[op]() # execute the instruction
##            if self.outputs != []:
##                return self.outputs.pop()
            
        
    
            
        
