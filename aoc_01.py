if __name__ == "__main__":

    f = open("input/01.txt", "r")
    lines = f.readlines()

    l1 = []
    l2 = []
    for line in lines:
        lx = line.split('   ')
        l1.append(int(lx[0]))
        l2.append(int(lx[1]))

    l1.sort()
    l2.sort()
    sum1 = 0
    for x, a in enumerate(l1):
        sum1 += abs(a - l2[x])
    print(sum1)

    sum2 = 0
    for a in l1:
        sum2 += a * l2.count(a)
    print(sum2)
