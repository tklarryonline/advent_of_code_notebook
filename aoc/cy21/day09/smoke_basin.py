def parse_input(input_value: str) -> list[list[int]]:
    return [
        [int(chr) for chr in line]
        for line in input_value.splitlines()
    ]


def get_adjacent_coordinates(x, y, x_size, y_size):
    possible_adjacency = [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1)
    ]

    return [
        (y1, x1)
        for y1, x1 in possible_adjacency
        if 0 <= y1 < y_size and 0 <= x1 < x_size
    ]


def find_basin(matrix, x, y, x_size, y_size):
    """From (x, y), expands and find all adjacent cells until reach 9"""
    basin = set()
    queue = [(y, x)]

    while queue:
        current = queue.pop()
        basin.add(current)

        current_y, current_x = current
        current_value = matrix[current_y][current_x]

        adjacent_coordinates = get_adjacent_coordinates(current_x, current_y, x_size, y_size)
        for ay, ax in adjacent_coordinates:
            adjacent_value = matrix[ay][ax]
            if current_value < adjacent_value < 9 and adjacent_value not in basin:
                queue.append((ay, ax))

    return len(basin)


def travel_inputs(input_value: str) -> tuple:
    matrix = parse_input(input_value)
    y_size = len(matrix)

    risk = 0
    basins = []
    for y, row in enumerate(matrix):
        x_size = len(row)
        for x, cell in enumerate(row):
            adjacent_coordinates = get_adjacent_coordinates(x, y, x_size, y_size)

            if not all(cell < matrix[ay][ax] for ay, ax in adjacent_coordinates):
                continue

            # Part 1's calculation
            risk += 1 + cell
            basins.append(find_basin(matrix, x, y, x_size, y_size))

    # Part 2 calculations
    basins_product = 1
    basins = sorted(basins)
    for basin in basins[-3:]:
        basins_product *= basin

    return risk, basins_product
