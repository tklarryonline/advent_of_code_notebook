import os

from aoc.cy21.day07.crab_submarines import align_submarines, align_submarines_part2


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**How much fuel must they spend to align to that position?**\n"
        f"Part 1: {align_submarines(inputs[0])}\n"
        f"Part 2: {align_submarines_part2(inputs[0])}\n"
    )
