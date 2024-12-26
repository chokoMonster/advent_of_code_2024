def transform_stone(st):
    if st == 0:
        return [1]
    x = str(st)
    if len(x) % 2 == 0:
        h = int(len(x)/2)
        s1 = x[:h]
        s2 = x[h:]
        return [int(s1), int(s2)]
    return [st*2024]


if __name__ == "__main__":
    f = open("input/11.txt", "r")
    line = f.read()
    line = line.strip()
    line = [int(l) for l in line.split(' ')]
    print(line)

    stones = {}
    for s in line:
        stones[s] = 1

    for i in range(75):
        trans_stones = {}
        for k in stones:
            new_stone = transform_stone(k)

            if new_stone[0] in trans_stones:
                trans_stones[new_stone[0]] += stones[k]
            else:
                trans_stones[new_stone[0]] = stones[k]

            if len(new_stone) > 1:
                if new_stone[1] in trans_stones:
                    trans_stones[new_stone[1]] += stones[k]
                else:
                    trans_stones[new_stone[1]] = stones[k]

        stones = trans_stones

    res = 0
    for v in stones.values():
        res += v

    print(res)
