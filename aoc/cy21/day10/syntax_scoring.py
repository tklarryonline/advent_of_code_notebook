from collections import defaultdict
from dataclasses import dataclass


@dataclass
class IncorrectCloseError(Exception):
    brace: str


class BracesPair:
    open: str
    close: str
    error_score: int
    complete_score: int

    def __init__(self, pair: str, error_score: int = 0, complete_score: int = 0):
        assert len(pair) == 2
        self.open, self.close = pair
        self.error_score = error_score
        self.complete_score = complete_score


PAIRS = [
    BracesPair(pair='()', error_score=3, complete_score=1),
    BracesPair(pair='[]', error_score=57, complete_score=2),
    BracesPair(pair='{}', error_score=1197, complete_score=3),
    BracesPair(pair='<>', error_score=25137, complete_score=4),
]

OPEN_BRACES = [pair.open for pair in PAIRS]
CLOSE_BRACES = [pair.close for pair in PAIRS]
OPEN_TO_CLOSE_BRACES = dict(zip(OPEN_BRACES, CLOSE_BRACES))
COMPLETE_SCORES = {
    pair.open: pair.complete_score
    for pair in PAIRS
}


def find_first_incorrect_close(line: str) -> list[str]:
    queue = []

    for brace in line:
        if brace in OPEN_BRACES:
            queue.append(brace)
        elif brace in CLOSE_BRACES:
            if not queue or brace != OPEN_TO_CLOSE_BRACES[queue.pop()]:
                raise IncorrectCloseError(brace)

    return queue


def fill_incomplete_braces(open_braces: list[str]) -> int:
    score = 0
    for open_brace in reversed(open_braces):
        score = (score * 5) + COMPLETE_SCORES[open_brace]
    return score


def fix_braces(inputs: list[str]) -> tuple[int, int]:
    illegal_close_braces = defaultdict(int)

    complete_scores = []
    for line in inputs:
        try:
            incomplete_braces = find_first_incorrect_close(line)
        except IncorrectCloseError as ice:
            illegal_close_braces[ice.brace] += 1
            continue

        complete_scores.append(fill_incomplete_braces(open_braces=incomplete_braces))

    illegal_scores = sum(
        pair.error_score * illegal_close_braces[pair.close]
        for pair in PAIRS
    )

    middle_scores = sorted(complete_scores)[len(complete_scores) // 2]

    return illegal_scores, middle_scores
