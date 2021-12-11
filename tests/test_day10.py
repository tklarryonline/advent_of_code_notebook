from aoc.day10.syntax_scoring import find_first_incorrect_close, fix_brackets


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
        assert find_first_incorrect_close(line='{([(<{}[<>[]}>{[]{[(<()>') == '}'

    def test_part01_inputs(self):
        assert fix_brackets(inputs=self.inputs) == 26397
