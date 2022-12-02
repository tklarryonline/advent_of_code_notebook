from collections import namedtuple
from dataclasses import dataclass, field


@dataclass
class Digit:
    digit: int
    patterns: str
    num_segments: int = field(init=False)

    def __post_init__(self):
        self.num_segments = len(self.patterns)

    def equals(self, pattern):
        if isinstance(pattern, str):
            return set(self.patterns) == set(pattern)

        return set(self.patterns) == pattern


Entry = namedtuple(
    typename='Entry',
    field_names=('signal_patterns', 'outputs')
)

SIGNAL_CHARS = set('abcdefg')

DIGIT_SEGMENTS = [
    Digit(digit=0, patterns='abcefg'),
    Digit(digit=1, patterns='cf'),
    Digit(digit=2, patterns='acdeg'),
    Digit(digit=3, patterns='acdfg'),
    Digit(digit=4, patterns='bcdf'),
    Digit(digit=5, patterns='abdfg'),
    Digit(digit=6, patterns='abdefg'),
    Digit(digit=7, patterns='acf'),
    Digit(digit=8, patterns='abcdefg'),
    Digit(digit=9, patterns='abcdfg'),
]

SPECIAL_DIGITS = [1, 4, 7, 8]

SPECIAL_DIGITS_BY_LENGTH: dict[int, Digit] = {
    DIGIT_SEGMENTS[digit].num_segments: DIGIT_SEGMENTS[digit]
    for digit in SPECIAL_DIGITS
}

TARGET_NUM_SEGMENTS = [
    DIGIT_SEGMENTS[digit].num_segments
    for digit in SPECIAL_DIGITS
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


def part01(inputs: list[str]) -> int:
    entries = parse_entries(inputs)

    return sum(
        len([
            o
            for o in entry.outputs
            if len(o) in TARGET_NUM_SEGMENTS
        ])
        for entry in entries
    )


def map_signal_segments(signals: list[str]) -> dict[str, str]:
    char_map = dict()

    # Finds all segments of 1, 4, 7, 8
    special_signals = sorted([
        signal
        for signal in signals
        if len(signal) in TARGET_NUM_SEGMENTS
    ], key=len)

    unfilled_chrs_original = SIGNAL_CHARS.copy()
    unfilled_chrs_new = SIGNAL_CHARS.copy()

    for signal in special_signals:
        # Finds the digit matching with the signal len
        possible_digit = SPECIAL_DIGITS_BY_LENGTH[len(signal)]

        # Now it's easy, just do the map from the possible digit's segments
        # to the signal
        for new_chr, original_chr in zip(signal, possible_digit.patterns):
            if new_chr not in char_map and original_chr not in char_map.values():
                char_map[new_chr] = original_chr
                unfilled_chrs_original.discard(original_chr)
                unfilled_chrs_new.discard(new_chr)

    # Back-fills the maps
    if not unfilled_chrs_original and not unfilled_chrs_new:
        # My work here is done
        return char_map

    # If there are more than one unfilled character then we're doomed
    print(unfilled_chrs_original)
    print(unfilled_chrs_new)
    assert len(unfilled_chrs_original) == len(unfilled_chrs_new) == 1
    char_map[unfilled_chrs_new.pop()] = unfilled_chrs_original.pop()

    return char_map


def decode_signal(input_signal: str, signals_map: dict[str, str]) -> int:
    actual_signals = set(
        signals_map[c]
        for c in input_signal
    )
    # Find the digit
    digit = [
        d
        for d in DIGIT_SEGMENTS
        if d.equals(actual_signals)
    ].pop()

    return digit.digit


def decode_signals(signals: list[str], signals_map: dict[str, str]) -> int:
    return int(''.join(
        str(decode_signal(signal, signals_map))
        for signal in signals
    ))


def part02(inputs: list[str]) -> int:
    entries = parse_entries(inputs)

    output_sum = 0
    for entry in entries:
        signals_map = map_signal_segments(signals=entry.signal_patterns)
        output_value = decode_signals(signals=entry.outputs, signals_map=signals_map)
        output_sum += output_value

    return output_sum
