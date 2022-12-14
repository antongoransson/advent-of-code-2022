from copy import deepcopy
import sys


def produce(grid, max_r, part2=False):
    sand_p = (0, 500)
    if sand_p in grid:
        return False
    while True:
        r, c = sand_p
        down = (r + 1, c)
        if down in grid:
            down_left = (r + 1, c - 1)
            if down_left in grid:
                down_right = (r + 1, c + 1)
                if down_right in grid:
                    grid.add(sand_p)
                    return True
                else:
                    sand_p = down_right
            else:
                sand_p = down_left
        else:
            sand_p = down
        if sand_p[0] > max_r and not part2:
            return False


def solve_part_1(grid):
    i = 0
    max_r = max(r for r, y in grid)
    while produce(grid, max_r):
        i += 1
    return i


def solve_part_2(grid):
    i = 0
    max_r = max(r for r, y in grid)
    for k in range(0, 1000 + 1):
        grid.add((max_r + 2, k))
    while produce(grid, max_r, True):
        i += 1
    return i


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid = set()
    with open(in_f) as f:
        for path in f:
            coords = path.strip().split(' -> ')
            for i in range(1, len(coords)):
                c1, r1 = map(int, coords[i - 1].split(','))
                c2, r2 = map(int, coords[i].split(','))
                for k in range(r1, r2 + 1):
                    grid.add((k, c1))
                for k in range(r2, r1 + 1):
                    grid.add((k, c1))
                for k in range(c1, c2 + 1):
                    grid.add((r1, k))
                for k in range(c2, c1 + 1):
                    grid.add((r1, k))
    sol1 = solve_part_1(set(x for x in grid))
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
