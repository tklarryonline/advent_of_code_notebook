from aoc.cy21.day01 import count_increase, count_increase_sliding_windows


class TestDay01:
    inputs = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    def test_part01_sample_inputs(self):
        assert count_increase(self.inputs) == 7

    def test_part02_sample_inputs(self):
        assert count_increase_sliding_windows(self.inputs) == 5
