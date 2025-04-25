import sys
# Most commments are copied from the video provided, the rest for labeling. Nothing is from AI

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

while program[pc] != "ALTHAY":
    opcode = program[pc]
    pc +=1

    if opcode == "USHPAY":
        number = program[pc]
        pc += 1
        stack.push(number)
        print("Pushed ", stack.buf[:stack.sp + 1])
    elif opcode == "OPPAY":
        print(chr(stack.pop()))
    elif opcode == "ADDYAY": 
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
        print("Added ", stack.buf[:stack.sp + 1])
    elif opcode == "UBSAY":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
        print("Subtracted ", stack.buf[:stack.sp + 1])
    elif opcode == "INTPRAY":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "EADRAY":
        _input = input()
        for char in _input:
            stack.push(ord(char)) 
        print("Read: ",stack.buf[:stack.sp + 1])
    elif opcode == "UMPJAYEQUALYAYEROZAY": 
        print("Checking equal to 0: ", stack.buf[:stack.sp + 1])
        number = stack.top()
        if number <= 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "UMPJAYEATERGRAYEROZAY":
        ("Checking greater than 0: ", stack.buf[:stack.sp + 1])
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode =="ECHOYAY":
        print(building_string)
    elif opcode == "UPLICATEDAY": 
        stack.push(stack.top())
        print("Duplicated ", stack.buf[:stack.sp + 1])
    elif opcode == "UILDBAY":
        counter = stack.pop()
        building_string += chr(stack.pop())
        stack.push(counter)
    elif opcode == "OPTAY":
        print("Final result: ", stack.pop())
    elif opcode == "APSWAY":
        print("Swapping ", stack.buf[:stack.sp + 1])
        if stack.sp > 0:
            first = stack.pop()
            second = stack.pop()
            stack.push(first)
            stack.push(second)
        print("Swapped ", stack.buf[:stack.sp + 1])
    elif opcode == "ISERAY":
        print("Moving bottom to top ", stack.buf[:stack.sp + 1])
        if stack.sp > 0:
            bottom_value = stack.buf[0]  
            for i in range(stack.sp):
                stack.buf[i] = stack.buf[i + 1]
            stack.buf[stack.sp] = bottom_value
        print("Moved bottom to top ", stack.buf[:stack.sp + 1])
    elif opcode == "IZESAY":
        stack.push(len(stack.buf[:stack.sp + 1]))
        print(stack.buf[:stack.sp + 1])
    elif opcode == "ELETEDAY":
        print("Deleted ", stack.pop())
    elif opcode == "EVERSERAY":
        if stack.sp > 0:
            bottom_value = stack.buf[0]  
            for i in range(stack.sp):
                stack.buf[i] = stack.buf[i + 1]
            building_string += chr(bottom_value)
        print(stack.buf[:stack.sp + 1])
    elif opcode == "IRDTHAY": 
        if stack.sp >= 2:
            top_index = stack.sp
            third_index = stack.sp - 2
            stack.buf[top_index], stack.buf[third_index] = stack.buf[third_index], stack.buf[top_index]
            print("Swapped first and third: ", stack.buf[:stack.sp + 1])