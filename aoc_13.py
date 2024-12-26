from sympy.solvers import *
from sympy import Symbol, Mod

def split_button_line(line, sep='+'):
    l = line.split(': ')[1].split(', ')
    x = l[0].split(sep)[1]
    y = l[1].split(sep)[1]
    return (int(x), int(y))


if __name__ == "__main__":
    f = open("input/13.txt", "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    res = 0
    i = 0
    while i < len(lines):
        (ax, ay) = split_button_line(lines[i])
        (bx, by) = split_button_line(lines[i+1])
        (px, py) = split_button_line(lines[i+2], '=')
        i += 4

        a = Symbol('a')
        b = Symbol('b')

        eqs = []
        # PART 1
        #e1 = a * ax + b * bx - px
        #e2 = a * ay + b * by - py
        e1 = a * ax + b * bx - (px+10000000000000)
        e2 = a * ay + b * by - (py+10000000000000)
        eqs.append(e1)
        eqs.append(e2)
        eqs.append(Mod(a, 1))
        eqs.append(Mod(b, 1))

        r = solve(eqs, *([a, b]))

        if len(r) > 0:
            res += r[0][0] * 3 + r[0][1]

    print(res)


