def align_submarines(inputs: str) -> int:
    positions = sorted(
        int(i)
        for i in inputs.split(',')
    )
    mid_position = positions[int(len(positions) / 2)]

    return sum(
        abs(mid_position - p)
        for p in positions
    )
