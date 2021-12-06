def dive_deeper(planned_course: list[str]) -> int:
    # Reads inputs
    horizontal_position = 0
    depth = 0
    for step in planned_course:
        action, unit = step.split()
        unit = int(unit)

        if action == 'forward':
            horizontal_position += unit
        elif action == 'down':
            depth += unit
        elif action == 'up':
            depth -= unit

    return horizontal_position * depth
