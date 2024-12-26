def get_next_pos(p):
    global grid

    next_steps = []
    if p[0] > 0 and grid[p[0]-1][p[1]]:
        next_steps.append((p[0]-1, p[1]))
    if p[1] > 0 and grid[p[0]][p[1]-1]:
        next_steps.append((p[0], p[1]-1))
    if p[0] < len(grid)-1 and grid[p[0]+1][p[1]]:
        next_steps.append((p[0]+1, p[1]))
    if p[1] < len(grid[0])-1 and grid[p[0]][p[1]+1]:
        next_steps.append((p[0], p[1]+1))

    return next_steps


def get_increasing_pos(p):
    global grid

    next_steps = []
    v = grid[p[0]][p[1]]
    for new_p in get_next_pos(p):
        if grid[new_p[0]][new_p[1]] == (v+1):
            next_steps.append(new_p)

    return next_steps


def get_next_level(p, l):
    l += 1
    if l == 10:
        return [p]

    all_pos = []
    my_steps = set()
    next_steps = get_increasing_pos((p[0], p[1]))
    for ns in next_steps:
        if ns in my_steps:
            continue
        my_steps.add(ns)
        if l < 10:
            all_pos += get_next_level(ns, l)
    return all_pos


def get_next_level2(p, l):
    l += 1
    if l == 10:
        return [[p]]

    all_pos = []
    next_steps = get_increasing_pos((p[0], p[1]))
    for ns in next_steps:
        if l < 10:
            next_pos = get_next_level2(ns, l)
            if len(next_pos) == 0:
                continue
            for np in next_pos:
                if type(np) is tuple:
                    np = [np]
                part_list = [ns] + np
                all_pos.append(part_list)
    return all_pos


if __name__ == "__main__":
    global grid

    f = open("input/10.txt", "r")
    grid = [list(l.strip()) for l in f.readlines()]

    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos == '.':
                grid[y][x] = '-1'
    grid = [[int(p) for p in row] for row in grid]

    print(grid)

    res = 0
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos == 0:
                pos_9 = get_next_level2((y, x), 0)
                print(pos_9)
                res += len(pos_9)
                #pos_9_unique = list(dict.fromkeys(pos_9))
                #res += len(pos_9_unique)

    print(res)
