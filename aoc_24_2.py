import copy

# zwischenergebnisse speichern: xy_xor, xy_and, c_and, c_new, z (aktuelles z)
changes = [('z', 'xy_xor'), ('z', 'xy_and'), ('z', 'c_and'), ('z', 'c_new'), ('xy_xor', 'xy_and'), ('xy_xor', 'c_and'), ('xy_xor', 'c_new'), ('xy_and', 'c_and'), ('xy_and', 'c_new'), ('c_and', 'c_new')]

def check_part_adder(i, c_in, gate_dict, changed = False):
    variables = {'xy_xor': None, 'xy_and': None, 'c_and': None, 'c_new': None, 'z': None}
    x = 'x' + i
    y = 'y' + i
    z = 'z' + i
    variables['z'] = 'z' + i
    variables['xy_xor'] = gate_dict[(x, 'XOR', y)]
    variables['xy_and'] = gate_dict[(x, 'AND', y)]
    error_detected = False

    z_key = (variables['xy_xor'], 'XOR', c_in)
    # z finden
    if z_key in gate_dict:
        variables['z'] = gate_dict[z_key]
    else: error_detected = True

    c_and_key = (variables['xy_xor'], 'AND', c_in)
    # c_and finden
    if c_and_key in gate_dict:
        variables['c_and'] = gate_dict[c_and_key]
    else:
        error_detected = True

    c_new_key = (variables['xy_and'], 'OR', variables['c_and'])
    if c_new_key in gate_dict:
        variables['c_new'] = gate_dict[c_new_key]
    else:
        error_detected = True

    if variables['z'] != z:
        error_detected = True

    if not error_detected:
        return gate_dict[c_new_key], gate_dict
    elif changed:
        return None, None
    else:
        # there is a problem in the gate --> change wires and check again!
        for c in changes:
            new_gates = copy.deepcopy(gate_dict)
            for (k, v) in new_gates.items():
                if v == variables[c[0]]:
                    new_gates[k] = variables[c[1]]
                elif v == variables[c[1]]:
                    new_gates[k] = variables[c[0]]
            (ret1, ret2) = check_part_adder(i, c_in, new_gates, True)
            if ret1 is not None:
                print('changed', variables[c[0]], variables[c[1]])
                return ret1, ret2

if __name__ == "__main__":
    f1 = open("input/24_1.txt", "r")
    f2 = open("input/24_2.txt", "r")
    values = f1.readlines()
    gate_lines = f2.readlines()
    gate_lines = [line.strip() for line in gate_lines]

    """
    gate_values = {}
    x = ''
    y = ''
    for v in values:
        val = v.split(': ')
        gate_values_init[val[0]] = int(val[1])
        if val[0].startswith('x'):
            x += val[1]
        else:
            y += val[1]
    z = int(x, base=2) + int(y, base=2)
    z_str = str(bin(z))[2:]
    z_reversed = z_str[::-1]
    print('x:', x, 'y:', y, 'z:', z_str, z_reversed)
    """

    gates = {}
    #print('digraph {')
    for g in gate_lines:
        gate = g.split(' -> ')
        in_gates = gate[0].split(' ')
        gates[(in_gates[0], in_gates[1], in_gates[2])] = gate[1]
        gates[(in_gates[2], in_gates[1], in_gates[0])] = gate[1]
        #print(in_gates[0], '->', gate[1], '[label=', in_gates[1], ']')
        #print(in_gates[2], '->', gate[1], '[label=', in_gates[1], ']')
    #print('}')

    # ONLY CHECK GATE!!
    # get first carry bit
    c_in = z_key = gates[('x00', 'AND', 'y00')]

    for i in range(1, int(len(values) / 2)):
        i_str = str(i)
        if i < 10:
            i_str = '0' + i_str
        (c_in, gates) = check_part_adder(i_str, c_in, gates)


"""
qff <-> qnw (Nähe z11)
pbv <-> z16
qqp <-> z23
fbq <-> z36

--> fbq,pbv,qff,qnw,qqp,z16,z23,z36
"""