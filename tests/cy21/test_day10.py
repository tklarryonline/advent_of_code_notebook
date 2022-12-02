import pytest

from aoc.cy21.day10.syntax_scoring import IncorrectCloseError, fill_incomplete_braces, find_first_incorrect_close, fix_braces


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

    def test_fill_incomplete_braces(self):
        cases = [
            (list('[({([[{{'), 288957),
            (list('({[<{('), 5566),
            (list('((((<{<{{'), 1480781),
            (list('<{[{[{{[['), 995444),
            (list('<{(['), 294),
        ]
        for inputs, expected in cases:
            assert fill_incomplete_braces(open_braces=inputs) == expected

    def test_part01_inputs(self):
        illegal_scores, _ = fix_braces(inputs=self.inputs)
        assert illegal_scores == 26397

    def test_part02_inputs(self):
        _, middle_scores = fix_braces(inputs=self.inputs)
        assert middle_scores == 288957
