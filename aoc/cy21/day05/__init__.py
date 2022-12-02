import os


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs.txt"), mode='r') as f:
        inputs = f.readlines()

    print(
        f"**What will your final score be if you choose that board?**\n"
    )
