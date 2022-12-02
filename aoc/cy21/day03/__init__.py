import os

from aoc.cy21.day03.binary_diagnostic import life_support, power_consumption


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**What is the power consumption of the submarine?**\n"
        f"{power_consumption(numbers=inputs)}\n"
        f"**What is the life support rating of the submarine?**\n"
        f"{life_support(numbers=inputs)}\n"
    )
