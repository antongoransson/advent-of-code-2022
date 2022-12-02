import sys
sys.path.append('..')

scoresp1 = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6
}

scoresp2 = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7
}


def solve_part_1(moves):
    return sum(scoresp1[m] for m in moves)


def solve_part_2(moves):
    return sum(scoresp2[m] for m in moves)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    moves = []
    with open(in_f) as f:
        for line in f:
            a, b = line.strip().split(' ')
            moves.append((a + b))
    sol1 = solve_part_1(moves)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(moves)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
