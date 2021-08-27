import sys
import opcode_table2
import matplotlib.pyplot as plt
import numpy as np

def change_bit(value):
    global dict
    if (len(value) >= 8):
        bit = 16 - len(value)
        value = "0"*bit + value
    return value


def binaryToDecimal(binary):
    binary = str(binary)
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return (decimal)

def get_binary(number, bits):
    number = int(number)
    s = bin(number & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def passone():
    global program
    global registers
    global dict
    global jump

    global cycle_no
    global mem_address

    jump = {}

    use = 0
    for i in range(len(program)):
        op_code = program[i][:5]
        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

        for j in op_table:
            if (j == op_code):
                op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                instruction = op_table[j][0]
                type = op_table[j][1]

                if ((use != 0) and (i < use)):
                    continue

                elif (type == "A"):
                    reg1 = program[i][7:10]
                    reg2 = program[i][10:13]
                    reg3 = program[i][13:16]

                    if (instruction == "add"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = int(value1)
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = int(value2)
                                value2 = binaryToDecimal(value2)

                        after_add = value1 + value2
                        if (after_add >= 256):
                            registers[reg1] = "0000000000000000"
                            registers[FLAGS] = "0000000000001000"
                        else:
                            after_add = get_binary(after_add, 8)
                            after_add = change_bit(after_add)
                            registers[reg1] = after_add
                            registers[reg1] = "0000000000000000"

                    elif (instruction == "sub"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = int(value1)
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = int(value2)
                                value2 = binaryToDecimal(value2)

                        if (value1 > value2):
                            registers[reg1] = "0000000000000000"
                            registers[FLAGS] = "0000000000001000"
                        else:
                            after_sub = value1 - value2
                            after_sub = get_binary(after_sub, 8)
                            after_sub = change_bit(after_sub)
                            registers[reg1] = after_sub
                            registers[FLAGS] = "0000000000000000"


                    elif (instruction == "mul"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = int(value1)
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = int(value2)
                                value2 = binaryToDecimal(value2)

                        after_mul = value1*value2
                        if (after_mul >= 256):
                            registers[reg1] = "0000000000000000"
                            registers[FLAGS] = "0000000000001000"
                        else:
                            after_mul = get_binary(after_mul, 8)
                            after_mul = change_bit(after_mul)
                            registers[reg1] = after_mul
                            registers[FLAGS] = "0000000000000000"


                    elif (instruction == "or"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = binaryToDecimal(value2)

                        reg_or = value1 | value2
                        reg_or = get_binary(reg_or, 16)

                        registers[reg1] = reg_or

                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "xor"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = binaryToDecimal(value2)

                        reg_xor = value1 ^ value2
                        reg_xor = get_binary(reg_xor, 16)

                        registers[reg1] = reg_xor

                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "and"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg2):
                                value1 = op_table[x]
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg3):
                                value2 = op_table[y]
                                value2 = binaryToDecimal(value2)

                        reg_and = value1 & value2
                        reg_and = get_binary(reg_and, 16)

                        registers[reg1] = reg_and

                        registers[FLAGS] = "0000000000000000"

                elif (type == "B"):
                    op_code = program[i][:5]
                    op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                    if (instruction == "movi"):
                        reg = program[i][5:8]
                        number = program[i][8:]
                        number ="0"+change_bit(number)

                        for x in op_table:
                            if (x == reg):
                                registers[x] = number
                                registers[FLAGS] = "0000000000000000"


                    elif (instruction == "ls"):
                        reg = program[i][5:8]
                        number = program[i][8:]
                        number = binaryToDecimal(number)

                        no_of_times = 0
                        while (number != 1):
                            number = int(number/2)
                            no_of_times += 1

                        for x in op_table:
                            if (x == reg):
                                value = registers[x]
                                value = binaryToDecimal(value)
                                value = value << no_of_times
                                value = get_binary(value, 16)

                        for y in registers:
                            if (y == reg):
                                registers[y] = value

                                registers[FLAGS] = "0000000000000000"


                    elif (instruction == "rs"):
                        reg = program[i][5:8]
                        number = program[i][8:]
                        number = binaryToDecimal(number)

                        no_of_times = 0
                        while (number != 1):
                            number = int(number / 2)
                            no_of_times += 1

                        for x in op_table:
                            if (x == reg):
                                value = registers[x]
                                value = binaryToDecimal(value)
                                value = value >> no_of_times
                                value = get_binary(value, 16)

                        for y in registers:
                            if (y == reg):
                                registers[y] = value

                                registers[FLAGS] = "0000000000000000"


                elif (type == "C"):
                    if (instruction == "movr"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        reg1 = program[i][10:13]
                        reg2 = program[i][13:16]
                        for x in op_table:
                            if (x == reg2):
                                value = op_table[x]
                                for y in registers:
                                    if (y == reg1):
                                        registers[y] = value

                                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "div"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        reg1 = program[i][10:13]
                        reg2 = program[i][13:16]

                        for x in op_table:
                            if (x == reg1):
                                value1 = op_table[x]
                                value1 = int(value1)
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg2):
                                value2 = op_table[y]
                                value2 = int(value2)
                                value2 = binaryToDecimal(value2)

                        remainder = value1%value2
                        value1 = value1 - remainder
                        quotient = int(value1/value2)

                        remainder = get_binary(remainder, 16)
                        quotient = get_binary(quotient, 16)

                        registers[R0] = quotient
                        registers[R1] = remainder

                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "not"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        reg1 = program[i][10:13]
                        reg2 = program[i][13:16]
                        for y in op_table:
                            if (y == reg2):
                                value2 = op_table[y]
                                value2 = binaryToDecimal(value2)

                                reg_help = ~value2
                                reg_help = get_binary(reg_help, 16)
                                for x in registers:
                                    if (x == reg1):
                                        registers[x] = reg_help

                                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "cmp"):
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        reg1 = program[i][10:13]
                        reg2 = program[i][13:16]

                        for x in op_table:
                            if (x == reg1):
                                value1 = op_table[x]
                                value1 = int(value1)
                                value1 = binaryToDecimal(value1)
                        for y in op_table:
                            if (y == reg2):
                                value2 = op_table[y]
                                value2 = int(value2)
                                value2 = binaryToDecimal(value2)

                        if (value1 < value2):
                            registers[FLAGS] = "0000000000000100"

                        elif (value1 > value2):
                            registers[FLAGS] = "0000000000000010"

                        elif (value1 == value2):
                            registers[FLAGS] = "0000000000000001"



                elif (type == "D"):
                    if (instruction == "st"):
                        reg = program[i][5:8]
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg):
                                dict[program[i][8:]] = op_table[x]

                                registers[FLAGS] = "0000000000000000"

                    elif (instruction == "ld"):
                        reg = program[i][5:8]
                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])
                        for x in op_table:
                            if (x == reg):
                                address = program[i][8:]
                                if address in dict:
                                    value = dict[address]
                                    value = change_bit(value)
                                    for y in registers:
                                        if (x == y):
                                            registers[y] = value

                                            registers[FLAGS] = "0000000000000000"


                elif (type == "E"):
                    if (instruction == "jmp"):
                        use = program[i][8:]
                        use = binaryToDecimal(use)
                        jump[i] = use
                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "jlt"):
                        if (registers[FLAGS] == "0000000000000100"):
                            use = program[i][8:]
                            use = binaryToDecimal(use)
                            jump[i] = use
                        elif (registers[FLAGS] == "0000000000000000"):
                            use = 0

                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "jgt"):
                        if (registers[FLAGS] == "0000000000000010"):
                            use = program[i][8:]
                            use = binaryToDecimal(use)
                            jump[i] = use
                        elif (registers[FLAGS] == "0000000000000000"):
                            use = 0

                        registers[FLAGS] = "0000000000000000"

                    elif (instruction == "je"):
                        if (registers[FLAGS] == "0000000000000001"):
                            use = program[i][8:]
                            use = binaryToDecimal(use)
                            jump[i] = use
                        elif (registers[FLAGS] == "0000000000000000"):
                            use = 0

                        registers[FLAGS] = "0000000000000000"


                elif (type == "F"):
                    if (instruction == "hlt"):
                        registers[FLAGS] = "0000000000000000"




    w = 0
    for j in range(len(program)):
        instruct = program[j][:5]
        if ((w != 0) and (j < w)):
            continue

        elif (len(jump) == 0):
            if ((instruct == "00101") or (instruct == "00100")):
                cycle_no.append(j)
                cycle_no.append(j)
                mem_address.append(j)

                s = program[j][8:]
                s = binaryToDecimal(s)
                mem_address.append(s)

            else:
                cycle_no.append(j)
                mem_address.append(j)


        elif (len(jump) != 0):
            if ((instruct == "00101") or (instruct == "00100")):
                cycle_no.append(j)
                cycle_no.append(j)
                mem_address.append(j)

                s = program[j][8:]
                s = binaryToDecimal(s)
                mem_address.append(s)                             

            elif ((instruct == "01111") or (instruct == "10000") or (instruct == "10001") or (instruct == "10010")):
                if (j not in jump):
                    cycle_no.append(j)
                    mem_address.append(j)
                elif (j in jump):
                    cycle_no.append(j)
                    mem_address.append(j)
                    w = jump[j]
                else:
                    cycle_no.append(j)
                    mem_address.append(j)



def main():
    global program
    global registers
    global dict
    global R0
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global FLAGS

    global cycle_no
    global mem_address

    cycle_no = []
    mem_address = []

    R0 = "000"
    R1 = "001"
    R2 = "010"
    R3 = "011"
    R4 = "100"
    R5 = "101"
    R6 = "110"
    FLAGS = "111"


    dict = {}
    registers = {R0: "0000000000000000",
                 R1: "0000000000000000",
                 R2: "0000000000000000",
                 R3: "0000000000000000",
                 R4: "0000000000000000",
                 R5: "0000000000000000",
                 R6: "0000000000000000",
                 FLAGS: "0000000000000000"}

    a = []
    while True:
        for line in sys.stdin:
            a.append(line)
        break
    program = a
    passone()
    x = cycle_no
    y = mem_address
    plt.scatter(x, y)
    plt.title("MEMORY ADDRESS VS CYCLE NO.")
    plt.yticks(np.arange(0, 255, 10))
    plt.xticks(np.arange(0, 255, 50))
    plt.xlabel("cycles")
    plt.ylabel("memory address")
    plt.show()
    


if __name__ == '__main__':
    main()