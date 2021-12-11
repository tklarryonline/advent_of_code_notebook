import os

from aoc.day10.syntax_scoring import fix_brackets


def run():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs.txt'), mode='r') as f:
        inputs = f.read().splitlines()

    print('**What is the total syntax error score for those errors?**')
    print(fix_brackets(inputs))
