from collections import namedtuple

Digit = namedtuple(
    typename='Digit',
    field_names=('digit', 'patterns', 'num_segments')
)

Entry = namedtuple(
    typename='Entry',
    field_names=('signal_patterns', 'outputs')
)

DIGIT_SEGMENTS = [
    Digit(digit=0, patterns=set('abcefg'), num_segments=6),
    Digit(digit=1, patterns=set('cf'), num_segments=2),
    Digit(digit=2, patterns=set('acdeg'), num_segments=5),
    Digit(digit=3, patterns=set('acdfg'), num_segments=5),
    Digit(digit=4, patterns=set('bcdf'), num_segments=4),
    Digit(digit=5, patterns=set('abdfg'), num_segments=5),
    Digit(digit=6, patterns=set('abdefg'), num_segments=6),
    Digit(digit=7, patterns=set('acf'), num_segments=3),
    Digit(digit=8, patterns=set('abcdefg'), num_segments=7),
    Digit(digit=9, patterns=set('abcdfg'), num_segments=6),
]


def parse_entry(entry: str) -> Entry:
    """
    Parse the below entry:
        be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    To the following data structure:
        Entry(<list of patterns>, <output>)

    :param entry:
    :return:
    """
    signal_patterns, output = entry.split('|')
    return Entry(signal_patterns.split(), output.split())


def parse_entries(inputs: list[str]) -> list[Entry]:
    return [parse_entry(entry) for entry in inputs]


def count_output_digits(entries: list[Entry], digits: list[int]) -> int:
    TARGET_NUM_SEGMENTS = [
        DIGIT_SEGMENTS[digit].num_segments
        for digit in digits
    ]

    return sum(
        len([
            o
            for o in entry.outputs
            if len(o) in TARGET_NUM_SEGMENTS
        ])
        for entry in entries
    )


def part01(inputs: list[str]) -> int:
    entries = parse_entries(inputs)

    return count_output_digits(entries=entries, digits=[1, 4, 7, 8])
