from collections import deque
import sys
sys.path.append('..')
import aoc


def bfs(grid, starts, target):
    visited = set()
    q = deque([[start]for start in starts])
    while q:
        path = q.popleft()
        node = path[-1]
        if node in visited:
            continue
        for n in aoc.neighbours(grid, node):
            if ord(grid[n]) - ord(grid[node]) < 2:
                if n == target:
                    return len(path)
                new_path = list(path) + [n]
                q.append(new_path)
        visited.add(node)


def solve_part_1(grid, start, target):
    return bfs(grid, [start], target)


def solve_part_2(grid, starts, target):
    return bfs(grid, starts, target)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid = {}
    starts = []
    with open(in_f) as f:
        for r, l in enumerate(f):
            for c, v in enumerate(l.strip()):
                if v == 'S':
                    start = r, c
                    grid[r, c] = 'a'
                elif v == 'E':
                    target = r, c
                    grid[r, c] = 'z'
                else:
                    grid[r, c] = v
                if grid[r, c] == 'a':
                    starts.append((r, c))
    sol1 = solve_part_1(grid, start, target)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid, starts, target)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
