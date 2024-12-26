def step(p, d):
    match d:
        case "^":
            return (p[0], p[1] - 1)
        case ">":
            return (p[0] + 1, p[1])
        case "v":
            return (p[0], p[1] + 1)
        case "<":
            return (p[0] - 1, p[1])

def move(op, np, g, d):
    match d:
        case "^":
            for py in range(np[1], op[1]):
                g[py][op[0]] = g[py+1][op[0]]
        case ">":
            for px in reversed(range(op[0]+1, np[0]+1)):
                g[op[1]][px] = g[op[1]][px-1]
        case "v":
            for py in reversed(range(op[1]+1, np[1]+1)):
                g[py][op[0]] = g[py-1][op[0]]
        case "<":
            for px in range(np[0], op[0]):
                g[op[1]][px] = g[op[1]][px+1]

    g[op[1]][op[0]] = '.'

"""
def can_move(p, g, d):
    new_pos = p
    while True:
        new_pos = step(new_pos, d)
        match g[new_pos[1]][new_pos[0]]:
            case '.':
                return new_pos
            case '#':
                return (-1, -1)
            case 'O':
                continue
"""


def move_vertical(p, g, d):
    new_grid = [r[:] for r in g]
    move_x = [p[0]]

    steps = 0
    while True:
        if len(move_x) == 0:
            break

        move_x_new = []
        for mx in move_x:
            op = (mx, p[1]+steps)
            np = step(op, d)
            if g[np[1]][np[0]] == '[':
                move_x_new.append(mx)
                if mx+1 not in move_x:
                    move_x_new.append(mx+1)
                    new_grid[np[1]][mx+1] = '.'
            if g[np[1]][np[0]] == ']' :
                move_x_new.append(mx)
                if mx-1 not in move_x:
                    move_x_new.append(mx-1)
                    new_grid[np[1]][mx-1] = '.'
            new_grid[np[1]][np[0]] = g[op[1]][op[0]]

        move_x = move_x_new #list(set(move_x_new))
        if d == '^':
            steps -= 1
        else:
            steps += 1

    #g = new_grid
    #g[p[1]][p[0]] = '.'
    #new_grid[p[1]][p[0]] = '.'
    return new_grid


def can_move(p, g, d):
    new_pos = p
    while True:
        new_pos = step(new_pos, d)
        match g[new_pos[1]][new_pos[0]]:
            case '.':
                return new_pos
            case '#':
                return False
            case '[':
                if d in ['^', 'v']:
                    if not can_move((new_pos[0]+1, new_pos[1]), g, d):
                        return False
            case ']':
                if d in ['^', 'v']:
                    if not can_move((new_pos[0]-1, new_pos[1]), g, d):
                        return False


if __name__ == "__main__":

    f2 = open("input/15_2.txt", "r")
    move_list = f2.readlines()
    move_list = [m.strip() for m in move_list]
    moves = ''.join(move_list)

    f = open("input/15.txt", "r")
    lines = f.readlines()
    lines = [list(l.strip()) for l in lines]
    #grid = lines

    grid = []
    for line in lines:
        row = []
        for l in line:
            match l:
                case '.':
                    row.append('.')
                    row.append('.')
                case '#':
                    row.append('#')
                    row.append('#')
                case 'O':
                    row.append('[')
                    row.append(']')
                case '@':
                    row.append('@')
                    row.append('.')
        grid.append(row)

    for g in grid:
        print(''.join(g))

    robot_pos = (0, 0)
    for j, row in enumerate(grid):
        for i, p in enumerate(row):
            if p == '@':
                robot_pos = (i, j)
                grid[j][i] = '.'

    for m in moves:
        ziel_pos = can_move(robot_pos, grid, m)
        if not ziel_pos:
            continue
        if m in ['^', 'v']:
            grid = move_vertical(robot_pos, grid, m)
        else:
            move(robot_pos, ziel_pos, grid, m)
        robot_pos = step(robot_pos, m)

        #print(robot_pos, m)
        #for row in grid:
        #    print(''.join(row))

    res = 0
    for j, row in enumerate(grid):
        print(''.join(row))
        for i, x in enumerate(row):
            if x == '[':
                res += 100 * j + i

    print(res)

    """
    robot_pos = (0, 0)
    for j, row in enumerate(grid):
        for i, p in enumerate(row):
            if p == '@':
                robot_pos = (i, j)
                grid[j][i] = '.'

    for m in moves:
        ziel_pos = can_move(robot_pos, grid, m)
        if ziel_pos[0] == -1:
            continue
        move(robot_pos, ziel_pos, grid, m)
        robot_pos = step(robot_pos, m)

    res = 0
    for j, row in enumerate(grid):
        print(''.join(row))
        for i, x in enumerate(row):
            if x == 'O':
                res += 100 * j + i

    print(res)
    """


