import os

from aoc.day06.lanternfish import part01_count_fishes


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.read()

    print(
        f"**How many lanternfish would there be after X days?**\n"
        f"Part 1: 80 days: {part01_count_fishes(inputs, days=80)}\n"
        f"Part 2: 256 days: {part01_count_fishes(inputs, days=256)}\n"
    )
