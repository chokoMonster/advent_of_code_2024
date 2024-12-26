import itertools

def check_eq(r, n, p):
    ops = [0, 1]
    if p == 2:
        ops = [0, 1, 2]
    combs = list(itertools.product(ops, repeat=len(n)))

    for c in combs:
        op_res = 0
        for i, op in enumerate(c):
            if op == 0:
                op_res += n[i]
            elif op == 1:
                op_res *= n[i]
            elif op == 2:
                op_res = int(str(op_res) + str(n[i]))
        if op_res == r:
            return True
    return False

if __name__ == "__main__":
    global grid, dim

    f = open("input/07.txt", "r")
    lines = f.readlines()

    sum_eqs = 0
    for line in lines:
        r = line.split(':')
        res = int(r[0])
        nums = r[1].strip().split(' ')
        nums = [int(n) for n in nums]

        if check_eq(res, nums, 2):
            sum_eqs += res

    print(sum_eqs)
