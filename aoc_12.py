global grid
"""
def find_region(x, y, p):
    global grid

    perimeter = 0
    area = 0

    if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]):
        return (0, 1)

    if grid[x][y].islower() and p.lower() == grid[x][y]:
        return (0, 0)

    if p != grid[x][y]:
        return (0, 1)

    area += 1
    grid[x][y] = p.lower()

    reg = find_region(x+1, y, p)
    area += reg[0]
    perimeter += reg[1]

    reg = find_region(x-1, y, p)
    area += reg[0]
    perimeter += reg[1]

    reg = find_region(x, y+1, p)
    area += reg[0]
    perimeter += reg[1]

    reg = find_region(x, y-1, p)
    area += reg[0]
    perimeter += reg[1]

    return (area, perimeter)
"""

def find_region(x, y, p):
    global grid

    area = 0
    side_list = []

    if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]):
        return (0, -1, side_list)

    if grid[x][y].islower() and p.lower() == grid[x][y]:
        return (0, 0, side_list)

    if p != grid[x][y]:
        return (0, -1, side_list)

    area += 1
    grid[x][y] = p.lower()

    reg = find_region(x+1, y, p)
    area += reg[0]
    if reg[1] == -1:
        side_list.append([x, y, 'D'])
    side_list += reg[2]

    reg = find_region(x-1, y, p)
    area += reg[0]
    if reg[1] == -1:
        side_list.append([x, y, 'U'])
    side_list += reg[2]

    reg = find_region(x, y+1, p)
    area += reg[0]
    if reg[1] == -1:
        side_list.append([x, y, 'R'])
    side_list += reg[2]

    reg = find_region(x, y-1, p)
    area += reg[0]
    if reg[1] == -1:
        side_list.append([x, y, 'L'])
    side_list += reg[2]

    return (area, 0, side_list)

if __name__ == "__main__":
    global grid

    f = open("input/12.txt", "r")
    grid = f.readlines()
    grid = [list(l.strip()) for l in grid]

    price = 0

    for i, line in enumerate(grid):
        for j, plot in enumerate(line):
            if plot.islower():
                continue
            region = find_region(i, j, plot)

            sides_hor = sorted(sorted(sorted(region[2], key=lambda x: x[1]), key=lambda x: x[2]), key=lambda x: x[0])

            len_hor = 0
            x = 0
            while x < len(sides_hor):
                s = sides_hor[x]
                if s[2] == 'R' or s[2] == 'L':
                    x += 1
                    continue

                len_hor += 1

                while x < len(sides_hor) - 1:
                    s_next = sides_hor[x+1]
                    if s[0] == s_next[0] and s[1] == s_next[1]-1 and s[2] == s_next[2]:
                        s = s_next
                        x += 1
                    else:
                        break
                x += 1

            sides_ver = sorted(sorted(sorted(region[2], key=lambda x: x[0]), key=lambda x: x[2]), key=lambda x: x[1])

            len_ver = 0
            x = 0
            while x < len(sides_ver):
                s = sides_ver[x]
                if s[2] == 'U' or s[2] == 'D':
                    x += 1
                    continue

                len_ver += 1

                while x < len(sides_ver) - 1:
                    s_next = sides_ver[x+1]
                    if s[0] == s_next[0]-1 and s[1] == s_next[1] and s[2] == s_next[2]:
                        s = s_next
                        x += 1
                    else:
                        break
                x += 1

            #price += region[0] * region[1]
            price += region[0] * (len_hor + len_ver)

    print(price)
