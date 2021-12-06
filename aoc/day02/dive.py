def simply_dive(steps: list[str]) -> int:
    horizontal_position = 0
    depth = 0

    for step in steps:
        action, unit = step.split()
        unit = int(unit)

        if action == 'down':
            depth += unit
        elif action == 'up':
            depth -= unit
        elif action == 'forward':
            horizontal_position += unit

    return horizontal_position * depth


def dive_and_aim(steps: list[str]) -> int:
    horizontal_position = 0
    aim = 0
    depth = 0

    for step in steps:
        action, unit = step.split()
        unit = int(unit)

        if action == 'down':
            aim += unit
        elif action == 'up':
            aim -= unit
        elif action == 'forward':
            horizontal_position += unit
            depth += aim * unit

    return horizontal_position * depth
