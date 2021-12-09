import os

from aoc.day09.smoke_basin import part01_sum_risk


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        input_value = f.read()

    print(
        f"**What is the sum of the risk levels of all low points on your heightmap?**\n"
        f"{part01_sum_risk(input_value)}\n"
    )
