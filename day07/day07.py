import sys


def get_file_structure(cmds):
    pwd = '/'
    dirs = {'/': {'children': set(), 'is_d': True}}
    i = 1
    for c in cmds:
        if '$ cd ' in c:
            if '..' in c:
                pwd = dirs[pwd]['parent']
            elif '/' in c:
                pwd = '/'
            else:
                n_pwd = pwd + '/' + c.split(' ')[2]
                if n_pwd not in dirs:
                    dirs[n_pwd] = {'parent': pwd, 'children': set(), 'is_d': True}
                    dirs[pwd]['children'].add(n_pwd)
                pwd = n_pwd
        elif '$ ls' not in c:
            s, fn = c.split(' ')
            fn = pwd + '/' + fn
            if s != 'dir':
                dirs[fn] = {'is_d': False, 'size': int(s), 'parent': pwd}
                dirs[pwd]['children'].add(fn)
    return dirs


def get_size(d, dirs, cache):
    if d in cache:
        return cache[d]
    if dirs[d]['is_d']:
        s = sum(get_size(c, dirs, cache) for c in dirs[d]['children'])
        cache[d] = s
        return s
    else:
        return dirs[d]['size']


def get_dir_sizes(cmds):
    cache = {}
    files = get_file_structure(cmds)
    return [get_size(d, files, cache) for d in files if files[d]['is_d']]


def solve_part_1(d_sizes):
    return sum(s for s in d_sizes if s <= 100000)


def solve_part_2(d_sizes):
    return min(s for s in d_sizes if s >= 30000000 - (70000000 - max(d_sizes)))


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l.strip() for l in f]
    d_sizes = get_dir_sizes(in_data)
    sol1 = solve_part_1(d_sizes)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(d_sizes)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
