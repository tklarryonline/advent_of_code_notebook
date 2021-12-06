from aoc.day02.dive import dive_deeper


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
        assert dive_deeper(planned_course=self.inputs) == 150
