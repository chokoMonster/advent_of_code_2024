
if __name__ == "__main__":

    f = open("input/09.txt", "r")
    line = f.read()
    blocks = list(line)
    blocks = [int(b) for b in blocks]

    files = blocks[0::2]
    free = blocks[1::2]

    res = 0
    for i, file_blocks in enumerate(reversed(files)):
        idx = len(files)-1 - i
        for j, f in enumerate(free):
            if idx == j:
                ges_idx = 2*idx
                pos = sum(blocks[:ges_idx])
                for x in range(file_blocks):
                    res += idx * pos
                    pos += 1
                break
            if f >= file_blocks:
                ges_idx = 2*j + 1
                pos = sum(blocks[:ges_idx])
                if f < blocks[ges_idx]:
                    pos += blocks[ges_idx] - f
                for x in range(file_blocks):
                    res += idx * pos
                    pos += 1
                free[j] -= file_blocks
                break

    print(res)
    #6488291456470

    """
    file_idx = 0
    cur_idx = len(files)-1
    cur_blocks = files[cur_idx]

    stop = False
    for i, free_block in enumerate(free):

        file_idx += 1
        for f in range(free_block):
            res += pos * cur_idx
            #print(pos, cur_idx, res)
            pos += 1
            cur_blocks -= 1

            if cur_blocks == 0:
                cur_idx -= 1
                cur_blocks = files[cur_idx]
                if cur_idx < file_idx:
                    stop = True
                    break

        if stop:
            break

        if (i+1) == cur_idx:
            file_blocks = files[file_idx]
            for f in range(file_blocks-cur_blocks, file_blocks):
                res += file_idx * pos
                #print('file', pos, file_idx, res)
            pos += 1
            print(i+1)
            break

        for f in range(files[file_idx]):
            res += file_idx * pos
            print('file', pos, file_idx, res)
            pos += 1

    print(res)

    """

