from functools import cmp_to_key
from itertools import zip_longest


def read_puzzle_inputs(file_name='samples.txt'):
    with open(file_name, 'r') as f:
        puzzle_inputs = f.read().strip().split('\n\n')

    packets = []
    for p in puzzle_inputs:
        p1, p2 = p.split('\n')
        packets += [
            eval(p1),
            eval(p2)
        ]

    return packets


def do_compare(left, right):
    if right is None:
        return 1

    if left is None:
        return -1

    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, int) and isinstance(right, list):
        return do_compare([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return do_compare(left, [right])

    for left_value, right_value in zip_longest(left, right):
        comparison = do_compare(left_value, right_value)

        if comparison == 0:
            continue

        return comparison

    return 0


def part1_run(packets):
    result = []
    pairs = zip(packets[::2], packets[1::2])
    for i, (left, right) in enumerate(pairs):
        if do_compare(left, right) < 0:
            result.append(i + 1)

    return result


def part2_run(packets):
    divider1, divider2 = divider_packets = [
        [[2]],
        [[6]]
    ]
    packets += divider_packets

    # Sort it
    packets = sorted(packets, key=cmp_to_key(do_compare))

    return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)


if __name__ == '__main__':
    packets_input = read_puzzle_inputs(file_name='inputs.txt')

    part1 = part1_run(packets_input)
    print(f'Part 1: {sum(part1)}.')

    part2 = part2_run(packets_input)
    print(f'Part 2: {part2}.')
