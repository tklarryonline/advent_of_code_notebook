import os

from aoc.day08.seven_segment_search import part01


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**In the output values, how many times do digits 1, 4, 7, or 8 appear?**\n"
        f"Part 1: {part01(inputs)}\n"
        f"**What do you get if you add up all of the output values?**\n"
    )
