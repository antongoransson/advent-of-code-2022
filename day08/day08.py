import sys


def is_visible(grid, p, l_r, l_c):
    r, c = p
    if (all(grid[rr, c] < grid[p] for rr in range(r + 1, l_r))):
        return True
    if (all(grid[rr, c] < grid[p] for rr in range(0, r))):
        return True
    if (all(grid[r, cc] < grid[p] for cc in range(0, c))):
        return True
    if (all(grid[r, cc] < grid[p] for cc in range(c + 1, l_c))):
        return True
    return False


def score(grid, p, l_r, l_c):
    r, c = p
    down, left, right, up = 0, 0, 0, 0
    for rr in range(r + 1, l_r):
        down += 1
        if grid[rr, c] >= grid[p]:
            break
    for cc in range(c - 1, -1, -1):
        left += 1
        if grid[r, cc] >= grid[p]:
            break
    for rr in range(r - 1, -1, -1):
        up += 1
        if grid[rr, c] >= grid[p]:
            break
    for cc in range(c + 1, l_c):
        right += 1
        if grid[r, cc] >= grid[p]:
            break
    return up * down * left * right


def solve_part_1(grid, l_r, l_c):
    return sum(is_visible(grid, p, l_r, l_c) for p in grid)


def solve_part_2(grid, l_r, l_c):
    return max(score(grid, p, l_r, l_c) for p in grid)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid, l_r, l_c = {}, 0, 0
    with open(in_f) as f:
        for r, l in enumerate(f):
            l_r += 1
            l_c = len(l.strip())
            for c, t in enumerate(l.strip()):
                grid[r, c] = int(t)
    sol1 = solve_part_1(grid, l_r, l_c)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid, l_r, l_c)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
