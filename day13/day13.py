from functools import cmp_to_key
import sys


def compare(l, r):
    for l_v, r_v in zip(l, r):
        if type(l_v) is list and type(r_v) is list:
            c = compare(l_v, r_v)
            if c != 0:
                return c
        elif type(l_v) is int and type(r_v) is int:
            if int(l_v) < int(r_v):
                return 1
            elif int(l_v) > int(r_v):
                return -1
        elif type(l_v) is list and type(r_v) is int:
            c = compare(l_v, [r_v])
            if c != 0:
                return c
        elif type(l_v) is int and type(r_v) is list:
            c = compare([l_v], r_v)
            if c != 0:
                return c
    if len(l) < len(r):
        return 1
    elif len(l) > len(r):
        return -1
    return 0


def solve_part_1(in_data):
    return sum(i + 1 for i, (l, r) in enumerate(in_data) if compare(l, r) == 1)


def solve_part_2(in_data):
    p = [l for l, r in in_data] + [r for l, r in in_data] + [[2], [6]]
    p.sort(key=cmp_to_key(compare), reverse=True)
    return (p.index([2]) + 1) * (p.index([6]) + 1)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    in_data = []
    with open(in_f) as f:
        for pair in f.read().split('\n\n'):
            l, r = map(eval, pair.split('\n'))
            in_data.append((l, r))
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
