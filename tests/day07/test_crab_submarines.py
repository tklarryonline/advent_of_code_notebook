from aoc.day07.crab_submarines import align_submarines


class TestDay07:
    inputs = '16,1,2,0,4,2,7,1,2,14'

    def test_align_submarines(self):
        assert align_submarines(self.inputs) == 37
