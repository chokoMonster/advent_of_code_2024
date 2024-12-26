import math

def get_combo_op(o, r):
    if o < 4:
        return o
    return r[o%4]


if __name__ == "__main__":

    program = '2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0'
    #A = 60589763

    # test
    #program = '0,3,5,4,3,0'
    #A = 729
    #B = 0
    #C = 0

    instructions = program.split(',')
    instructions = [int(i) for i in instructions]

    part2_match = 0

    i = 0
    while True:
        i += 1

        """ thoughts ...
        B = A % 8
        B = B XOR 0101 (5)
        C = trunc(A / 2^B) --> vorderer Teil abhängig, aber letzte Zahl bleibt stabil!! --> jeweils letzte Zahl Bruteforcen?
        B = B XOR 0110 (6)
        B = B XOR C
        out: B % 8
        A = trunc(A / 2^3) --> A / 8 --> letzte Ziffer faellt weg im Oktalsystem!!
        jump 0
        
        --> Octal system??!
        """

        #2415751641550330
        #A = i * 8 + 0o330551461575142

        # oki lets go brute force digits..
        A = i
        A = i * 8**5 + 0o24632
        A = i * 8**7 + 0o4424632
        A = i * 8**9 + 0o334424632
        A = i * 8**11 + 0o46334424632

        #0,3,5,4,3,0
        #A = i * 8

        registers = [A, 0, 0]
        outputs = []
        instruction_pointer = 0


        while instruction_pointer < len(instructions)-1:
            operator = instructions[instruction_pointer]
            operand = instructions[instruction_pointer+1]

            match operator:
                case 0: # division
                    registers[0] = math.trunc(registers[0] / pow(2, get_combo_op(operand, registers)))
                case 1: # bitwise XOR
                    registers[1] = registers[1] ^ operand
                case 2: # combo % 8
                    registers[1] = get_combo_op(operand, registers) % 8
                case 3: # jump
                    if registers[0] != 0:
                        instruction_pointer = operand - 2
                case 4: # bitwise XOR
                    registers[1] = registers[1] ^ registers[2]
                case 5: # combo % 8
                    outputs.append(get_combo_op(operand, registers) % 8)
                    if outputs[len(outputs)-1] != instructions[len(outputs)-1]:
                        if len(outputs) > part2_match:
                            part2_match = len(outputs)
                            print(oct(A))
                        break
                case 6: # division
                    registers[1] = math.trunc(registers[0] / pow(2, get_combo_op(operand, registers)))
                case 7: # division
                    registers[2] = math.trunc(registers[0] / pow(2, get_combo_op(operand, registers)))

            instruction_pointer += 2

        if outputs == instructions:
            print('A', A, oct(A))
            break

    #print(outputs)
    #print(','.join([str(o) for o in outputs]))