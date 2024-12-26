import itertools

ALL_POS = {'A': (2, 3), '0': (1, 3), '1': (0, 2), '2': (1, 2), '3': (2, 2), '4': (0, 1), '5': (1, 1), '6': (2, 1), '7': (0, 0), '8': (1, 0), '9': (2, 0)}
DIR_POS = {'A': (2, 0), '^': (1, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}

"""
   ^  A
<  v  >
"""

STORE = {}
def get_directional_seq_recursive(s, r, robs):
    #print('s', s, r)
    steps = 0
    pos = (2, 0)
    p = 'A'
    for val in s:
        new_pos = DIR_POS[val]

        if pos == new_pos:
            steps += 1
            continue

        store_key = (p, val, r)
        #store_key = (pos, new_pos, r)
        if store_key in STORE:
            steps += STORE[store_key]
            #print('loaded', store_key, ':', STORE[store_key])
            pos = new_pos
            p = val
            continue

        #print('find', store_key)

        seq_list = []
        #if pos == new_pos:
        #    seq_list.append('A')
        if pos[0] == 0:  # < alt
            start_seq = ['>']
            end_seq = ['']
            if new_pos[0] == 2 or new_pos[1] == 0:
                end_seq = get_num_path((1, 1), new_pos)
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        elif new_pos[0] == 0: # < neu
            start_seq = ['']
            end_seq = ['<']
            if pos[0] == 2 or pos[1] == 0:
                start_seq = get_num_path(pos, (1, 1))
            for st in start_seq:
                for es in end_seq:
                    seq_list.append(st + es + 'A')
        # all other combinations
        else:
            for p in get_num_path(pos, new_pos):
                seq_list.append(p + 'A')

        min_steps = -1
        for r_neu in seq_list: # all possibilities getting from POS to NEW_POS --> find shortest
            next_steps = len(r_neu)
            #if r == 2:
            #    print('robo 2', p, val, r_neu, len(r_neu))
            if r < robs:
                next_steps = get_directional_seq_recursive(r_neu, r+1, robs)
            if min_steps < 0 or min_steps > next_steps:
                min_steps = next_steps
        STORE[store_key] = min_steps
        steps += min_steps

        pos = new_pos
        p = val

    #print('steps', steps)
    return steps

"""
(A)1
(A)^<<A        (A)<^<A
(A)<Av<AA>>^A  (A)v<<A>^Av<A>>^A
"""

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

    #all_robots = 2 # PART 1
    all_robots = 25 # PART 2

    res = 0
    for line in lines:
        print('seq:', line)
        dir_seq_lengths = []
        num_sequences = get_numeric_sequence(line)
        #print('num_seq', num_sequences)
        for num_sequence in num_sequences:
            dir_seq_lengths.append(get_directional_seq_recursive(num_sequence, 1, all_robots))
        #print('dir_seq_len', dir_seq_lengths)

        #print(STORE)

        shortest_seq = dir_seq_lengths[0]
        for l in dir_seq_lengths:
            if l < shortest_seq:
                shortest_seq = l

        num_code = line[:3]
        print(shortest_seq)
        res += shortest_seq * int(num_code)


    print('res', res)
    # 171596
    # 209268004868246
