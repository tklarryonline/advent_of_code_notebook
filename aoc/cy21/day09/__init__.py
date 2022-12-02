import os

from aoc.cy21.day09.smoke_basin import travel_inputs


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        input_value = f.read()

    risk, basins_product = travel_inputs(input_value)

    print(
        f"**What is the sum of the risk levels of all low points on your heightmap?**\n"
        f"{risk}\n"
        f"**What do you get if you multiply together the sizes of the three largest basins?**\n"
        f"{basins_product}\n"
    )
