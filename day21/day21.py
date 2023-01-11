from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def solve_part_1(monkeys):
    return get_value('root', monkeys, {})


def solve_part_2(monkeys):
    monkey = monkeys['root']
    me = monkeys['humn']
    n2 = get_value(monkey['m2'], monkeys, {})
    h = 10009000000000
    l = 0
    while l < h:
        m = (l + h) // 2
        me['n'] = m
        n1 = get_value(monkey['m1'], monkeys, {})
        if n1 < n2:
            h = m - 1
        elif n1 > n2:  # Bigger m means smaller n1
            l = m + 1
        else:
            return m


def apply_op(n1, n2, op):
    match (op):
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '/':
            return n1 // n2
        case '*':
            return n1 * n2
    assert False


def get_value(monkey_name, monkeys, cache):
    monkey = monkeys[monkey_name]
    if 'n' in monkey:
        return monkey['n']
    if monkey_name in cache:
        return cache[monkey_name]
    n1 = cache[monkey['m1']] if monkey['m1'] in cache else get_value(monkey['m1'], monkeys, cache)
    n2 = cache[monkey['m2']] if monkey['m2'] in cache else get_value(monkey['m2'], monkeys, cache)
    r = apply_op(n1, n2, monkey['op'])
    cache[monkey_name] = r
    return r


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    monkeys = {}
    with open(in_f) as f:
        for line in f:
            l = line.strip().split(' ')
            monkey = l[0][:-1]
            if len(l) == 2:
                monkeys[monkey] = {'n': int(l[1])}
            else:
                monkeys[monkey] = {'m1': l[1], 'op': l[2], 'm2': l[3]}
    sol1 = solve_part_1(monkeys)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(monkeys)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
