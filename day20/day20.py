from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def mix(l, c_i):
    item = [(x, i) for i, x in enumerate(l) if x[1] == c_i][0]
    v, i = item
    n = v[0]
    new_i = (i + n) % (len(l) - 1)
    if new_i >= i:
        l = l[0:i] + l[i + 1:new_i + 1] + [(n, v[1])] + l[new_i + 1:]
    elif i > new_i:
        l = l[0:new_i] + [(n, v[1])] + l[new_i:i] + l[i + 1:]
    return l


def solve_part_1(in_data):
    l = [(v, i) for i, v in enumerate(in_data)]
    for i in range(len(l)):
        l = mix(l, i)
    i0 = [i for i, v in enumerate(l) if v[0] == 0][0]
    return l[(i0 + 1000) % len(l)][0] + l[(i0 + 2000) % len(l)][0] + l[(i0 + 3000) % len(l)][0]


def solve_part_2(in_data):
    l = [(v * 811589153, i) for i, v in enumerate(in_data)]
    length = len(l)
    for _ in range(10):
        for c_i in range(length):
            l = mix(l, c_i)
    i0 = [i for i, v in enumerate(l) if v[0] == 0][0]
    return l[(i0 + 1000) % len(l)][0] + l[(i0 + 2000) % len(l)][0] + l[(i0 + 3000) % len(l)][0]


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    m = []
    with open(in_f) as f:
        in_data = aoc.get_ints(f.read())
    # for i, n in enumerate(in_data):
    #     m.append((n, False))
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
