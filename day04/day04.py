import sys
sys.path.append('..')
import aoc


def solve_part_1(in_d):
    return sum(x1 <= y1 and x2 >= y2 or y1 <= x1 and y2 >= x2 for x1, x2, y1, y2 in in_d)


def solve_part_2(in_d):
    return sum(x1 <= y2 and x2 >= y1 for x1, x2, y1, y2 in in_d)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_d = [aoc.get_ints(l, sign=False) for l in f]
    sol1 = solve_part_1(in_d)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_d)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
