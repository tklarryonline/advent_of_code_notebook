def parse_inputs(inputs: str) -> list[int]:
    return sorted(
        int(i)
        for i in inputs.split(',')
    )


def calc_fuel(start: int, end: int) -> int:
    return sum(range(abs(start - end) + 1))


def align_submarines(inputs: str) -> int:
    positions = parse_inputs(inputs)
    mid_position = positions[int(len(positions) / 2)]

    return sum(
        abs(mid_position - p)
        for p in positions
    )


def align_submarines_part2(inputs: str) -> int:
    positions = parse_inputs(inputs)
    avg_position = sum(positions) / len(positions)

    return min(
        sum(
            calc_fuel(avg_p, p)
            for p in positions
        )
        for avg_p in [int(avg_position), round(avg_position)]
    )
