import pytest

from aoc.day10.syntax_scoring import IncorrectCloseError, find_first_incorrect_close, fix_braces


class TestDay10:
    inputs = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ]

    def test_find_first_invalid(self):
        with pytest.raises(IncorrectCloseError) as ice_info:
            find_first_incorrect_close(line='{([(<{}[<>[]}>{[]{[(<()>')
        assert ice_info.value.brace == '}'

    def test_part01_inputs(self):
        illegal_scores, _ = fix_braces(inputs=self.inputs)
        assert illegal_scores == 26397

    def test_part02_inputs(self):
        _, middle_scores = fix_braces(inputs=self.inputs)
        assert middle_scores == 288957
