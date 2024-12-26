import itertools

ALL_POS = {'A': (2, 3), '0': (1, 3), '1': (0, 2), '2': (1, 2), '3': (2, 2), '4': (0, 1), '5': (1, 1), '6': (2, 1), '7': (0, 0), '8': (1, 0), '9': (2, 0)}
DIR_POS = {'A': (2, 0), '^': (1, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}


def get_directional_sequence(s):
    pos = (2, 0)
    res_seq_list = ['']
    for val in s:
        new_pos = DIR_POS[val]
        seq_list = []

        if pos == new_pos:
            seq_list.append('A')
        elif pos[0] == 0:  # < alt
            start_seq = ['>']
            end_seq = ['']
            #res_seq += start_seq[0]
            if new_pos[0] == 2 or new_pos[1] == 0:
                end_seq = get_num_path((1, 1), new_pos)
            #res_seq += end_seq[0]
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        elif new_pos[0] == 0: # < neu
            start_seq = ['']
            end_seq = ['<']
            if pos[0] == 2 or pos[1] == 0:
                start_seq = get_num_path(pos, (1, 1))
            #res_seq += start_seq[0]
            #res_seq += end_seq[0]
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        # all other combinations
        else:
            #res_seq += get_num_path(pos, new_pos)[0]
            for p in get_num_path(pos, new_pos):
                seq_list.append(p + 'A')

        res_seq_list_new = []
        for r in res_seq_list:
            for r_neu in seq_list:
                res_seq_list_new.append(r + r_neu)

        res_seq_list = res_seq_list_new

        #res_seq += 'A'
        pos = new_pos

    return res_seq_list

def get_num_path(p1, p2):
    possibilities = []
    dif_x = p2[0] - p1[0]
    dif_y = p2[1] - p1[1]
    abs_dif_x = abs(dif_x)
    abs_dif_y = abs(dif_y)

    lst = [list(i) for i in itertools.product([0, 1], repeat = abs_dif_x + abs_dif_y)]
    lst = list(filter(lambda x: x.count(0) == abs_dif_x, lst))
    for l in lst:
        pos_seq = ''
        for s in l:
            if s == 0 and dif_x > 0:
                pos_seq += '>'
            elif s == 0 and dif_x < 0:
                pos_seq += '<'
            elif s == 1 and dif_y > 0:
                pos_seq += 'v'
            elif s == 1 and dif_y < 0:
                pos_seq += '^'
        possibilities.append(pos_seq)

    return possibilities

def get_numeric_sequence(s):
    pos = (2, 3)
    res_seq_list = ['']
    for val in s:
        new_pos = ALL_POS[val]
        seq_list = []

        if pos == new_pos:
            seq_list.append('A')
        # A + 0
        elif pos[1] == 3 and new_pos[1] == 3:
            if pos[0] == 2: # A --> 0
                seq_list.append('<A')
            else: # 0 --> A
                seq_list.append('>A')
        # A = alt
        elif pos[1] == 3 and pos[0] == 2 and new_pos[0] == 0:
            start_seq = ['<^', '^<']
            end_seq = get_num_path((1, 2), new_pos)
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
            if new_pos[1] < 2:
                start_seq = ['^^']
                end_seq = get_num_path((2, 1), new_pos)
                for st in start_seq:
                    for es in end_seq:
                        seq_list.append(st + es + 'A')
        # A = neu
        elif new_pos[1] == 3 and new_pos[0] == 2 and pos[0] == 0:
            start_seq = get_num_path(pos, (1, 2))
            end_seq = ['>v', 'v>']
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
            if pos[1] < 2:
                start_seq = get_num_path(pos, (2, 1))
                end_seq = ['vv']
                for st in start_seq:
                    for es in end_seq:
                        seq_list.append(st + es + 'A')
        elif pos[1] == 3 and pos[0] == 1 and new_pos[0] == 0: # 0 alt
            start_seq = ['^']
            end_seq = ['']
            if new_pos[1] < 2:
                end_seq = get_num_path((1, 2), new_pos)
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        elif new_pos[1] == 3 and new_pos[0] == 1 and pos[0] == 0: # 0 neu
            start_seq = ['']
            end_seq = ['v']
            if pos[1] < 2:
                start_seq = get_num_path(pos, (1, 2))
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        # all other combinations
        else:
            for p in get_num_path(pos, new_pos):
                seq_list.append(p + 'A')

        res_seq_list_new = []
        for r in res_seq_list:
            for r_neu in seq_list:
                res_seq_list_new.append(r + r_neu)

        res_seq_list = res_seq_list_new
        pos = new_pos

    return res_seq_list

if __name__ == "__main__":
    f = open("input/21.txt", "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    res = 0
    for line in lines:
        print('seq:', line)
        dir_seq1 = []
        dir_seq2 = []
        num_sequences = get_numeric_sequence(line)
        #print('num_seq', num_sequences)
        for num_sequence in num_sequences:
            dir_seq1 += get_directional_sequence(num_sequence)
        #print('dir_seq1', dir_seq1)
        for ds1 in dir_seq1:
            dir_seq2 += get_directional_sequence(ds1)
        #print('dir_seq2', dir_seq2)
        shortest_seq = len(dir_seq2[0])
        for ds2 in dir_seq2:
            if len(ds2) < shortest_seq:
                #print(ds2)
                shortest_seq = len(ds2)

        num_code = line[:3]
        print(num_code, shortest_seq, shortest_seq * int(num_code))
        res += shortest_seq * int(num_code)

    print('res1', res) # 171596
