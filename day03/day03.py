import sys

L = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def solve_part_1(in_data):
    s = 0
    for rs in in_data:
        i = len(rs) // 2
        for j in range(i):
            if rs[j] in rs[i:] and rs[j]:
                s += L.index(rs[j]) + 1
                break
    return s


def solve_part_2(in_data):
    s = 0
    for i in range(0, len(in_data), 3):
        r1, r2, r3 = in_data[i:i + 3]
        for c in r1:
            if c in r2 and c in r3:
                s += L.index(c) + 1
                break
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l. strip() for l in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
