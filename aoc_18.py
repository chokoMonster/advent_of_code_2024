def step(p, d):
    (x, y) = p
    match d:
        case "U":
            return x, y - 1
        case "R":
            return x + 1, y
        case "D":
            return x, y + 1
        case "L":
            return x - 1, y

def get_byte(p, g, d):
    match d:
        case "U":
            return g[p[1] - 1][p[0]] == "#"
        case "R":
            return g[p[1]][p[0] + 1] == "#"
        case "D":
            return g[p[1] + 1][p[0]] == "#"
        case "L":
            return g[p[1]][p[0] - 1] == "#"

def get_boundaries(p, d, w):
    match d:
        case "U":
            return p[1] == 0
        case "R":
            return p[0] == w-1
        case "D":
            return p[1] == w-1
        case "L":
            return p[0] == 0



if __name__ == "__main__":

    f = open("input/18.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    directions = ['U', 'R', 'D', 'L']

    width = 71
    #width = 7

    stop_0 = 1024
    #stop_0 = 12

    found_loop = False

    for s in range(stop_0+1, len(lines)):
        if found_loop:
            break

        stop = s

        grid = [['.' for i in range(width)] for j in range(width)]
        for l, line in enumerate(lines):
            if l >= stop:
                break
            (i, j) = line.split(',')
            grid[int(j)][int(i)] = '#'

        start_pos = (0, 0)
        visited = [start_pos]
        pos_list = [start_pos]

        finished = False
        steps = 0
        while not finished:
            if len(pos_list) == 0:
                found_loop = True
                print('endless loop:', stop-1, lines[stop-1])
                break

            steps += 1
            pos_list_new = []

            for pos in pos_list:
                if pos[0] == width - 1 and pos[1] == width - 1:
                    print('finished:', steps)
                    finished = True
                    break

                for direction in directions:
                    if get_boundaries(pos, direction, width):
                        continue

                    if get_byte(pos, grid, direction):
                        continue

                    new_pos = step(pos, direction)
                    if new_pos not in visited:
                        pos_list_new.append(new_pos)
                        visited.append(new_pos)

            pos_list = pos_list_new

        print(steps - 1)

    """
    stop = 1024
    stop = 12
    
    grid = [['.' for i in range(width)] for j in range(width)]

    for l, line in enumerate(lines):
        if l >= stop:
            break
        (i, j) = line.split(',')
        grid[int(j)][int(i)] = '#'

    for g in grid:
        print(g)

    start_pos = (0, 0)
    visited = [start_pos]
    pos_list = [start_pos]

    ziel = False
    steps = 0
    while not ziel:
        if len(pos_list) == 0:
            print(stop)
            print('endless loop')
        steps += 1
        pos_list_new = []

        for pos in pos_list:
            if pos[0] == width-1 and pos[1] == width-1:
                print('ZIEL', steps)
                ziel = True
                break

            for direction in directions:
                if get_boundaries(pos, direction, width):
                    continue

                if get_byte(pos, grid, direction):
                    continue

                new_pos = step(pos, direction)
                if new_pos not in visited:
                    pos_list_new.append(new_pos)
                    visited.append(new_pos)


        pos_list = pos_list_new

    print(steps-1)
    """
