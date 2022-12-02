import os

from .sonar_sweep import count_increase, count_increase_sliding_windows


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        lines = f.readlines()

    inputs = [int(line) for line in lines]

    print(
        f"**How many measurements are larger than the previous measurement?**\n"
        f"{count_increase(inputs)}\n"
        f"**How many sums are larger than the previous sum?**\n"
        f"{count_increase_sliding_windows(inputs)}\n"
    )
