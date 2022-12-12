import math
import re
from copy import deepcopy
from typing import Callable

NUMBER = re.compile(r'(\d+)')


class Monkey:

    def __init__(self, items: list[int], operation: Callable, divisible_by: int, test_true: int, test_false: int):
        self.inspections_count = 0
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.test_true = test_true
        self.test_false = test_false

    @classmethod
    def create(cls, monkey_str: str) -> 'Monkey':
        return cls(*[
            cls.parse_attr(attr)
            for attr in monkey_str.strip().split('\n')[1:]
        ])

    @classmethod
    def parse_attr(cls, attr: str):
        attr = attr.strip()

        if attr.startswith('Starting items:'):
            return [int(x) for x in NUMBER.findall(attr)]

        if attr.startswith('Operation:'):
            return eval(attr.replace('Operation: new = ', 'lambda old: '))

        if attr.startswith('Test:') or attr.startswith('If'):
            return int(attr.split(' ')[-1])

    def inspect(self, monkeys: list, part: int, lcm: int):
        """The monkey takes a turn"""
        while self.items:
            item = self.items.pop(0)
            self.inspections_count += 1

            # You begin to worry
            item = self.operation(item)

            # Then you're not
            if part == 1:
                item //= 3
            else:
                item %= lcm

            # Monkey tests you
            target = self.test(item)
            monkeys[target].items.append(item)

    def test(self, item: int):
        if item % self.divisible_by == 0:
            return self.test_true
        else:
            return self.test_false


# file_name = 'samples.txt'
file_name = 'inputs.txt'
with open(file_name, 'r') as f:
    puzzle_inputs = f.read().split('\n\n')

monkeys = [
    Monkey.create(monkey_str)
    for monkey_str in puzzle_inputs
]
lcm = math.lcm(*[m.divisible_by for m in monkeys])


def run(part, rounds=20):
    _monkeys = deepcopy(monkeys)
    for i in range(rounds):
        for monkey in _monkeys:
            monkey.inspect(_monkeys, part, lcm)

    inspections = sorted([monkey.inspections_count for monkey in _monkeys])
    print(f'Part {part} = {inspections[-1] * inspections[-2]}')


run(1)
run(2, rounds=10000)
