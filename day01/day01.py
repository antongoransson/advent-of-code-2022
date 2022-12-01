import sys


def solve_part_1(elves):
    return max(sum(x) for x in elves)


def solve_part_2(elves):
    s = sorted([sum(x) for x in elves])
    return s[-1] + s[-2] + s[-3]


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    elves = [[]]
    with open(in_f) as f:
        for line in f.readlines():
            l = line.strip()
            if l == '':
                elves.append([])
            else:
                elves[-1].append(int(l))

    sol1 = solve_part_1(elves)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(elves)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
