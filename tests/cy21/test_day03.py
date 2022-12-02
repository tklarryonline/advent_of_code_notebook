from aoc.cy21.day03.binary_diagnostic import (
    binary_flip,
    count_most_common_bits,
    life_support,
    parse_inputs,
    power_consumption,
)


class TestDay03:
    inputs = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

    def test_parse_inputs(self):
        expected = [
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 1]
        ]

        assert parse_inputs([
            '0111',
            '0100',
            '1111',
            '0111',
            '0001'
        ]) == expected

    def test_binary_flip(self):
        cases = [
            ('00100', '11011'),
            ('1010', '0101'),
            ('101', '010'),
            ('01', '10'),
            ('0', '1')
        ]
        for binary_str, expected in cases:
            assert binary_flip(binary_str) == expected

    def test_count_most_common_bits(self):
        cases = [
            ((0, 1, 1, 1), 1),
            ((0, 1, 0, 0), 0),
            ((1, 1, 1, 1), 1),
            ((0, 1, 0, 1), 1),
            ((0, 0, 0, 1), 0)
        ]

        for bits, expected in cases:
            assert count_most_common_bits(bits) == expected

    def test_part01_sample_inputs(self):
        assert power_consumption(numbers=self.inputs) == 198

    def test_part02_sample_inputs(self):
        assert life_support(numbers=self.inputs) == 230
