from aoc.day09.smoke_basin import part01_sum_risk


class TestDay09:
    input_value = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    def test_part01(self):
        assert part01_sum_risk(self.input_value) == 15
