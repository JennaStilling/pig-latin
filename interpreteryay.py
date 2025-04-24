import sys
# Most commments are copied from the video provided, the rest for labeling. Anything from AI is marked with AI

# read arguments
program_filepath = sys.argv[1]

# Tokenize Program

# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}

for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # empty
    if opcode == "":
        continue
    
    # check if its a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # store opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "USHPAY": # push
        # expecting a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "INTPRAY": # print
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "UMPJAYEQUALYAYEROZAY": # jump if equal
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "UMPJAYEATERGRAYEROZAY": # jump if greater
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1

# Interpret Program

class Stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1 # sp = stack pointer

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]
    
pc = 0 # program counter
building_string = ""
building_number = 0
stack = Stack(256)

while program[pc] != "ALTHAY": # halt
    opcode = program[pc]
    pc +=1

    if opcode == "USHPAY": # push
        number = program[pc]
        pc += 1
        stack.push(number)
        # print(stack.buf[:stack.sp + 1])
    elif opcode == "OPPAY": # pop
        print(chr(stack.pop()))
    elif opcode == "ADDYAY": # add
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "UBSAY": # sub
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
        # print(stack.buf[:stack.sp + 1])
    elif opcode == "INTPRAY": # print
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "EADRAY":
        _input = input()
        for char in _input:
            stack.push(ord(char)) 
        # print(stack.buf[:stack.sp + 1])
    elif opcode == "UMPJAYEQUALYAYEROZAY": # jump if equal
        # print("Checking equal to 0: ", stack.buf[:stack.sp + 1])
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "UMPJAYEATERGRAYEROZAY": # jump if greater
        # ("Checking greater than 0: ", stack.buf[:stack.sp + 1])
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "ULMAY": # mul
        a = (chr(stack.pop()))
        b = (chr(stack.pop()))
        result = 0
        for i in range(0,int(b)):
            result += int(a)
        stack.push(result)
    elif opcode =="ECHOYAY": # echo
        print(building_string)
    elif opcode == "UPLICATEDAY": # duplicate
        stack.push(stack.top())
        # print(stack.buf[:stack.sp + 1])
    elif opcode == "UILDBAY":
        counter = stack.pop()
        building_string += chr(stack.pop())
        stack.push(counter)
    # elif opcode == "OINTERPAY":
        # number = stack.pop()
        # print(chr(number))
    elif opcode == "OPTAY":
        print(stack.pop())
    elif opcode == "APSWAY":
        # print(stack.buf[:stack.sp + 1])
        first = stack.pop()
        second = stack.pop()
        stack.push(first)
        stack.push(second)
        # print("Swapped ", stack.buf[:stack.sp + 1])
    elif opcode == "ISERAY":
        size = stack.top()
        print()
    elif opcode == "IZESAY":
        stack.push(len(stack.buf[:stack.sp + 1]))
        print(stack.buf[:stack.sp + 1])