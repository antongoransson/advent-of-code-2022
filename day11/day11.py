import sys
sys.path.append('..')
import aoc


class Monkey:

    def __init__(self, items, operation, test_n, monkey1, monkey2, is_part_1):
        self.n_inspects = 0
        self.items = [v for v in items]
        self.operation = self.get_operation_f(operation)
        self.test_n = test_n
        self.m1 = monkey1
        self.m2 = monkey2
        self.is_part_1 = is_part_1

    def throw(self, monkeys):
        next_monkey = monkeys[self.m1] if self.test() else monkeys[self.m2]
        item = self.items.pop(0)
        next_monkey.items.append(item)

    def inspect(self):
        new_v = self.operation(self.items[0])
        if self.is_part_1:
            new_v //= 3
        else:
            new_v %= self.mod_divisor
        self.items[0] = new_v
        self.n_inspects += 1

    def test(self):
        return self.items[0] % self.test_n == 0

    def has_items(self):
        return len(self.items)

    def get_operation_f(self, operation):
        op_n = aoc.get_ints(operation)
        if len(op_n):
            if '*' in operation:
                def m_op(old): return old * op_n[0]
            elif '+' in operation:
                def m_op(old): return old + op_n[0]

        else:
            if '*' in operation:
                def m_op(old): return old * old
            elif '+' in operation:
                def m_op(old): return old + old
        return m_op


def solve(n, monkeys):
    for i in range(n):
        for m in monkeys:
            while m.has_items():
                m.inspect()
                m.throw(monkeys)
    n_inspects = sorted([m.n_inspects for m in monkeys])
    return n_inspects[-1] * n_inspects[-2]


def solve_part_1(monkeys):
    return solve(20, monkeys)


def solve_part_2(monkeys):
    return solve(10000, monkeys)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    monkeys1 = []
    monkeys2 = []
    mod_divisor = 1
    with open(in_f) as f:
        for monkey in f.read().split('\n\n'):
            monkey_att = monkey.split('\n')
            items = aoc.get_ints(monkey_att[1])
            operation = monkey_att[2]
            test_n = aoc.get_ints(monkey_att[3])[0]
            mod_divisor *= test_n
            monkey1 = aoc.get_ints(monkey_att[4])[0]
            monkey2 = aoc.get_ints(monkey_att[5])[0]
            monkeys1.append(Monkey(items, operation, test_n, monkey1, monkey2, True))
            monkeys2.append(Monkey(items, operation, test_n, monkey1, monkey2, False))
        for m in monkeys1:
            m.mod_divisor = mod_divisor
        for m in monkeys2:
            m.mod_divisor = mod_divisor
    sol1 = solve_part_1(monkeys1)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(monkeys2)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
