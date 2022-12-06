import sys
sys.path.append('..')


def solve(signal, n):
    for i in range(len(signal)):
        if len(set(signal[i:i + n])) == n:
            return i + n


def solve_part_1(in_data):
    return solve(in_data, 4)


def solve_part_2(in_data):
    return solve(in_data, 14)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = f.readlines()[0]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
