import os

from aoc.cy21.day02.dive import dive_and_aim, simply_dive


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**What do you get if you multiply your final horizontal position by your final depth?**\n"
        f"Part 01: {simply_dive(inputs)}\n"
        f"Part 02: {dive_and_aim(inputs)}\n"
    )
