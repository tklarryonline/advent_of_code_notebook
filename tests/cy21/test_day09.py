from aoc.cy21.day09 import travel_inputs


class TestDay09:
    input_value = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    def test_part01(self):
        risk, _ = travel_inputs(self.input_value)
        assert risk == 15

    def test_part02(self):
        _, basins_product = travel_inputs(self.input_value)
        assert basins_product == 1134
