from collections import defaultdict


class BracketPair:
    open: str
    close: str
    points: int

    def __init__(self, pair: str, points: int = 0):
        assert len(pair) == 2
        self.open, self.close = pair
        self.points = points


PAIRS = [
    BracketPair(pair='()', points=3),
    BracketPair(pair='[]', points=57),
    BracketPair(pair='{}', points=1197),
    BracketPair(pair='<>', points=25137),
]

OPEN_BRACKETS = [pair.open for pair in PAIRS]
CLOSE_BRACKETS = [pair.close for pair in PAIRS]
MAPPED_BRACKETS = dict(zip(OPEN_BRACKETS, CLOSE_BRACKETS))


def find_first_incorrect_close(line: str) -> str:
    queue = []

    for bracket in line:
        if bracket in OPEN_BRACKETS:
            queue.append(bracket)
        elif bracket in CLOSE_BRACKETS:
            if not queue or bracket != MAPPED_BRACKETS[queue.pop()]:
                return bracket


def fix_brackets(inputs: list[str]) -> int:
    illegal_close_brackets = defaultdict(int)

    for line in inputs:
        invalid_close = find_first_incorrect_close(line)

        if invalid_close:
            illegal_close_brackets[invalid_close] += 1

    return sum(
        pair.points * illegal_close_brackets[pair.close]
        for pair in PAIRS
    )
