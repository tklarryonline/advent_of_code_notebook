from typing import Sequence


def parse_inputs(numbers: list[str]) -> list[list[int]]:
    return [
        [int(bit) for bit in number.strip()]
        for number in numbers
    ]


def transpose(matrix: list[Sequence[int]]) -> list[Sequence[int]]:
    return list(zip(*matrix))


def binary_flip(bit: str) -> str:
    return bin((int(bit, 2) ^ (2 ** (len(bit) + 1) - 1)))[3:]


def count_most_common_bits(bits: Sequence[int]) -> int:
    one_appearances = sum(1 for b in bits if b == 1)
    return 1 if one_appearances >= (len(bits) / 2) else 0


def power_consumption(numbers: list[str]) -> int:
    matrix = transpose(parse_inputs(numbers))

    gamma = ''.join(str(count_most_common_bits(m)) for m in matrix)
    epsilon = binary_flip(gamma)

    return int(gamma, 2) * int(epsilon, 2)


def life_support(numbers: list[str]) -> int:
    matrix = parse_inputs(numbers)

    oxygen = _life_support(matrix)
    oxygen = ''.join(str(x) for x in oxygen)

    co2 = _life_support(matrix, take_most_common=False)
    co2 = ''.join(str(x) for x in co2)

    return int(oxygen, 2) * int(co2, 2)


def _life_support(matrix: list[Sequence[int]], take_most_common=True, position=0) -> Sequence[int]:
    if len(matrix) == 1:
        return matrix[0]

    transposed = transpose(matrix)
    most_common = count_most_common_bits(transposed[position])
    if take_most_common:
        filtered_matrix = [m for m in matrix if m[position] == most_common]
    else:
        filtered_matrix = [m for m in matrix if m[position] != most_common]

    return _life_support(matrix=filtered_matrix, take_most_common=take_most_common, position=position + 1)
