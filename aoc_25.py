if __name__ == "__main__":
    f = open("input/25.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    locks = []
    keys = []
    i = 0
    while i < len(lines):
        if lines[i][0] == '#':
            lock = []
            while len(lines[i]) > 0:
                lock.append(lines[i])
                i += 1
            locks.append(lock)
        elif lines[i][0] == '.':
            key = []
            while len(lines[i]) > 0:
                key.append(lines[i])
                i += 1
            keys.append(key)
        i += 1

    lock_heights = []
    key_heights = []

    for lock in locks:
        l = []
        for i in range(0, len(lock[0])):
            height = 0
            for j in range(1, len(lock)):
                if lock[j][i] == '.':
                    break
                height += 1
            l.append(height)
        lock_heights.append(l)

    for key in keys:
        k = []
        for i in range(0, len(key[0])):
            height = 0
            for j in reversed(range(0, len(key)-1)):
                if key[j][i] == '.':
                    break
                height += 1
            k.append(height)
        key_heights.append(k)

    print(lock_heights)
    print(key_heights)

    matches = 0
    for lock in lock_heights:
        for key in key_heights:
            match = True
            for i in range(0, len(lock)):
                if lock[i] + key[i] > 5:
                    match = False
                    break
            if match:
                matches += 1

    print(matches)
