from aoc.cy21.day06.lanternfish import part01_count_fishes


class TestDay06:
    inputs = '3, 4, 3, 1, 2'

    def test_count_fishes(self):
        assert part01_count_fishes(inputs=self.inputs, days=18) == 26
        assert part01_count_fishes(inputs=self.inputs, days=80) == 5934
        assert part01_count_fishes(inputs=self.inputs, days=256) == 26984457539
