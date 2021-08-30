import sys

import opcode_table2

import math



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

                        after_add = get_binary(after_add, 16)

                        after_add = change_bit(after_add)

                        registers[reg1] = after_add

                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



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



                        if (value1 < value2):

                            registers[reg1] = "0000000000000000"

                            registers[FLAGS] = "0000000000001000"

                        else:

                            after_sub = value1 - value2

                            after_sub = get_binary(after_sub, 16)

                            after_sub = change_bit(after_sub)

                            registers[reg1] = after_sub

                            registers[FLAGS] = "0000000000000000"



                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



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

                        # if (after_mul >= 256):

                        #     registers[reg1] = "0000000000000000"

                        #     registers[FLAGS] = "0000000000001000"

                        # else:

                        after_mul = get_binary(after_mul, 16)

                        after_mul = change_bit(after_mul)

                        registers[reg1] = after_mul

                        registers[FLAGS] = "0000000000000000"



                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "or"):

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        for x in op_table:

                            if (x == reg2):

                                value1 = op_table[x]

                                value1 = binaryToDecimal(int(value1))

                        for y in op_table:

                            if (y == reg3):

                                value2 = op_table[y]

                                value2 = binaryToDecimal(int(value2))



                        reg_or = value1 | value2

                        reg_or = get_binary(reg_or, 16)



                        registers[reg1] = reg_or



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "xor"):

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        for x in op_table:

                            if (x == reg2):

                                value1 = op_table[x]

                                value1 = binaryToDecimal(int(value1))

                        for y in op_table:

                            if (y == reg3):

                                value2 = op_table[y]

                                value2 = binaryToDecimal(int(value2))



                        reg_xor = value1 ^ value2

                        reg_xor = get_binary(reg_xor, 16)



                        registers[reg1] = reg_xor



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "and"):

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        for x in op_table:

                            if (x == reg2):

                                value1 = op_table[x]

                                value1 = binaryToDecimal(int(value1))

                        for y in op_table:

                            if (y == reg3):

                                value2 = op_table[y]

                                value2 = binaryToDecimal(int(value2))



                        reg_and = value1 & value2

                        reg_and = get_binary(reg_and, 16)



                        registers[reg1] = reg_and



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                elif (type == "B"):

                    op_code = program[i][:5]

                    op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])



                    if (instruction == "movi"):

                        reg = program[i][5:8]

                        number = program[i][8:]



                        number ="0" + change_bit(number)

                        if len(number) != 16:

                            x = 16 - len(number)

                            number = x*"0" + number

                        for x in op_table:

                            if (x == reg):

                                registers[x] = number

                                registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))





                    elif (instruction == "ls"):

                        reg = program[i][5:8]

                        number = program[i][8:]

                        number = binaryToDecimal(int(number))



                        # no_of_times = 0

                        # while (number != 1):

                        #     number = int(number/2)

                        #     no_of_times += 1



                        no_of_times = number



                        for x in op_table:

                            if (x == reg):

                                value = registers[x]

                                value = binaryToDecimal(int(value))

                                value = value << no_of_times

                                value = get_binary(value, 16)



                        for y in registers:

                            if (y == reg):

                                registers[y] = value



                                registers[FLAGS] = "0000000000000000"

                                print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))





                    elif (instruction == "rs"):

                        reg = program[i][5:8]

                        number = program[i][8:]

                        number = binaryToDecimal(int(number))



                        no_of_times = number

                        for x in op_table:

                            if (x == reg):

                                value = registers[x]

                                value = binaryToDecimal(int(value))

                                value = value >> no_of_times

                                value = get_binary(value, 16)



                        for y in registers:

                            if (y == reg):

                                registers[y] = value



                                registers[FLAGS] = "0000000000000000"

                                print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))





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

                                        print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))



                    elif (instruction == "div"):

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        reg1 = program[i][10:13]

                        reg2 = program[i][13:16]



                        for x in op_table:

                            if (x == reg1):

                                value1 = op_table[x]

                                value1 = int(value1)

                                value1 = binaryToDecimal(int(value1))

                        for y in op_table:

                            if (y == reg2):

                                value2 = op_table[y]

                                value2 = int(value2)

                                value2 = binaryToDecimal(value2)



                        if (value2 == 0):

                            remainder = 0

                            quotient = 0

                        else:    

                            remainder = value1%value2

                            value1 = value1 - remainder

                            quotient = int(value1/value2)



                        remainder = get_binary(remainder, 16)

                        quotient = get_binary(quotient, 16)



                        registers[R0] = quotient

                        registers[R1] = remainder



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "not"):

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])



                        reg1 = program[i][10:13]

                        reg2 = program[i][13:16]

                        for y in op_table:

                            if (y == reg2):

                                value2 = op_table[y]

                                value2 = binaryToDecimal(int(value2))



                                reg_help = ~value2

                                reg_help = get_binary(reg_help, 16)

                                for x in registers:

                                    if (x == reg1):

                                        registers[x] = reg_help



                                        registers[FLAGS] = "0000000000000000"

                                        print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))



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



                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))





                elif (type == "D"):

                    if (instruction == "st"):

                        reg = program[i][5:8]

                        op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                        for x in op_table:

                            if (x == reg):

                                dict[program[i][8:]] = op_table[x]



                                registers[FLAGS] = "0000000000000000"

                                print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))



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

                                else:



                                    registers[FLAGS] = "0000000000000000"



                        print(get_binary(i, 8), str(registers[R0]).replace('\n', ""), str(registers[R1]).replace('\n', ""), str(registers[R2]).replace('\n', ""), str(registers[R3]).replace('\n', ""), str(registers[R4]).replace('\n', ""), str(registers[R5]).replace('\n', ""), str(registers[R6]).replace('\n', ""), str(registers[FLAGS]).replace('\n', ""))





                elif (type == "E"):

                    op_table = opcode_table2.asd(registers[R0], registers[R1], registers[R2], registers[R3], registers[R4], registers[R5], registers[R6], registers[FLAGS])

                    if (instruction == "jmp"):

                        use = program[i][8:]

                        use = int(use)

                        use = binaryToDecimal(use)



                        jump[i] = use

                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "jlt"):

                        if (registers[FLAGS] == "0000000000000100"):

                            use = program[i][8:]

                            use = int(use)

                            use = binaryToDecimal(use)

                            jump[i] = use

                        else:

                            use = 0



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "jgt"):

                        if (registers[FLAGS] == "0000000000000010"):

                            use = program[i][8:]

                            use = int(use)

                            use = binaryToDecimal(use)

                            jump[i] = use

                        else:

                            use = 0



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



                    elif (instruction == "je"):

                        if (registers[FLAGS] == "0000000000000001"):

                            use = program[i][8:]

                            use = int(use)

                            use = binaryToDecimal(use)

                            jump[i] = use

                        else:

                            use = 0



                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))





                elif (type == "F"):

                    if (instruction == "hlt"):

                        registers[FLAGS] = "0000000000000000"

                        print(get_binary(i, 8),str(registers[R0]).replace('\n',""),str(registers[R1]).replace('\n',""),str(registers[R2]).replace('\n',""),str(registers[R3]).replace('\n',""),str(registers[R4]).replace('\n',""),str(registers[R5]).replace('\n',""),str(registers[R6]).replace('\n',""),str(registers[FLAGS]).replace('\n',""))



    for i in program:

        print(i)



    for k in dict:

        num = dict[k]

        num = change_bit(num)

        print(num)

    remaining = 256 - len(program) - len(dict)



    for v in range(remaining):

        print("0000000000000000")



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

    return





if __name__ == '__main__':

    main()
