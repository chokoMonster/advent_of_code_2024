import math
from collections import deque


def get_next_num(n):
    n = (n ^ (n*64)) % 16777216 # XOR
    n = (n ^ math.floor(n/32)) % 16777216
    n = (n ^ (n*2048)) % 16777216
    return n


if __name__ == "__main__":
    f = open("input/22.txt", "r")
    lines = f.readlines()
    lines = [int(line.strip()) for line in lines]

    history = deque([])
    change_values = {}

    for i, secret_number in enumerate(lines):
        history = deque([])
        num = get_next_num(secret_number)
        ones_digit = num % 10
        for x in range(1999):
            num = get_next_num(num)
            ones_digit_new = num % 10
            ones_digit_dif = ones_digit_new - ones_digit
            ones_digit = ones_digit_new

            if len(history) == 4:
                history.rotate(-1)
                history[3] = ones_digit_dif
                hist_key = tuple(history)
                if hist_key in change_values.keys():
                    if change_values[hist_key][0] <= i:
                        change_values[hist_key][0] = i+1
                        change_values[hist_key][1] += ones_digit_new
                else:
                    change_values[hist_key] = [i+1, ones_digit_new]
            else:
                history.append(ones_digit_dif)

    max_price = 0
    for v in change_values.values():
        if max_price < v[1]:
            max_price = v[1]
    print('price:', max_price)


    """
    res = 0
    for secret_number in lines:
        print(secret_number)
        num = secret_number
        for i in range(2000):
            num = get_next_num(num)
        res += num
    print(res)
    """