
if __name__ == "__main__":
    TEST_MODE = False
    if not TEST_MODE:
        f1 = open("input/24_1.txt", "r")
        f2 = open("input/24_2.txt", "r")
    else:
        f1 = open("input/24_1_test.txt", "r")
        f2 = open("input/24_2_test.txt", "r")
    lines = f1.readlines()
    values = [line.strip() for line in lines]
    gate_lines = f2.readlines()
    gate_lines = [line.strip() for line in gate_lines]

    gate_values = {}
    gates = []

    for v in values:
        val = v.split(': ')
        gate_values[val[0]] = int(val[1])
    for g in gate_lines:
        #x00 AND y00 -> z00
        gate = g.split(' -> ')
        gates.append((gate[1], gate[0].split(' ')))
    print(gates)

    while len(gates) > 0:
        i = 0
        while i < len(gates):
            g = gates[i]

            in1 = g[1][0]
            in2 = g[1][2]
            if in1 in gate_values and in2 in gate_values:
                in_val1 = gate_values[in1]
                in_val2 = gate_values[in2]
                op = g[1][1]
                gate_val = 0
                gate_res = 0
                if op == 'AND':
                    gate_res = in_val1 == 1 and in_val2 == 1
                elif op == 'OR':
                    gate_res = in_val1 == 1 or in_val2 == 1
                elif op == 'XOR':
                    gate_res = in_val1 != in_val2
                if gate_res:
                    gate_val = 1
                gate_values[g[0]] = gate_val
                del gates[i]
                i -= 1

            i += 1

    print(gate_values)
    z_gates = {k: v for k, v in gate_values.items() if k.startswith('z')}
    z_gates = dict(sorted(z_gates.items(), reverse=True))
    print(z_gates)
    out = ''
    for v in z_gates.values():
        out += str(v)
    bin_out = int(out, base=2)
    print(bin_out)
