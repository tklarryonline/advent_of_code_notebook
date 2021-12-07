import os

from aoc.day03.binary_diagnostic import simple_power_consumption


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**What is the power consumption of the submarine?**\n"
        f"{simple_power_consumption(numbers=inputs)}"
    )
