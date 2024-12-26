import re
from operator import contains

if __name__ == "__main__":

    f = open("input/03.txt", "r")
    l = f.read()
    #l = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

    res = 0

    do = []
    do_not = l.split('don\'t()')
    for i, dnt in enumerate(do_not):
        if i == 0:
            do.append(dnt)
        elif contains(dnt, 'do()'):
            do_list = dnt.split('do()', 1)
            do.append(do_list[1])

    for inp in do:
        mul_list = re.findall('mul\([1-9][0-9]*,[1-9][0-9]*\)', inp)
        print(mul_list)
        for mul in mul_list:
            mul = mul[4:len(mul) - 1]
            nums = mul.split(',')
            res += int(nums[0]) * int(nums[1])

    """
    mul_list = re.findall('mul\([1-9][0-9]*,[1-9][0-9]*\)', l)
    print(mul_list)

    for mul in mul_list:
        mul = mul[4:len(mul)-1]
        nums = mul.split(',')

        res += int(nums[0]) * int(nums[1])
    """

    print(res)
