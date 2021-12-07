from aoc.day03.binary_diagnostic import simple_power_consumption


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

    def test_part01_sample_inputs(self):
        assert simple_power_consumption(numbers=self.inputs) == 198

    def test_part02_sample_inputs(self):
        pass
