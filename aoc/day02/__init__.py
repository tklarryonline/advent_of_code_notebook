import os

from aoc.day02.dive import dive_deeper


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**What do you get if you multiply your final horizontal position by your final depth?**\n"
        f"Part 01: {dive_deeper(inputs)}\n"
    )
