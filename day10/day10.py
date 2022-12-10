from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def get_score(i, x):
    if i in [20, 60, 100, 140, 180, 220]:
        return i * x
    return 0


def solve_part_1(in_data):
    i, x, s = 0, 1, 0
    for cmd in in_data:
        if 'noop' in cmd:
            i += 1
            s += get_score(i, x)
        elif 'addx' in cmd:
            i += 1
            s += get_score(i, x)
            i += 1
            s += get_score(i, x)
            x += int(cmd.split(' ')[1])
    return s, i, x


def draw(i, x, s):
    p = (i - 1) % 40
    if p == 0:
        s += '\n'
    if p in [x - 1, x, x + 1]:
        return s + '#'
    return s + ' '


def solve_part_2(in_data):
    i = 0
    x = 1
    s = ''
    for cmd in in_data:
        if 'noop' in cmd:
            i += 1
            s = draw(i, x, s)
        elif 'addx' in cmd:
            i += 1
            s = draw(i, x, s)
            i += 1
            s = draw(i, x, s)
            x += int(cmd.split(' ')[1])
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l.strip() for l in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
