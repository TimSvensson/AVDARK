import importlib

memory = importlib.import_module('memory')

# OPCODES
add = '+'
sub = '-'

addi = '+i'
subi = '-i'

load = 'l'
store = 's'

loadi = 'li'
storei = 'si'

jmp = 'j'
jgt = 'j+'
jlt = 'j-'
j0 = 'j0'

nop = '0'

# Instruction shorthands for dictionary instructions.
opcode = 'opcode'
src1 = 'src1'
src2 = 'src2'
im = 'im'
jmp = 'jmp'
dst = 'dst'

def instruction(_opcode, _src1, _src2, _im, _jmp, _dst):
    return {opcode:_opcode, src1:_src1, src2:_src2, im:_im, jmp:_jmp, dst:_dst}

class cpu:

    def __init__(self, _instructions, _number_of_registers, _memory):
        # Instructions
        self.instruction_index = 0
        self.instructions = _instructions
        self.number_of_instructions = len(self.instructions)
        
        # Registers
        self.number_of_register = _number_of_registers
        self.register = [0] * self.number_of_register
        
        # Cache
        pass
        
        # Memory
        self.memory = _memory

    def __str__(self):
        return "Class: {}\n\nInstruction Index: {}\nInstructions:\n{}\n\nRegisters:\n{}\n\nMemory:\n{}".format(
            self.__class__.__name__,
            self.instruction_index,
            self.instructions,
            self.register,
            self.memory)
        
    def pipeline(self):

        # Instruction fetch
        instruction = self.instructions[self.instruction_index]

        # Instruction decode
        op = instruction[opcode]

        # Data load
        src1 = instruction[src1]
        src2 = instruction[src2]
        im = instruction[im]
        jmp = instruction[jmp]
        dst = instruction[dst]

        # Execute operation
        result = None
        
        if op == add:
            result = self.register[src1] + self.register[src2]
        elif op == sub:
            result = self.register[src1] - self.register[src2]
        elif op == addi:
            result = self.register[src1] + im
        elif op == subi:
            result = self.register[src1] - im
        elif op == load:
            result = self.memory.load(src1)
        elif op == store:
            result = self.register[src1]
        elif op == loadi:
            result = im
        elif op == storei:
            result = im

        # Write back
        if op == store or op == storei:
            self.memory.store(result, dst)
        else:
            self.register[dst] = result

        # Update instruction index
        self.instruction_index += 1
    
    def run(self):
        while self.instruction_index < self.number_of_instructions:
            self.pipeline()

    def load_instructoins(self, instructions):
        self.instructions = instructions
        self.number_of_instructions = len(instructions)
        self.instruction_index = 0
        
if __name__ == "__main__":

    # opcode, src1, src2, im ,jmp, dst
    i = [
        instruction(addi, 0, None, 2, None, 0),
        instruction(addi, 0, None, 1, None, 1),
        instruction(add, 0, 1, None, None, 2),
        instruction(store, 0, None, None, None, 0),
        instruction(store, 1, None, None, None, 1),
        instruction(store, 2, None, None, None, 2)
        ]
    m = memory.memory(8)
    cpu = cpu(i, 4, m)
    
    print(cpu)
    cpu.run()
    print(cpu)
