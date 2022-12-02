import os

from aoc.cy21.day10.syntax_scoring import fix_braces


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs.txt'), mode='r') as f:
        inputs = f.read().splitlines()

    illegal_scores, middle_scores = fix_braces(inputs=inputs)
    print('**What is the total syntax error score for those errors?**')
    print(illegal_scores)
    print('**What is the middle score?**')
    print(middle_scores)
