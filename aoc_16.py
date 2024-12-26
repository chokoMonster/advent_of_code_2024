
def turn_right(current_dir):
    match current_dir:
        case "U":
            return "R"
        case "R":
            return "D"
        case "D":
            return "L"
        case "L":
            return "U"

def turn_left(current_dir):
    match current_dir:
        case "U":
            return "L"
        case "R":
            return "U"
        case "D":
            return "R"
        case "L":
            return "D"

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

def get_wall(p, g, d):
    match d:
        case "U":
            return g[p[1] - 1][p[0]] == "#"
        case "R":
            return g[p[1]][p[0] + 1] == "#"
        case "D":
            return g[p[1] + 1][p[0]] == "#"
        case "L":
            return g[p[1]][p[0] - 1] == "#"


if __name__ == "__main__":
    global overall_sum

    f = open("input/16.txt", "r")
    lines = f.readlines()
    grid = [list(l.strip()) for l in lines]

    start_direction = 'R'
    start_pos = (0, 0)

    for j, row in enumerate(grid):
        print(''.join(row))
        for i, x in enumerate(row):
            if x == 'S':
                start_pos = (i, j)

    start_key = (start_pos[0], start_pos[1], start_direction)
    visited = {start_key: 0}
    #paths = {start_key: 0} PART1
    paths = {start_key: [0, {start_pos}]} # PART2

    end_score = -1
    best_paths = []

    while len(paths) > 0:
        new_paths = {}
        for k in paths.keys():
            pos = (k[0], k[1])
            if 0 < end_score < paths[k][0]:
                continue

            if grid[pos[1]][pos[0]] == 'E':
                if end_score > paths[k][0]:
                    best_paths = []
                best_paths.append(paths[k][1])
                end_score = paths[k][0]
                continue

            direction = k[2]
            current_path = paths[k][1]

            if not get_wall(pos, grid, direction):
                new_pos = step(pos, direction)
                new_val = paths[k][0] + 1
                new_key = (new_pos[0], new_pos[1], direction)
                if (not ((new_key in paths and new_val > paths[new_key][0])
                        or (new_key in new_paths and new_val > new_paths[new_key][0]))
                    and not (new_key in visited and visited[new_key] < new_val)):
                    new_cur_path = current_path.union({new_pos})
                    if new_key in new_paths and new_paths[new_key][0] == new_val:
                        new_paths[new_key][1] = new_paths[new_key][1].union(new_cur_path)
                    else:
                        new_paths[new_key] = [new_val, new_cur_path]
                    visited[new_key] = new_val

            new_val = paths[k][0] + 1000

            new_dir_r = turn_right(direction)
            new_key = (pos[0], pos[1], new_dir_r)
            if (not ((new_key in paths and new_val > paths[new_key][0])
                    or (new_key in new_paths and new_val > new_paths[new_key][0]))
                and not (new_key in visited and visited[new_key] < new_val)):
                if new_key in new_paths and new_paths[new_key][0] == new_val:
                    new_paths[new_key][1] = new_paths[new_key][1].union(current_path)
                else:
                    new_paths[new_key] = [new_val, current_path]
                visited[new_key] = new_val

            new_dir_l = turn_left(direction)
            new_key = (pos[0], pos[1], new_dir_l)
            if (not ((new_key in paths and new_val > paths[new_key][0])
                    or (new_key in new_paths and new_val > new_paths[new_key][0]))
                and not (new_key in visited and visited[new_key] < new_val)):
                if new_key in new_paths and new_paths[new_key][0] == new_val:
                    new_paths[new_key][1] = new_paths[new_key][1].union(current_path)
                else:
                    new_paths[new_key] = [new_val, current_path]
                visited[new_key] = new_val

        paths = new_paths

    best_tiles = [y for x in best_paths for y in x]
    tiles_unique = list(dict.fromkeys(best_tiles))
    print(len(tiles_unique))
    print(end_score)

    """
    while len(paths) > 0:
        new_paths = {}
        for k in paths.keys():
            pos = (k[0], k[1])
            if 0 < end_score < paths[k]:
                continue

            if grid[pos[1]][pos[0]] == 'E':
                end_score = paths[k]
                continue

            direction = k[2]
            if not get_wall(pos, grid, direction):
                new_pos = step(pos, direction)
                new_val = paths[k] + 1
                new_key = (new_pos[0], new_pos[1], direction)
                if (not ((new_key in paths and new_val > paths[new_key])
                        or (new_key in new_paths and new_val > new_paths[new_key]))
                    and not (new_key in visited and visited[new_key] < new_val)):
                    new_paths[new_key] = new_val
                    visited[new_key] = new_val

            new_val = paths[k] + 1000

            new_dir_r = turn_right(direction)
            new_key = (pos[0], pos[1], new_dir_r)
            if (not ((new_key in paths and new_val > paths[new_key])
                    or (new_key in new_paths and new_val > new_paths[new_key]))
                and not (new_key in visited and visited[new_key] < new_val)):
                new_paths[new_key] = new_val
                visited[new_key] = new_val

            new_dir_l = turn_left(direction)
            new_key = (pos[0], pos[1], new_dir_l)
            if (not ((new_key in paths and new_val > paths[new_key])
                    or (new_key in new_paths and new_val > new_paths[new_key]))
                and not (new_key in visited and visited[new_key] < new_val)):
                new_paths[new_key] = new_val
                visited[new_key] = new_val

        paths = new_paths

    print(end_score)
    """