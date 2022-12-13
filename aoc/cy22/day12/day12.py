"""
Day 12
"""
import string
from time import process_time_ns

CHARACTER_SCORE = dict(zip(string.ascii_lowercase, range(len(string.ascii_lowercase))))
ADJACENT_SQUARES = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
)


def read_puzzle_inputs(file_name='samples.txt'):
    puzzle_map = []
    start_position = end_position = None
    with open(file_name, 'r') as f:
        for i, line in enumerate(f):
            if 'S' in line:
                start_position = (i, line.index('S'))
                line = line.replace('S', 'a')
            if 'E' in line:
                end_position = (i, line.index('E'))
                line = line.replace('E', 'z')
            puzzle_map.append([
                CHARACTER_SCORE[c]
                for c in line.strip()
            ])

    return puzzle_map, start_position, end_position


def calculate_distance(puzzle_map, start, end=None):
    map_height = len(puzzle_map)
    map_width = len(puzzle_map[0])
    closed_list = {
        start: 0
    }
    open_list = [start]

    while open_list:
        current_i, current_j = current_node = open_list.pop(0)
        current_value = puzzle_map[current_i][current_j]
        current_steps = closed_list[current_node]

        for i, j in ADJACENT_SQUARES:
            step_i, step_j = step = (current_i + i, current_j + j)

            # Have we visited this step before?
            #  Or is it out of range?
            if step in closed_list or step_i in [-1, map_height] or step_j in [-1, map_width]:
                continue

            step_value = puzzle_map[step_i][step_j]
            if end:
                if step_value - current_value > 1:
                    continue

                closed_list[step] = current_steps + 1
                open_list.append(step)

                if step == end:
                    return current_steps + 1
            else:
                if step_value < current_value - 1:
                    continue

                closed_list[step] = current_steps + 1
                open_list.append(step)

                if step_value == 0:
                    return current_steps + 1

    raise AssertionError(f"Can't find the path from {start} to {end}")


if __name__ == '__main__':
    puzzle_map, start_position, end_position = read_puzzle_inputs(file_name='inputs.txt')

    start_time = process_time_ns()
    p1_result = calculate_distance(puzzle_map, start_position, end_position)
    elapsed_time = process_time_ns() - start_time

    print(f'Part 1 = {p1_result}. Took {elapsed_time}ns.')

    start_time = process_time_ns()
    p2_result = calculate_distance(puzzle_map, start=end_position)
    elapsed_time = process_time_ns() - start_time

    print(f'Part 2 = {p2_result}. Took {elapsed_time}ns.')
