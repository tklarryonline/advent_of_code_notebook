from aoc.cy21.day02 import dive_and_aim, simply_dive


class TestDay02:
    inputs = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]

    def test_part01_sample_inputs(self):
        assert simply_dive(steps=self.inputs) == 150

    def test_part02_sample_inputs(self):
        assert dive_and_aim(steps=self.inputs) == 900
