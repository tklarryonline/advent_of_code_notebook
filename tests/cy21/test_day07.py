from aoc.cy21.day07 import align_submarines, align_submarines_part2, calc_fuel


class TestDay07:
    inputs = '16,1,2,0,4,2,7,1,2,14'

    def test_align_submarines(self):
        assert align_submarines(self.inputs) == 37

    def test_align_submarines_part2(self):
        assert align_submarines_part2(self.inputs) == 168

    def test_calculate_fuel_increasing_rate(self):
        cases = [
            (16, 5, 66),
            (1, 5, 10),
            (2, 5, 6)
        ]
        for start, end, expected in cases:
            assert calc_fuel(start, end) == expected
