import sys
sys.path.append('..')
import aoc


def solve_part_1(stacks, moves):
    for n, i1, i2 in moves:
        stacks[i2 - 1] = stacks[i1 - 1][:n][::-1] + stacks[i2 - 1]
        stacks[i1 - 1] = stacks[i1 - 1][n:]
    return ''.join(s[0] for s in stacks)


def solve_part_2(stacks, moves):
    for n, i1, i2 in moves:
        stacks[i2 - 1] = stacks[i1 - 1][:n] + stacks[i2 - 1]
        stacks[i1 - 1] = stacks[i1 - 1][n:]
    return ''.join(s[0] for s in stacks)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    stacks = [[] for i in range(9 if in_f == 'in.txt' else 3)]
    with open(in_f) as f:
        in1, in2 = f.read().split('\n\n')
        i, j = 0, 0
        in1 = in1.replace('\n', ' ').split(' ')
        while i < len(in1):
            if in1[i].strip().isnumeric():
                break
            elif in1[i].strip() == '':
                i += 4
                j += 1
            else:
                stacks[j % len(stacks)].append(in1[i][1])
                i += 1
                j += 1
    moves = [aoc.get_ints(s) for s in in2.split('\n') if s.strip()]
    sol1 = solve_part_1([s for s in stacks], moves)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(stacks, moves)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
