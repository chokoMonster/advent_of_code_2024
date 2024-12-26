def turn(current_dir):
    match current_dir:
        case "U":
            return "R"
        case "R":
            return "D"
        case "D":
            return "L"
        case "L":
            return "U"

def get_rock(p, g, d):
    match d:
        case "U":
            return g[p[1] - 1][p[0]] == "#"
        case "R":
            return g[p[1]][p[0] + 1] == "#"
        case "D":
            return g[p[1] + 1][p[0]] == "#"
        case "L":
            return g[p[1]][p[0] - 1] == "#"

def step(p, d):
    match d:
        case "U":
            return (p[0], p[1] - 1)
        case "R":
            return (p[0] + 1, p[1])
        case "D":
            return (p[0], p[1] + 1)
        case "L":
            return (p[0] - 1, p[1])

def check_obstacle(p, rp, d, g):
    my_steps = set()

    while True:
        if p[0] == 0 or p[1] == 0 or p[0] == len(g[0]) - 1 or p[1] == len(g) - 1:
            return False

        key = (p[0], p[1], d)
        if key in my_steps:
            return True
        my_steps.add(key)

        np = step(p, d)
        if get_rock(p, g, d) or np == rp:
            d = turn(d)
        else:
            p = np


if __name__ == "__main__":

    f = open("input/06.txt", "r")
    lines = f.readlines()
    grid = [l.strip() for l in lines]

    start_pos = (0, 0)
    start_direction = 'X'
    for row, line in enumerate(lines):
        for col, l in enumerate(line):
            if l == "^":
                start_pos = (col, row)
                start_direction = 'U'

    pos = start_pos
    direction = start_direction

    visited = [pos]
    obstacles = set()
    obs = 0
    while True:
        #if (pos[1] == 0 and direction == "U") or (pos[1] == len(grid) - 1 and direction == "D") or (
        #        pos[0] == 0 and direction == "L") or (pos[0] == len(grid[0]) - 1 and direction == "R"):
        if pos[1] == 0 or pos[0] == 0 or pos[0] == len(grid[0]) - 1 or pos[1] == len(grid) - 1:
            break

        if not get_rock(pos, grid, direction):
            rock_pos = step(pos, direction)
            if rock_pos != start_pos and rock_pos not in obstacles:
                if check_obstacle(start_pos, rock_pos, start_direction, grid):
                    obstacles.add(rock_pos)
                    #print("--", pos, direction, rock_pos)

        if get_rock(pos, grid, direction):
            direction = turn(direction)
        else:
            pos = step(pos, direction)
            visited.append(pos)

    v = list(dict.fromkeys(visited))
    print(len(v))
    # 5086

    print(len(obstacles))
    # 1770


    """
    pos = (0, 0)
    direction = 'U'
    for row, line in enumerate(lines):
        for col, l in enumerate(line):
            if l == "^":
                pos = (col, row)

    visited = []
    visited.append(pos)
    running  = True
    while running:
        if (pos[1] == 0 and direction == "U") or (pos[1] == len(grid)-1 and direction == "D") or (pos[0] == 0 and direction == "L") or (pos[0] == len(grid[0])-1 and direction == "R"):
            running == False
            break

        if get_rock(pos, grid, direction):
            direction = turn(direction)
        else:
            pos = step(pos, direction)
            visited.append(pos)

        print(pos)

    v = list(dict.fromkeys(visited))
    print(len(v))
    """