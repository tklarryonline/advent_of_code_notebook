import pytest

from aoc.day08.seven_segment_search import decode_signal, decode_signals, map_signal_segments, part01, part02


@pytest.mark.skip()
class TestDay08:
    inputs = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    def test_part01(self):
        assert part01(inputs=self.inputs) == 26

    def test_map_entry_segments(self):
        signals = [
            'acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab',
            'cdfeb', 'fcadb', 'cdfeb', 'cdbaf'
        ]
        expected = {
            'd': 'a',
            'e': 'b',
            'a': 'c',
            'f': 'd',
            'g': 'e',
            'b': 'f',
            'c': 'g'
        }

        assert map_signal_segments(signals) == expected

    def test_decode_signal(self):
        signals_map = {
            'd': 'a',
            'e': 'b',
            'a': 'c',
            'f': 'd',
            'g': 'e',
            'b': 'f',
            'c': 'g'
        }

        cases = [
            ('cdfeb', 5),
            ('fcadb', 3),
            ('cdfeb', 5),
            ('cdbaf', 3),
        ]

        for case, expected in cases:
            assert decode_signal(case, signals_map=signals_map)

    def test_decode_signals(self):
        signals_map = {
            'd': 'a',
            'e': 'b',
            'a': 'c',
            'f': 'd',
            'g': 'e',
            'b': 'f',
            'c': 'g'
        }

        assert decode_signals(
            signals=['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'],
            signals_map=signals_map
        ) == 5353

    def test_part02(self):
        assert part02(inputs=self.inputs) == 61229
