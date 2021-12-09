def parse_input(input_value: str) -> list[list[int]]:
    return [
        [int(chr) for chr in line]
        for line in input_value.splitlines()
    ]


def get_adjacent_cells(matrix, x, y, x_size, y_size):
    adjacent_cells = []

    if y > 0:
        adjacent_cells.append(matrix[y - 1][x])

    if y + 1 < y_size:
        adjacent_cells.append(matrix[y + 1][x])

    if x > 0:
        adjacent_cells.append(matrix[y][x - 1])

    if x + 1 < x_size:
        adjacent_cells.append(matrix[y][x + 1])

    return adjacent_cells


def part01_sum_risk(input_value: str) -> int:
    matrix = parse_input(input_value)
    y_size = len(matrix)

    risk = 0
    for y, row in enumerate(matrix):
        x_size = len(row)
        for x, cell in enumerate(row):
            adjacent_cells = get_adjacent_cells(matrix, x, y, x_size, y_size)

            if all(cell < adj_cell for adj_cell in adjacent_cells):
                risk += 1 + cell

    return risk
