import sys

move = {
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c),
    'L': lambda r, c: (r, c - 1),
    'R': lambda r, c: (r, c + 1)
}


def step(h, t):
    hr, hc = h
    tr, tc = t
    dr = abs(hr - tr)
    dc = abs(hc - tc)
    if dr == 0:
        if dc == 2:
            tc = tc + 1 if hc > tc else tc - 1
    elif dc == 0:
        if dr == 2:
            tr = tr + 1 if hr > tr else tr - 1
    elif dr and dc != 1 or dc and dr != 1:
        tr = tr - 1 if hr - tr < 0 else tr + 1
        tc = tc - 1 if hc - tc < 0 else tc + 1
    return tr, tc


def solve_part_1(in_data):
    hr, hc, tr, tc = 0, 0, 0, 0
    visited = set()
    visited.add((tr, tc))
    for m, n in in_data:
        for i in range(n):
            hr, hc = move[m](hr, hc)
            tr, tc = step((hr, hc), (tr, tc))
            visited.add((tr, tc))
    return len(visited)


def solve_part_2(in_data):
    hr, hc = 0, 0
    knots = [(0, 0) for _ in range(9)]
    visited = set()
    visited.add((0, 0))
    for m, n in in_data:
        for i in range(n):
            hr, hc = move[m](hr, hc)
            rope = [(hr, hc)] + knots
            for j in range(1, len(rope)):
                rope[j] = step(rope[j - 1], rope[j])
            knots = rope[1:len(rope)]
            visited.add(knots[-1])
    return len(visited)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [(l.strip().split()[0], int(l.strip().split()[1])) for l in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
