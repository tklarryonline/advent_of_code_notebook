from collections import defaultdict
from dataclasses import dataclass


@dataclass
class IncorrectCloseError(Exception):
    brace: str


class BracesPair:
    open: str
    close: str
    points: int

    def __init__(self, pair: str, points: int = 0):
        assert len(pair) == 2
        self.open, self.close = pair
        self.points = points


PAIRS = [
    BracesPair(pair='()', points=3),
    BracesPair(pair='[]', points=57),
    BracesPair(pair='{}', points=1197),
    BracesPair(pair='<>', points=25137),
]

OPEN_BRACES = [pair.open for pair in PAIRS]
CLOSE_BRACES = [pair.close for pair in PAIRS]
OPEN_TO_CLOSE_BRACES = dict(zip(OPEN_BRACES, CLOSE_BRACES))


def find_first_incorrect_close(line: str) -> list[str]:
    queue = []

    for brace in line:
        if brace in OPEN_BRACES:
            queue.append(brace)
        elif brace in CLOSE_BRACES:
            if not queue or brace != OPEN_TO_CLOSE_BRACES[queue.pop()]:
                raise IncorrectCloseError(brace)

    return queue


def fix_braces(inputs: list[str]) -> tuple[int, int]:
    illegal_close_braces = defaultdict(int)

    incomplete_lines = []
    for line in inputs:
        try:
            incomplete_braces = find_first_incorrect_close(line)
        except IncorrectCloseError as ice:
            illegal_close_braces[ice.brace] += 1
            continue

        incomplete_lines.append(line)

    illegal_scores = sum(
        pair.points * illegal_close_braces[pair.close]
        for pair in PAIRS
    )

    return illegal_scores, 0
