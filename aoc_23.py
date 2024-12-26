connections = {}

def get_largest_group(c, start_comp, group_comps):
    if c == len(connections[start_comp]):
        return len(group_comps), group_comps

    new_comp = connections[start_comp][c]

    valid = True
    for g_comp in group_comps:
        if new_comp not in connections[g_comp]:
            valid = False
            break

    x = [0, None]
    if valid:
        x = get_largest_group(c+1, start_comp, group_comps+[new_comp])
    y = get_largest_group(c+1, start_comp, group_comps)

    if x[0] > y[0]:
        return x
    return y

if __name__ == "__main__":
    f = open("input/23.txt", "r")
    lines = f.readlines()
    lines = [line.strip().split('-') for line in lines]

    computers = set()
    for comp in lines:
        if comp[0] not in computers:
            computers.add(comp[0])
        if comp[1] not in computers:
            computers.add(comp[1])
    print('computers', len(computers))

    for comp in computers:
        connections[comp] = []

    for comp in lines:
        connections[comp[0]].append(comp[1])
        connections[comp[1]].append(comp[0])
    print(connections)

    max_group = []
    for comp in computers:
        group = get_largest_group(0, comp, [comp])
        if group[0] > len(max_group):
            max_group = group[1]

    max_group.sort()
    print(','.join(max_group))

    """
    t_computers = set()
    for comp in computers:
        if comp.startswith('t'):
            t_computers.add(comp)
    print(t_computers)

    groups = set()
    for comp in t_computers:
        t_conns = connections[comp]
        for c, conn in enumerate(t_conns):
            for c2 in range(c+1, len(t_conns)):
                conn2 = t_conns[c2]
                if conn2 in connections[conn]:
                    triple = [conn2, conn, comp]
                    triple.sort()
                    triple = tuple(triple)
                    if triple not in groups:
                        groups.add(triple)

    print(len(groups))
    """




