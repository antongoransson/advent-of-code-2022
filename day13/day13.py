from functools import cmp_to_key
import sys


def compare(l, r):
    match (l[0], r[0]):
        case a, b if a == b:
            return compare(l[1:], r[1:])
        case ']', _:
            return -1
        case _, ']':
            return 1
        case '[', _:
            return compare(l, '[' + r[0] + ']' + r[1:])
        case _, '[':
            return compare('[' + l[0] + ']' + l[1:], r)
        case a, b:
            return ord(a) - ord(b)


def solve_part_1(in_data):
    return sum(i + 1 for i, (l, r) in enumerate(in_data) if compare(l, r) < 0)


def solve_part_2(in_data):
    p = ['[2]', '[6]']
    for pair in in_data:
        p.extend(pair)
    p.sort(key=cmp_to_key(compare))
    return (p.index('[2]') + 1) * (p.index('[6]') + 1)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    in_data = []
    with open(in_f) as f:
        for pair in f.read().split('\n\n'):
            l, r = pair.replace('10', 'A').split('\n')
            in_data.append((l, r))
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
