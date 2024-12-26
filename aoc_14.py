
if __name__ == "__main__":
    global overall_sum

    f = open("input/14.txt", "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    width = 101
    height = 103

    #width = 11
    #height = 7

    #steps = 100

    #grid = [[0 for x in range(width)] for y in range(height)]

    robots = []
    for line in lines:
        l = line.split(' ')
        p = l[0].split('=')[1].split(',')
        v = l[1].split('=')[1].split(',')
        robots.append({'x': int(p[0]), 'y': int(p[1]), 'vx': int(v[0]), 'vy': int(v[1])})
        #grid[int(p[1])][int(p[0])] += 1 # P2

    print(robots)

    half_width = int((width-1)/2)
    """
    tree = [[0 for x in range(width)] for y in range(height)]
    for h in range(height-1):
        tree[h][half_width - h] = 1
        tree[h][half_width + h] = 1
    tree[height-1][half_width] = 1
    """

    tree_steps = 0
    robot_crowd = 0
    for n in range(100000):
    #while True:

        for r in robots:
            #grid[r['y']][r['x']] -= 1
            r['x'] = (r['x'] + r['vx']) % width
            if r['x'] < 0:
                r['x'] = width - r['x']
            r['y'] = (r['y'] + r['vy']) % height
            if r['y'] < 0:
                r['y'] = height - r['y']
            #grid[r['y']][r['x']] += 1

        #if grid == tree:
        #    break
        """is_tree = False
        for h in range(height - half_width - 1):
            is_tree = True

            #tree = [[0 for x in range(width)] for y in range(height)]
            for x in range(h, h + half_width+1):
                #tree[x][half_width - (x-h)] = 1
                #tree[x][half_width + (x-h)] = 1
                if grid[x][half_width - (x-h)] == 0 or grid[x][half_width + (x-h)] == 0:
                    is_tree = False
                    break

            #tree[h + half_width + 1][half_width] = 1
            if grid[h + half_width + 1][half_width] == 0:
                is_tree = False

        if is_tree:
            break
        """

        if tree_steps < 5000:
            continue

        new_crowd = 0
        for r1, rob1 in enumerate(robots):
            for r2 in range(r1+1, len(robots)):
                rob2 = robots[r2]
                # robot distance
                rob_dist = abs(rob1['x'] - rob2['x']) + abs(rob1['y'] - rob2['y'])
                if rob_dist < 10:
                    new_crowd += 1
        if new_crowd > robot_crowd:
            robot_crowd = new_crowd
            tree_steps = n + 1
            print(robot_crowd, tree_steps)

            if robot_crowd > 10000:
                grid = [['.' for x in range(width)] for y in range(height)]
                for r in robots:
                    grid[r['y']][r['x']] = 'R'
                for g in grid:
                    print(''.join(g))


    """for r in robots:
        r['x'] = (r['x'] + r['vx']*steps) % width
        if r['x'] < 0:
            r['x'] = width - r['x']
        r['y'] = (r['y'] + r['vy']*steps) % height
        if r['y'] < 0:
            r['y'] = height - r['y']

    q = [0, 0, 0, 0]
    for r in robots:
        if r['x'] < (width-1) / 2 and r['y'] < (height - 1) / 2:
            q[0] += 1
        elif r['x'] < (width-1) / 2 and r['y'] > (height - 1) / 2:
            q[1] += 1
        elif r['x'] > (width-1) / 2 and r['y'] < (height - 1) / 2:
            q[2] += 1
        elif r['x'] > (width-1) / 2 and r['y'] > (height - 1) / 2:
            q[3] += 1
            
    res = q[0] * q[1] * q[2] * q[3]
    print(res)
    """