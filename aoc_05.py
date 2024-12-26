import re

if __name__ == "__main__":
    global grid, dim

    f = open("input/05.txt", "r")
    content = f.read()
    sections = content.split('\n---\n')

    rule_sec = sections[0].split('\n')
    print_sec = sections[1].split('\n')

    rules = {}
    for r in rule_sec:
        parts = r.split('|')
        x = int(parts[0])
        #if not x in rules.keys():
        if rules.get(x) is None:
            rules[x] = []
        rules[x].append(int(parts[1]))

    prints = []
    for p in print_sec:
        prints.append([int(x) for x in p.split(',')])

    print(rules)
    print(prints)

    res = 0
    for pidx, p in enumerate(prints):
        valid = False
        all_valid = True
        while not valid:
            printed = []
            valid = True
            for i, x in enumerate(p):
                for j, y in enumerate(printed):
                    if rules.get(x) is not None and y in rules[x]:
                        print('wrong order', p)
                        valid = False
                        all_valid = False
                        #print('i', i)
                        #print('j', j)
                        for k in reversed(range(j, i)):
                            #print('k', k)
                            p[k+1] = p[k]
                        p[j] = x
                        print('right order', p)
                        break
                if not valid:
                    break
                printed.append(x)
        if not all_valid:
            res += p[int((len(p)-1)/2)]

    print(res)

    """
    res = 0
    for p in prints:
        valid = True
        printed = []
        for x in p:
            for y in printed:
                if rules.get(x) is not None and y in rules[x]:
                    valid = False
                    break
            if not valid:
                print('not valid:', p)
                break
            printed.append(x)
        if valid:
            print('valid:', p)
            res += p[int((len(p)-1)/2)]

    print(res)
    """
