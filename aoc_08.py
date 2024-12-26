
if __name__ == "__main__":
    f = open("input/08.txt", "r")
    lines = f.readlines()

    grid_size = len(lines)
    antennas = {}
    for j, line in enumerate(lines):
        for i, l in enumerate(line):
            if l != '.' and l != '\n':
                if antennas.get(l) is None:
                    antennas[l] = []
                antennas[l].append((i, j))

    positions = []
    positions2 = []

    for a in antennas:
        #print(a, antennas[a])
        ant_pos = antennas[a]

        for i in range(len(ant_pos)-1):
            for j in range(i+1, len(ant_pos)):
                delta_x = ant_pos[j][0] - ant_pos[i][0]
                delta_y = ant_pos[j][1] - ant_pos[i][1]

                #print(delta_x)

                #### 1
                # position zwischen 2 Antennen?
                if abs(delta_x) >= 3 or abs(delta_y) >= 3:
                    if delta_x % 3 == 0 and delta_y % 3 == 0:
                        positions.append((ant_pos[i][0]+delta_x/3, ant_pos[i][1]+delta_y/3))
                        positions.append((ant_pos[j][0]-delta_x/3, ant_pos[j][1]-delta_y/3))

                if 0 <= ant_pos[j][0]+delta_x < grid_size and 0 <= ant_pos[j][1]+delta_y < grid_size:
                    positions.append((ant_pos[j][0]+delta_x, ant_pos[j][1]+delta_y))
                if 0 <= ant_pos[i][0]-delta_x < grid_size and 0 <= ant_pos[i][1]-delta_y < grid_size:
                    positions.append((ant_pos[i][0]-delta_x, ant_pos[i][1]-delta_y))

                ##### 2
                r = 0
                while 0 <= ant_pos[i][0]+ r*delta_x < grid_size and 0 <= ant_pos[i][1]+ r*delta_y < grid_size:
                    positions2.append((ant_pos[i][0] + r*delta_x, ant_pos[i][1] + r*delta_y))
                    r += 1
                r = 1
                while 0 <= ant_pos[i][0] - r*delta_x < grid_size and 0 <= ant_pos[i][1] - r*delta_y < grid_size:
                    positions2.append((ant_pos[i][0] - r*delta_x, ant_pos[i][1] - r*delta_y))
                    r += 1

                #print(positions2)

    print(positions)
    p = list(dict.fromkeys(positions))
    print(len(p))

    print(positions2)
    p2 = list(dict.fromkeys(positions2))
    print(len(p2))